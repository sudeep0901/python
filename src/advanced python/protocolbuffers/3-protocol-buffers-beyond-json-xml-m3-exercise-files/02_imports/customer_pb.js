/**
 * @fileoverview
 * @enhanceable
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

var jspb = require('google-protobuf');
var goog = jspb;
var global = Function('return this')();

var address_pb = require('./address_pb.js');
goog.exportSymbol('proto.Customer', null, global);
goog.exportSymbol('proto.CustomerType', null, global);

/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.Customer = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.Customer.repeatedFields_, null);
};
goog.inherits(proto.Customer, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.Customer.displayName = 'proto.Customer';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.Customer.repeatedFields_ = [2];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.Customer.prototype.toObject = function(opt_includeInstance) {
  return proto.Customer.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.Customer} msg The msg instance to transform.
 * @return {!Object}
 */
proto.Customer.toObject = function(includeInstance, msg) {
  var f, obj = {
    username: msg.getUsername(),
    emailAddressesList: jspb.Message.getField(msg, 2),
    type: msg.getType(),
    address: (f = msg.getAddress()) && address_pb.Address.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.Customer}
 */
proto.Customer.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.Customer;
  return proto.Customer.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.Customer} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.Customer}
 */
proto.Customer.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setUsername(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.getEmailAddressesList().push(value);
      msg.setEmailAddressesList(msg.getEmailAddressesList());
      break;
    case 3:
      var value = /** @type {!proto.CustomerType} */ (reader.readEnum());
      msg.setType(value);
      break;
    case 4:
      var value = new address_pb.Address;
      reader.readMessage(value,address_pb.Address.deserializeBinaryFromReader);
      msg.setAddress(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Class method variant: serializes the given message to binary data
 * (in protobuf wire format), writing to the given BinaryWriter.
 * @param {!proto.Customer} message
 * @param {!jspb.BinaryWriter} writer
 */
proto.Customer.serializeBinaryToWriter = function(message, writer) {
  message.serializeBinaryToWriter(writer);
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.Customer.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  this.serializeBinaryToWriter(writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the message to binary data (in protobuf wire format),
 * writing to the given BinaryWriter.
 * @param {!jspb.BinaryWriter} writer
 */
proto.Customer.prototype.serializeBinaryToWriter = function (writer) {
  var f = undefined;
  f = this.getUsername();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = this.getEmailAddressesList();
  if (f.length > 0) {
    writer.writeRepeatedString(
      2,
      f
    );
  }
  f = this.getType();
  if (f !== 0.0) {
    writer.writeEnum(
      3,
      f
    );
  }
  f = this.getAddress();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      address_pb.Address.serializeBinaryToWriter
    );
  }
};


/**
 * Creates a deep clone of this proto. No data is shared with the original.
 * @return {!proto.Customer} The clone.
 */
proto.Customer.prototype.cloneMessage = function() {
  return /** @type {!proto.Customer} */ (jspb.Message.cloneMessage(this));
};


/**
 * optional string username = 1;
 * @return {string}
 */
proto.Customer.prototype.getUsername = function() {
  return /** @type {string} */ (jspb.Message.getFieldProto3(this, 1, ""));
};


/** @param {string} value  */
proto.Customer.prototype.setUsername = function(value) {
  jspb.Message.setField(this, 1, value);
};


/**
 * repeated string email_addresses = 2;
 * If you change this array by adding, removing or replacing elements, or if you
 * replace the array itself, then you must call the setter to update it.
 * @return {!Array.<string>}
 */
proto.Customer.prototype.getEmailAddressesList = function() {
  return /** @type {!Array.<string>} */ (jspb.Message.getField(this, 2));
};


/** @param {Array.<string>} value  */
proto.Customer.prototype.setEmailAddressesList = function(value) {
  jspb.Message.setField(this, 2, value || []);
};


/**
 * optional CustomerType type = 3;
 * @return {!proto.CustomerType}
 */
proto.Customer.prototype.getType = function() {
  return /** @type {!proto.CustomerType} */ (jspb.Message.getFieldProto3(this, 3, 0));
};


/** @param {!proto.CustomerType} value  */
proto.Customer.prototype.setType = function(value) {
  jspb.Message.setField(this, 3, value);
};


/**
 * optional Address address = 4;
 * @return {proto.Address}
 */
proto.Customer.prototype.getAddress = function() {
  return /** @type{proto.Address} */ (
    jspb.Message.getWrapperField(this, address_pb.Address, 4));
};


/** @param {proto.Address|undefined} value  */
proto.Customer.prototype.setAddress = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.Customer.prototype.clearAddress = function() {
  this.setAddress(undefined);
};


/**
 * @enum {number}
 */
proto.CustomerType = {
  REGULAR: 0,
  MEMBER: 1,
  SPONSOR: 2
};

goog.object.extend(exports, proto);
