// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: customer.proto

#ifndef PROTOBUF_customer_2eproto__INCLUDED
#define PROTOBUF_customer_2eproto__INCLUDED

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 3000000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 3000000 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)

// Internal implementation detail -- do not call these.
void protobuf_AddDesc_customer_2eproto();
void protobuf_AssignDesc_customer_2eproto();
void protobuf_ShutdownFile_customer_2eproto();

class Customer;

// ===================================================================

class Customer : public ::google::protobuf::Message {
 public:
  Customer();
  virtual ~Customer();

  Customer(const Customer& from);

  inline Customer& operator=(const Customer& from) {
    CopyFrom(from);
    return *this;
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const Customer& default_instance();

  void Swap(Customer* other);

  // implements Message ----------------------------------------------

  inline Customer* New() const { return New(NULL); }

  Customer* New(::google::protobuf::Arena* arena) const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const Customer& from);
  void MergeFrom(const Customer& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const;
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  void InternalSwap(Customer* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return _internal_metadata_.arena();
  }
  inline void* MaybeArenaPtr() const {
    return _internal_metadata_.raw_arena_ptr();
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // optional int32 id = 1;
  void clear_id();
  static const int kIdFieldNumber = 1;
  ::google::protobuf::int32 id() const;
  void set_id(::google::protobuf::int32 value);

  // optional string username = 2;
  void clear_username();
  static const int kUsernameFieldNumber = 2;
  const ::std::string& username() const;
  void set_username(const ::std::string& value);
  void set_username(const char* value);
  void set_username(const char* value, size_t size);
  ::std::string* mutable_username();
  ::std::string* release_username();
  void set_allocated_username(::std::string* username);

  // optional string first_name = 3;
  void clear_first_name();
  static const int kFirstNameFieldNumber = 3;
  const ::std::string& first_name() const;
  void set_first_name(const ::std::string& value);
  void set_first_name(const char* value);
  void set_first_name(const char* value, size_t size);
  ::std::string* mutable_first_name();
  ::std::string* release_first_name();
  void set_allocated_first_name(::std::string* first_name);

  // optional string last_name = 4;
  void clear_last_name();
  static const int kLastNameFieldNumber = 4;
  const ::std::string& last_name() const;
  void set_last_name(const ::std::string& value);
  void set_last_name(const char* value);
  void set_last_name(const char* value, size_t size);
  ::std::string* mutable_last_name();
  ::std::string* release_last_name();
  void set_allocated_last_name(::std::string* last_name);

  // @@protoc_insertion_point(class_scope:Customer)
 private:

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  bool _is_default_instance_;
  ::google::protobuf::internal::ArenaStringPtr username_;
  ::google::protobuf::internal::ArenaStringPtr first_name_;
  ::google::protobuf::internal::ArenaStringPtr last_name_;
  ::google::protobuf::int32 id_;
  mutable int _cached_size_;
  friend void  protobuf_AddDesc_customer_2eproto();
  friend void protobuf_AssignDesc_customer_2eproto();
  friend void protobuf_ShutdownFile_customer_2eproto();

  void InitAsDefaultInstance();
  static Customer* default_instance_;
};
// ===================================================================


// ===================================================================

#if !PROTOBUF_INLINE_NOT_IN_HEADERS
// Customer

// optional int32 id = 1;
inline void Customer::clear_id() {
  id_ = 0;
}
inline ::google::protobuf::int32 Customer::id() const {
  // @@protoc_insertion_point(field_get:Customer.id)
  return id_;
}
inline void Customer::set_id(::google::protobuf::int32 value) {
  
  id_ = value;
  // @@protoc_insertion_point(field_set:Customer.id)
}

// optional string username = 2;
inline void Customer::clear_username() {
  username_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline const ::std::string& Customer::username() const {
  // @@protoc_insertion_point(field_get:Customer.username)
  return username_.GetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void Customer::set_username(const ::std::string& value) {
  
  username_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:Customer.username)
}
inline void Customer::set_username(const char* value) {
  
  username_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:Customer.username)
}
inline void Customer::set_username(const char* value, size_t size) {
  
  username_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:Customer.username)
}
inline ::std::string* Customer::mutable_username() {
  
  // @@protoc_insertion_point(field_mutable:Customer.username)
  return username_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline ::std::string* Customer::release_username() {
  // @@protoc_insertion_point(field_release:Customer.username)
  
  return username_.ReleaseNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void Customer::set_allocated_username(::std::string* username) {
  if (username != NULL) {
    
  } else {
    
  }
  username_.SetAllocatedNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), username);
  // @@protoc_insertion_point(field_set_allocated:Customer.username)
}

// optional string first_name = 3;
inline void Customer::clear_first_name() {
  first_name_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline const ::std::string& Customer::first_name() const {
  // @@protoc_insertion_point(field_get:Customer.first_name)
  return first_name_.GetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void Customer::set_first_name(const ::std::string& value) {
  
  first_name_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:Customer.first_name)
}
inline void Customer::set_first_name(const char* value) {
  
  first_name_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:Customer.first_name)
}
inline void Customer::set_first_name(const char* value, size_t size) {
  
  first_name_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:Customer.first_name)
}
inline ::std::string* Customer::mutable_first_name() {
  
  // @@protoc_insertion_point(field_mutable:Customer.first_name)
  return first_name_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline ::std::string* Customer::release_first_name() {
  // @@protoc_insertion_point(field_release:Customer.first_name)
  
  return first_name_.ReleaseNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void Customer::set_allocated_first_name(::std::string* first_name) {
  if (first_name != NULL) {
    
  } else {
    
  }
  first_name_.SetAllocatedNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), first_name);
  // @@protoc_insertion_point(field_set_allocated:Customer.first_name)
}

// optional string last_name = 4;
inline void Customer::clear_last_name() {
  last_name_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline const ::std::string& Customer::last_name() const {
  // @@protoc_insertion_point(field_get:Customer.last_name)
  return last_name_.GetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void Customer::set_last_name(const ::std::string& value) {
  
  last_name_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:Customer.last_name)
}
inline void Customer::set_last_name(const char* value) {
  
  last_name_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:Customer.last_name)
}
inline void Customer::set_last_name(const char* value, size_t size) {
  
  last_name_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:Customer.last_name)
}
inline ::std::string* Customer::mutable_last_name() {
  
  // @@protoc_insertion_point(field_mutable:Customer.last_name)
  return last_name_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline ::std::string* Customer::release_last_name() {
  // @@protoc_insertion_point(field_release:Customer.last_name)
  
  return last_name_.ReleaseNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void Customer::set_allocated_last_name(::std::string* last_name) {
  if (last_name != NULL) {
    
  } else {
    
  }
  last_name_.SetAllocatedNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), last_name);
  // @@protoc_insertion_point(field_set_allocated:Customer.last_name)
}

#endif  // !PROTOBUF_INLINE_NOT_IN_HEADERS

// @@protoc_insertion_point(namespace_scope)

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_customer_2eproto__INCLUDED
