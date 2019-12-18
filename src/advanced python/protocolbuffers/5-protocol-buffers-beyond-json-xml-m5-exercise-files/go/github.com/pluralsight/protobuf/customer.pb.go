// Code generated by protoc-gen-go.
// source: customer.proto
// DO NOT EDIT!

/*
Package protobuf is a generated protocol buffer package.

It is generated from these files:
	customer.proto

It has these top-level messages:
	Customer
*/
package protobuf

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

type Customer struct {
	Id        int32  `protobuf:"varint,1,opt,name=id" json:"id,omitempty"`
	Username  string `protobuf:"bytes,2,opt,name=username" json:"username,omitempty"`
	FirstName string `protobuf:"bytes,3,opt,name=first_name,json=firstName" json:"first_name,omitempty"`
	LastName  string `protobuf:"bytes,4,opt,name=last_name,json=lastName" json:"last_name,omitempty"`
}

func (m *Customer) Reset()                    { *m = Customer{} }
func (m *Customer) String() string            { return proto.CompactTextString(m) }
func (*Customer) ProtoMessage()               {}
func (*Customer) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{0} }

func init() {
	proto.RegisterType((*Customer)(nil), "Customer")
}

func init() { proto.RegisterFile("customer.proto", fileDescriptor0) }

var fileDescriptor0 = []byte{
	// 152 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x09, 0x6e, 0x88, 0x02, 0xff, 0xe2, 0xe2, 0x4b, 0x2e, 0x2d, 0x2e,
	0xc9, 0xcf, 0x4d, 0x2d, 0xd2, 0x2b, 0x28, 0xca, 0x2f, 0xc9, 0x57, 0x2a, 0xe2, 0xe2, 0x70, 0x86,
	0x8a, 0x08, 0xf1, 0x71, 0x31, 0x65, 0xa6, 0x48, 0x30, 0x2a, 0x30, 0x6a, 0xb0, 0x06, 0x01, 0x59,
	0x42, 0x52, 0x5c, 0x1c, 0xa5, 0xc5, 0xa9, 0x45, 0x79, 0x89, 0xb9, 0xa9, 0x12, 0x4c, 0x40, 0x51,
	0xce, 0x20, 0x38, 0x5f, 0x48, 0x96, 0x8b, 0x2b, 0x2d, 0xb3, 0xa8, 0xb8, 0x24, 0x1e, 0x2c, 0xcb,
	0x0c, 0x96, 0xe5, 0x04, 0x8b, 0xf8, 0x81, 0xa4, 0xa5, 0xb9, 0x38, 0x73, 0x12, 0x61, 0xb2, 0x2c,
	0x10, 0xbd, 0x20, 0x01, 0x90, 0xa4, 0x93, 0x62, 0x94, 0x7c, 0x7a, 0x66, 0x49, 0x46, 0x69, 0x92,
	0x5e, 0x72, 0x7e, 0xae, 0x7e, 0x41, 0x4e, 0x69, 0x51, 0x62, 0x4e, 0x71, 0x66, 0x7a, 0x46, 0x89,
	0x3e, 0xd8, 0x4d, 0x49, 0xa5, 0x69, 0x49, 0x6c, 0x60, 0x96, 0x31, 0x20, 0x00, 0x00, 0xff, 0xff,
	0x32, 0x62, 0xc4, 0x6e, 0xaf, 0x00, 0x00, 0x00,
}
