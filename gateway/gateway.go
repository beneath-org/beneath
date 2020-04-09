package gateway

import (
	"time"

	"gitlab.com/beneath-hq/beneath/engine"
	"gitlab.com/beneath-hq/beneath/gateway/subscriptions"
	"gitlab.com/beneath-hq/beneath/internal/metrics"
)

var (
	// Metrics collects stats on records read from/written to Beneath
	Metrics *metrics.Broker

	// Subscriptions handles real-time data subscriptions
	Subscriptions *subscriptions.Broker
)

// InitMetrics initializes the Metrics global
func InitMetrics(cacheSize int, commitInterval time.Duration) {
	Metrics = metrics.NewBroker(cacheSize, commitInterval)
}

// InitSubscriptions initializes the Subscriptionsglobal
func InitSubscriptions(eng *engine.Engine) {
	Subscriptions = subscriptions.NewBroker(eng)
}
