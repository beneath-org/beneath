package gateway

import (
	"fmt"
	"log"
	"net/http"

	"github.com/beneath-core/beneath-go/control/auth"
	"github.com/beneath-core/beneath-go/control/model"
	"github.com/beneath-core/beneath-go/core/httputil"

	"github.com/go-chi/chi"
	"github.com/go-chi/chi/middleware"
	uuid "github.com/satori/go.uuid"
)

// ListenAndServeHTTP serves a HTTP API
func ListenAndServeHTTP(port int) error {
	log.Printf("HTTP server running on port %d\n", port)
	return http.ListenAndServe(fmt.Sprintf(":%d", port), httpHandler())
}

func httpHandler() http.Handler {
	handler := chi.NewRouter()

	// handler.Use(middleware.RealIP) // TODO: Uncomment if IPs are a problem behind nginx
	handler.Use(middleware.Logger)
	handler.Use(middleware.Recoverer)
	handler.Use(auth.HTTPMiddleware)

	// TODO: Add graphql
	// GraphQL endpoints
	// handler.Get("/graphql")
	// handler.Get("/projects/{projectName}/graphql")

	// REST endpoints
	handler.Method("GET", "/projects/{projectName}/streams/{streamName}", httputil.AppHandler(getFromProjectAndStream))
	handler.Method("GET", "/streams/instances/{instanceID}", httputil.AppHandler(getFromInstance))
	handler.Method("POST", "/streams/instances/{instanceID}", httputil.AppHandler(postToInstance))

	return handler
}

func getFromProjectAndStream(w http.ResponseWriter, r *http.Request) error {
	projectName := chi.URLParam(r, "projectName")
	streamName := chi.URLParam(r, "streamName")
	instanceID := model.FindInstanceIDByNameAndProject(streamName, projectName)
	if instanceID == uuid.Nil {
		return httputil.NewError(404, "instance for stream not found")
	}

	return getFromInstanceID(w, r, instanceID)
}

func getFromInstance(w http.ResponseWriter, r *http.Request) error {
	instanceID, err := uuid.FromString(chi.URLParam(r, "instanceID"))
	if err != nil {
		return httputil.NewError(404, "instance not found -- malformed ID")
	}

	return getFromInstanceID(w, r, instanceID)
}

func getFromInstanceID(w http.ResponseWriter, r *http.Request, instanceID uuid.UUID) error {
	key := auth.GetKey(r.Context())

	stream := model.FindCachedStreamByCurrentInstanceID(instanceID)
	if stream == nil {
		return httputil.NewError(404, "stream not found")
	}

	if !key.ReadsProject(stream.ProjectID) {
		return httputil.NewError(403, "token doesn't grant right to read this stream")
	}

	// TODO
	// Read from BT in accordance with how we end up writing it
	// Support filter, limit, page (see https://docs.hasura.io/1.0/graphql/manual/queries/query-filters.html)

	w.Write([]byte(fmt.Sprintf("Hello Stream Instance %s", instanceID.String())))
	return nil
}

func postToInstance(w http.ResponseWriter, r *http.Request) error {
	key := auth.GetKey(r.Context())

	instanceID, err := uuid.FromString(chi.URLParam(r, "instanceID"))
	if err != nil {
		return httputil.NewError(404, "instance not found -- malformed ID")
	}

	stream := model.FindCachedStreamByCurrentInstanceID(instanceID)
	if err == nil {
		return httputil.NewError(404, "stream not found")
	}

	if !key.WritesStream(stream) {
		return httputil.NewError(403, "token doesn't grant right to read this stream")
	}

	// TODO: Write item

	return nil
}

// var body interface{}
// err = json.NewDecoder(r.Body).Decode(&body)
// if err != nil {
// 	return NewHTTPError(400, "request body must be json")
// }

//

// err = beneath.WriteItem(instanceID, schema, data, eventTime, seqNo)
// if err != nil {
// 	if inputerr, ok := err.(*beneath.WriteInputError); ok {
// 		return NewHTTPError(400, inputerr.Error())
// 	} else {
// 		return NewHTTPError(500, err.Error())
// 	}
// }

// SPEC
// - Get schema for stream
// - Read payload (JSON) and encode with schema
// - Write to pubsub

/*
	INPUT
	- instanceID
	- data (json)
	- timestamp: default now
	- seq no: default random

	- eventTime
	- seqNo

	PAYLOAD TO PUBSUB
	- streamInstanceId
	- ksuid: timestamp + seqno
	- data (binary encoded according to schema)

	INTO BIGQUERY
	- create view beneath.projectName.streamName -> latest streamInstanceId
	- beneath.projectName.streamInstanceId
		- ksuid, timestamp, insert_time, fields in data

	INTO BIGTABLE
	- streamInstanceId#key (key read from data + schema)
	- ksuid, updated_on, fields_in_data (on bigger than previous ksuid)

*/
