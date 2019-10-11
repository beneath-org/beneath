package control

import (
	"context"
	"fmt"
	"net/http"

	"github.com/vektah/gqlparser/ast"

	"github.com/beneath-core/beneath-go/core/log"

	"github.com/beneath-core/beneath-go/control/auth"
	"github.com/beneath-core/beneath-go/control/gql"
	"github.com/beneath-core/beneath-go/control/migrations"
	"github.com/beneath-core/beneath-go/control/resolver"
	"github.com/beneath-core/beneath-go/core"
	"github.com/beneath-core/beneath-go/core/middleware"
	"github.com/beneath-core/beneath-go/core/segment"
	"github.com/beneath-core/beneath-go/db"

	"github.com/99designs/gqlgen/graphql"
	"github.com/99designs/gqlgen/handler"
	"github.com/go-chi/chi"
	chimiddleware "github.com/go-chi/chi/middleware"
	"github.com/rs/cors"
	"github.com/vektah/gqlparser/gqlerror"
)

type configSpecification struct {
	ControlPort  int    `envconfig:"CONTROL_PORT" required:"true" default:"8080"`
	ControlHost  string `envconfig:"CONTROL_HOST" required:"true"`
	FrontendHost string `envconfig:"FRONTEND_HOST" required:"true"`

	RedisURL         string `envconfig:"CONTROL_REDIS_URL" required:"true"`
	PostgresHost     string `envconfig:"CONTROL_POSTGRES_HOST" required:"true"`
	PostgresUser     string `envconfig:"CONTROL_POSTGRES_USER" required:"true"`
	PostgresPassword string `envconfig:"CONTROL_POSTGRES_PASSWORD" required:"true"`

	StreamsDriver   string `envconfig:"ENGINE_STREAMS_DRIVER" required:"true"`
	TablesDriver    string `envconfig:"ENGINE_TABLES_DRIVER" required:"true"`
	WarehouseDriver string `envconfig:"ENGINE_WAREHOUSE_DRIVER" required:"true"`

	SegmentSecret    string `envconfig:"CONTROL_SEGMENT_SECRET" required:"true"`
	SessionSecret    string `envconfig:"CONTROL_SESSION_SECRET" required:"true"`
	GithubAuthID     string `envconfig:"CONTROL_GITHUB_AUTH_ID" required:"true"`
	GithubAuthSecret string `envconfig:"CONTROL_GITHUB_AUTH_SECRET" required:"true"`
	GoogleAuthID     string `envconfig:"CONTROL_GOOGLE_AUTH_ID" required:"true"`
	GoogleAuthSecret string `envconfig:"CONTROL_GOOGLE_AUTH_SECRET" required:"true"`
}

var (
	// Config for control
	Config configSpecification
)

func init() {
	// load config
	core.LoadConfig("beneath", &Config)

	// connect postgres, redis and engine
	db.InitPostgres(Config.PostgresHost, Config.PostgresUser, Config.PostgresPassword)
	db.InitRedis(Config.RedisURL)
	db.InitEngine(Config.StreamsDriver, Config.TablesDriver, Config.WarehouseDriver)

	// run migrations
	migrations.MustRunUp(db.DB)

	// init segment
	segment.InitClient(Config.SegmentSecret)

	// configure auth
	auth.InitGoth(&auth.GothConfig{
		ClientHost:       Config.FrontendHost,
		SessionSecret:    Config.SessionSecret,
		BackendHost:      Config.ControlHost,
		GithubAuthID:     Config.GithubAuthID,
		GithubAuthSecret: Config.GithubAuthSecret,
		GoogleAuthID:     Config.GoogleAuthID,
		GoogleAuthSecret: Config.GoogleAuthSecret,
	})
}

// ListenAndServeHTTP serves the GraphQL API on HTTP
func ListenAndServeHTTP(port int) error {
	router := chi.NewRouter()

	router.Use(chimiddleware.RealIP)
	router.Use(chimiddleware.DefaultCompress)
	router.Use(middleware.InjectTags)
	router.Use(middleware.Logger)
	router.Use(middleware.Recoverer)
	router.Use(middleware.Auth)
	router.Use(middleware.IPRateLimit())
	router.Use(segmentMiddleware)

	// Add CORS
	router.Use(cors.New(cors.Options{
		AllowedOrigins: []string{
			Config.FrontendHost,
			Config.ControlHost,
		},
		AllowedHeaders:   []string{"*"},
		AllowCredentials: true,
		Debug:            false,
	}).Handler)

	// Authentication endpoints
	router.Mount("/auth", auth.Router())

	// Add health check
	router.Get("/", healthCheck)
	router.Get("/healthz", healthCheck)

	// Add playground
	router.Handle("/playground", handler.Playground("Beneath", "/graphql"))

	// Add graphql server
	router.Handle("/graphql", handler.GraphQL(
		makeExecutableSchema(),
		makeQueryLoggingMiddleware(),
		makeGraphQLErrorPresenter(),
		handler.RecoverFunc(func(ctx context.Context, err interface{}) error {
			panic(err)
		}),
	))

	// Serve
	log.S.Infow("control http started", "port", port)
	return http.ListenAndServe(fmt.Sprintf(":%d", port), router)
}

func healthCheck(w http.ResponseWriter, r *http.Request) {
	if db.Healthy() {
		w.WriteHeader(http.StatusOK)
		w.Write([]byte(http.StatusText(http.StatusOK)))
	} else {
		log.S.Errorf("Control database health check failed")
		http.Error(w, http.StatusText(http.StatusInternalServerError), http.StatusInternalServerError)
	}
}

func makeExecutableSchema() graphql.ExecutableSchema {
	return gql.NewExecutableSchema(gql.Config{Resolvers: &resolver.Resolver{}})
}

type gqlLog struct {
	Op    string `json:"op"`
	Name  string `json:"name,omitempty"`
	Field string `json:"field"`
	Error error  `json:"error,omitempty"`
}

func makeQueryLoggingMiddleware() handler.Option {
	return handler.RequestMiddleware(func(ctx context.Context, next func(ctx context.Context) []byte) []byte {
		reqCtx := graphql.GetRequestContext(ctx)
		middleware.SetTagsPayload(ctx, logInfoFromRequestContext(reqCtx))
		return next(ctx)
	})
}

func logInfoFromRequestContext(ctx *graphql.RequestContext) interface{} {
	var queries []gqlLog
	for _, op := range ctx.Doc.Operations {
		for _, sel := range op.SelectionSet {
			if field, ok := sel.(*ast.Field); ok {
				name := op.Name
				if name == "" {
					name = "Unnamed"
				}
				queries = append(queries, gqlLog{
					Op:    string(op.Operation),
					Name:  name,
					Field: field.Name,
				})
			}
		}
	}
	return queries
}

func makeGraphQLErrorPresenter() handler.Option {
	return handler.ErrorPresenter(func(ctx context.Context, err error) *gqlerror.Error {
		tags := middleware.GetTags(ctx)
		if q, ok := tags.Payload.(gqlLog); ok {
			q.Error = err
		}
		// Uncomment this line to print resolver error details in the console
		// fmt.Printf("Error in GraphQL Resolver: %s", err.Error())
		return graphql.DefaultErrorPresenter(ctx, err)
	})
}

func segmentMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// run the request first, thus setting tags.Payload
		next.ServeHTTP(w, r)

		tags := middleware.GetTags(r.Context())
		gqlLogs, ok := tags.Payload.([]gqlLog)
		if !ok {
			return
		}

		for _, l := range gqlLogs {
			name := "GQL: " + l.Name
			segment.TrackHTTP(r, name, l)
		}
	})
}
