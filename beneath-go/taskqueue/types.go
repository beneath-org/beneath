package taskqueue

import (
	"context"
	"fmt"
	"reflect"
	"time"

	"github.com/beneath-core/beneath-go/core/timeutil"
	uuid "github.com/satori/go.uuid"
	"github.com/vmihailenco/msgpack"

	pb "github.com/beneath-core/beneath-go/proto"
)

// Task is the abstract interface for a worker task
type Task interface {
	Run(ctx context.Context) error
}

var (
	taskRegistry map[string]reflect.Type
)

func registerTask(task Task) {
	if taskRegistry == nil {
		taskRegistry = make(map[string]reflect.Type)
	}
	t := reflect.TypeOf(task)
	taskRegistry[t.Name()] = t
}

func encodeTask(task Task) (*pb.QueuedTask, error) {
	t := reflect.TypeOf(task)
	data, err := msgpack.Marshal(task)
	if err != nil {
		return nil, err
	}

	return &pb.QueuedTask{
		UniqueId:  uuid.NewV4().String(),
		Name:      t.Name(),
		Timestamp: timeutil.UnixMilli(time.Now()),
		Data:      data,
	}, nil
}

func decodeTask(qt *pb.QueuedTask) (Task, error) {
	t, ok := taskRegistry[qt.Name]
	if !ok {
		return nil, fmt.Errorf("cannot find task with name '%s'", qt.Name)
	}

	tval := reflect.New(t)
	task, ok := tval.Interface().(Task)
	if !ok {
		return nil, fmt.Errorf("cannot cast type '%s' to Task", qt.Name)
	}

	err := msgpack.Unmarshal(qt.Data, task)
	if err != nil {
		return nil, err
	}

	return task, nil
}