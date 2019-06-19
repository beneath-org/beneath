// Code generated by protoc-gen-go. DO NOT EDIT.
// source: gateway.proto

package proto

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	grpc "google.golang.org/grpc"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type WriteRecordsResponse struct {
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *WriteRecordsResponse) Reset()         { *m = WriteRecordsResponse{} }
func (m *WriteRecordsResponse) String() string { return proto.CompactTextString(m) }
func (*WriteRecordsResponse) ProtoMessage()    {}
func (*WriteRecordsResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_f1a937782ebbded5, []int{0}
}

func (m *WriteRecordsResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_WriteRecordsResponse.Unmarshal(m, b)
}
func (m *WriteRecordsResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_WriteRecordsResponse.Marshal(b, m, deterministic)
}
func (m *WriteRecordsResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_WriteRecordsResponse.Merge(m, src)
}
func (m *WriteRecordsResponse) XXX_Size() int {
	return xxx_messageInfo_WriteRecordsResponse.Size(m)
}
func (m *WriteRecordsResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_WriteRecordsResponse.DiscardUnknown(m)
}

var xxx_messageInfo_WriteRecordsResponse proto.InternalMessageInfo

type WriteInternalRecordsResponse struct {
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *WriteInternalRecordsResponse) Reset()         { *m = WriteInternalRecordsResponse{} }
func (m *WriteInternalRecordsResponse) String() string { return proto.CompactTextString(m) }
func (*WriteInternalRecordsResponse) ProtoMessage()    {}
func (*WriteInternalRecordsResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_f1a937782ebbded5, []int{1}
}

func (m *WriteInternalRecordsResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_WriteInternalRecordsResponse.Unmarshal(m, b)
}
func (m *WriteInternalRecordsResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_WriteInternalRecordsResponse.Marshal(b, m, deterministic)
}
func (m *WriteInternalRecordsResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_WriteInternalRecordsResponse.Merge(m, src)
}
func (m *WriteInternalRecordsResponse) XXX_Size() int {
	return xxx_messageInfo_WriteInternalRecordsResponse.Size(m)
}
func (m *WriteInternalRecordsResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_WriteInternalRecordsResponse.DiscardUnknown(m)
}

var xxx_messageInfo_WriteInternalRecordsResponse proto.InternalMessageInfo

func init() {
	proto.RegisterType((*WriteRecordsResponse)(nil), "proto.WriteRecordsResponse")
	proto.RegisterType((*WriteInternalRecordsResponse)(nil), "proto.WriteInternalRecordsResponse")
}

func init() { proto.RegisterFile("gateway.proto", fileDescriptor_f1a937782ebbded5) }

var fileDescriptor_f1a937782ebbded5 = []byte{
	// 182 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0xe2, 0x4d, 0x4f, 0x2c, 0x49,
	0x2d, 0x4f, 0xac, 0xd4, 0x2b, 0x28, 0xca, 0x2f, 0xc9, 0x17, 0x62, 0x05, 0x53, 0x52, 0x3c, 0xa9,
	0x79, 0xe9, 0x99, 0x79, 0xa9, 0x10, 0x41, 0x25, 0x31, 0x2e, 0x91, 0xf0, 0xa2, 0xcc, 0x92, 0xd4,
	0xa0, 0xd4, 0xe4, 0xfc, 0xa2, 0x94, 0xe2, 0xa0, 0xd4, 0xe2, 0x82, 0xfc, 0xbc, 0xe2, 0x54, 0x25,
	0x39, 0x2e, 0x19, 0xb0, 0xb8, 0x67, 0x5e, 0x49, 0x6a, 0x51, 0x5e, 0x62, 0x0e, 0x9a, 0xbc, 0xd1,
	0x76, 0x46, 0x2e, 0x76, 0x77, 0x88, 0xf1, 0x42, 0x9e, 0x5c, 0x3c, 0xc8, 0x66, 0x08, 0x49, 0x41,
	0xcc, 0xd6, 0x43, 0x35, 0xb8, 0xb0, 0x34, 0xb5, 0xb8, 0x44, 0x4a, 0x1a, 0xab, 0x1c, 0xd4, 0x52,
	0x06, 0xa1, 0x44, 0xa8, 0x73, 0xd0, 0xac, 0x15, 0x52, 0x42, 0xd6, 0x86, 0xe1, 0x26, 0x88, 0xd1,
	0xca, 0x78, 0xd5, 0xc0, 0xac, 0x70, 0x52, 0xe7, 0x12, 0xcd, 0x4b, 0x2d, 0x29, 0xcf, 0x2f, 0xca,
	0xd6, 0x4b, 0x4a, 0xcd, 0x4b, 0x4d, 0x2c, 0xc9, 0x80, 0xe8, 0x73, 0xe2, 0x71, 0x82, 0x70, 0x03,
	0x40, 0xbc, 0x00, 0xc6, 0x24, 0x36, 0xb0, 0xb0, 0x31, 0x20, 0x00, 0x00, 0xff, 0xff, 0xd3, 0x3c,
	0x69, 0x63, 0x47, 0x01, 0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// GatewayClient is the client API for Gateway service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type GatewayClient interface {
	WriteRecords(ctx context.Context, in *WriteRecordsRequest, opts ...grpc.CallOption) (*WriteRecordsResponse, error)
	WriteInternalRecords(ctx context.Context, in *WriteInternalRecordsRequest, opts ...grpc.CallOption) (*WriteInternalRecordsResponse, error)
}

type gatewayClient struct {
	cc *grpc.ClientConn
}

func NewGatewayClient(cc *grpc.ClientConn) GatewayClient {
	return &gatewayClient{cc}
}

func (c *gatewayClient) WriteRecords(ctx context.Context, in *WriteRecordsRequest, opts ...grpc.CallOption) (*WriteRecordsResponse, error) {
	out := new(WriteRecordsResponse)
	err := c.cc.Invoke(ctx, "/proto.Gateway/WriteRecords", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayClient) WriteInternalRecords(ctx context.Context, in *WriteInternalRecordsRequest, opts ...grpc.CallOption) (*WriteInternalRecordsResponse, error) {
	out := new(WriteInternalRecordsResponse)
	err := c.cc.Invoke(ctx, "/proto.Gateway/WriteInternalRecords", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// GatewayServer is the server API for Gateway service.
type GatewayServer interface {
	WriteRecords(context.Context, *WriteRecordsRequest) (*WriteRecordsResponse, error)
	WriteInternalRecords(context.Context, *WriteInternalRecordsRequest) (*WriteInternalRecordsResponse, error)
}

func RegisterGatewayServer(s *grpc.Server, srv GatewayServer) {
	s.RegisterService(&_Gateway_serviceDesc, srv)
}

func _Gateway_WriteRecords_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(WriteRecordsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServer).WriteRecords(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.Gateway/WriteRecords",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServer).WriteRecords(ctx, req.(*WriteRecordsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Gateway_WriteInternalRecords_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(WriteInternalRecordsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServer).WriteInternalRecords(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.Gateway/WriteInternalRecords",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServer).WriteInternalRecords(ctx, req.(*WriteInternalRecordsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _Gateway_serviceDesc = grpc.ServiceDesc{
	ServiceName: "proto.Gateway",
	HandlerType: (*GatewayServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "WriteRecords",
			Handler:    _Gateway_WriteRecords_Handler,
		},
		{
			MethodName: "WriteInternalRecords",
			Handler:    _Gateway_WriteInternalRecords_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "gateway.proto",
}
