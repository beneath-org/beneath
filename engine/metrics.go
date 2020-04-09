package engine

import (
	"context"
	"time"

	uuid "github.com/satori/go.uuid"

	pb "gitlab.com/beneath-hq/beneath/engine/proto"
	"gitlab.com/beneath-hq/beneath/pkg/timeutil"
)

// CommitUsage writes a batch of usage metrics
func (e *Engine) CommitUsage(ctx context.Context, id uuid.UUID, period timeutil.Period, ts time.Time, usage pb.QuotaUsage) error {
	return e.Lookup.CommitUsage(ctx, id, period, ts, usage)
}

// ClearUsage clears all usage data saved for the id
func (e *Engine) ClearUsage(ctx context.Context, id uuid.UUID) error {
	return e.Lookup.ClearUsage(ctx, id)
}

// ReadSingleUsage reads usage metrics for one key
func (e *Engine) ReadSingleUsage(ctx context.Context, id uuid.UUID, period timeutil.Period, ts time.Time) (pb.QuotaUsage, error) {
	return e.Lookup.ReadSingleUsage(ctx, id, period, ts)
}

// ReadUsage reads usage metrics for multiple periods and calls fn one by one
func (e *Engine) ReadUsage(ctx context.Context, id uuid.UUID, period timeutil.Period, from time.Time, until time.Time, fn func(ts time.Time, usage pb.QuotaUsage) error) error {
	return e.Lookup.ReadUsage(ctx, id, period, from, until, fn)
}
