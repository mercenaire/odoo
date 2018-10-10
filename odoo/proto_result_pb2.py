# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto_result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import odoo.proto_oms_pb2 as proto__oms__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto_result.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x12proto_result.proto\x1a\x0fproto_oms.proto\"O\n\x12RequestCreateOrder\x12\x0f\n\x07is_done\x18\x05 \x01(\x08\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x14\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x06.Order\"K\n\x1fRequestOrderDetailByOrderNumber\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x14\n\x0corder_number\x18\x02 \x01(\t\"V\n\x0cRequestOrder\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\x12\x0c\n\x04note\x18\x04 \x01(\t\x12\x14\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x06.Order\"d\n\x13RequestPaymentOrder\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\x12\x0c\n\x04note\x18\x04 \x01(\t\x12\x1b\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\r.PaymentOrder\"f\n\x14RequestShipmentOrder\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\x12\x0c\n\x04note\x18\x04 \x01(\t\x12\x1c\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x0e.ShipmentOrder\"t\n\x1bRequestShipmentOrderPackage\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\x12\x0c\n\x04note\x18\x04 \x01(\t\x12#\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x15.ShipmentOrderPackage\"X\n\x18RequestCommitUpdateOrder\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x13\n\x03old\x18\x02 \x01(\x0b\x32\x06.Order\x12\x13\n\x03new\x18\x03 \x01(\x0b\x32\x06.Order\"m\n\x1fRequestCommitUpdatePaymentOrder\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x1a\n\x03old\x18\x02 \x01(\x0b\x32\r.PaymentOrder\x12\x1a\n\x03new\x18\x03 \x01(\x0b\x32\r.PaymentOrder\"p\n RequestCommitUpdateShipmentOrder\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x1b\n\x03old\x18\x02 \x01(\x0b\x32\x0e.ShipmentOrder\x12\x1b\n\x03new\x18\x03 \x01(\x0b\x32\x0e.ShipmentOrder\"\x85\x01\n\'RequestCommitUpdateShipmentOrderPackage\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\"\n\x03old\x18\x02 \x01(\x0b\x32\x15.ShipmentOrderPackage\x12\"\n\x03new\x18\x03 \x01(\x0b\x32\x15.ShipmentOrderPackage\"K\n\x19RequestUpdateOrderPayment\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x1a\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x0c.PaymentData\"M\n\x1aRequestUpdateOrderShipment\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x1b\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\r.ShipmentData\"f\n\x14RequestOrderLineItem\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\x12\x0c\n\x04note\x18\x04 \x01(\t\x12\x1c\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x0e.OrderLineItem\"B\n\x11RequestSettlement\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x19\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x0b.SettlementB%\n\x1a\x63om.mapan.boronjai.requestB\x07Requestb\x06proto3')
  ,
  dependencies=[proto__oms__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQUESTCREATEORDER = _descriptor.Descriptor(
  name='RequestCreateOrder',
  full_name='RequestCreateOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_done', full_name='RequestCreateOrder.is_done', index=0,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='RequestCreateOrder.request_id', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='RequestCreateOrder.data', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=118,
)


_REQUESTORDERDETAILBYORDERNUMBER = _descriptor.Descriptor(
  name='RequestOrderDetailByOrderNumber',
  full_name='RequestOrderDetailByOrderNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='RequestOrderDetailByOrderNumber.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_number', full_name='RequestOrderDetailByOrderNumber.order_number', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=195,
)


_REQUESTORDER = _descriptor.Descriptor(
  name='RequestOrder',
  full_name='RequestOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='RequestOrder.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='RequestOrder.status', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='note', full_name='RequestOrder.note', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='RequestOrder.data', index=3,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=283,
)


_REQUESTPAYMENTORDER = _descriptor.Descriptor(
  name='RequestPaymentOrder',
  full_name='RequestPaymentOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='RequestPaymentOrder.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='RequestPaymentOrder.status', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='note', full_name='RequestPaymentOrder.note', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='RequestPaymentOrder.data', index=3,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=285,
  serialized_end=385,
)


_REQUESTSHIPMENTORDER = _descriptor.Descriptor(
  name='RequestShipmentOrder',
  full_name='RequestShipmentOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='RequestShipmentOrder.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='RequestShipmentOrder.status', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='note', full_name='RequestShipmentOrder.note', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='RequestShipmentOrder.data', index=3,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=387,
  serialized_end=489,
)


_REQUESTSHIPMENTORDERPACKAGE = _descriptor.Descriptor(
  name='RequestShipmentOrderPackage',
  full_name='RequestShipmentOrderPackage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='RequestShipmentOrderPackage.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='RequestShipmentOrderPackage.status', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='note', full_name='RequestShipmentOrderPackage.note', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='RequestShipmentOrderPackage.data', index=3,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=491,
  serialized_end=607,
)


_REQUESTCOMMITUPDATEORDER = _descriptor.Descriptor(
  name='RequestCommitUpdateOrder',
  full_name='RequestCommitUpdateOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='RequestCommitUpdateOrder.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='old', full_name='RequestCommitUpdateOrder.old', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new', full_name='RequestCommitUpdateOrder.new', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=609,
  serialized_end=697,
)


_REQUESTCOMMITUPDATEPAYMENTORDER = _descriptor.Descriptor(
  name='RequestCommitUpdatePaymentOrder',
  full_name='RequestCommitUpdatePaymentOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='RequestCommitUpdatePaymentOrder.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='old', full_name='RequestCommitUpdatePaymentOrder.old', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new', full_name='RequestCommitUpdatePaymentOrder.new', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=699,
  serialized_end=808,
)


_REQUESTCOMMITUPDATESHIPMENTORDER = _descriptor.Descriptor(
  name='RequestCommitUpdateShipmentOrder',
  full_name='RequestCommitUpdateShipmentOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='RequestCommitUpdateShipmentOrder.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='old', full_name='RequestCommitUpdateShipmentOrder.old', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new', full_name='RequestCommitUpdateShipmentOrder.new', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=810,
  serialized_end=922,
)


_REQUESTCOMMITUPDATESHIPMENTORDERPACKAGE = _descriptor.Descriptor(
  name='RequestCommitUpdateShipmentOrderPackage',
  full_name='RequestCommitUpdateShipmentOrderPackage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='RequestCommitUpdateShipmentOrderPackage.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='old', full_name='RequestCommitUpdateShipmentOrderPackage.old', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new', full_name='RequestCommitUpdateShipmentOrderPackage.new', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=925,
  serialized_end=1058,
)


_REQUESTUPDATEORDERPAYMENT = _descriptor.Descriptor(
  name='RequestUpdateOrderPayment',
  full_name='RequestUpdateOrderPayment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='RequestUpdateOrderPayment.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='RequestUpdateOrderPayment.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1060,
  serialized_end=1135,
)


_REQUESTUPDATEORDERSHIPMENT = _descriptor.Descriptor(
  name='RequestUpdateOrderShipment',
  full_name='RequestUpdateOrderShipment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='RequestUpdateOrderShipment.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='RequestUpdateOrderShipment.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1137,
  serialized_end=1214,
)


_REQUESTORDERLINEITEM = _descriptor.Descriptor(
  name='RequestOrderLineItem',
  full_name='RequestOrderLineItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='RequestOrderLineItem.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='RequestOrderLineItem.status', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='note', full_name='RequestOrderLineItem.note', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='RequestOrderLineItem.data', index=3,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1216,
  serialized_end=1318,
)


_REQUESTSETTLEMENT = _descriptor.Descriptor(
  name='RequestSettlement',
  full_name='RequestSettlement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='RequestSettlement.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='RequestSettlement.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1320,
  serialized_end=1386,
)

_REQUESTCREATEORDER.fields_by_name['data'].message_type = proto__oms__pb2._ORDER
_REQUESTORDER.fields_by_name['data'].message_type = proto__oms__pb2._ORDER
_REQUESTPAYMENTORDER.fields_by_name['data'].message_type = proto__oms__pb2._PAYMENTORDER
_REQUESTSHIPMENTORDER.fields_by_name['data'].message_type = proto__oms__pb2._SHIPMENTORDER
_REQUESTSHIPMENTORDERPACKAGE.fields_by_name['data'].message_type = proto__oms__pb2._SHIPMENTORDERPACKAGE
_REQUESTCOMMITUPDATEORDER.fields_by_name['old'].message_type = proto__oms__pb2._ORDER
_REQUESTCOMMITUPDATEORDER.fields_by_name['new'].message_type = proto__oms__pb2._ORDER
_REQUESTCOMMITUPDATEPAYMENTORDER.fields_by_name['old'].message_type = proto__oms__pb2._PAYMENTORDER
_REQUESTCOMMITUPDATEPAYMENTORDER.fields_by_name['new'].message_type = proto__oms__pb2._PAYMENTORDER
_REQUESTCOMMITUPDATESHIPMENTORDER.fields_by_name['old'].message_type = proto__oms__pb2._SHIPMENTORDER
_REQUESTCOMMITUPDATESHIPMENTORDER.fields_by_name['new'].message_type = proto__oms__pb2._SHIPMENTORDER
_REQUESTCOMMITUPDATESHIPMENTORDERPACKAGE.fields_by_name['old'].message_type = proto__oms__pb2._SHIPMENTORDERPACKAGE
_REQUESTCOMMITUPDATESHIPMENTORDERPACKAGE.fields_by_name['new'].message_type = proto__oms__pb2._SHIPMENTORDERPACKAGE
_REQUESTUPDATEORDERPAYMENT.fields_by_name['data'].message_type = proto__oms__pb2._PAYMENTDATA
_REQUESTUPDATEORDERSHIPMENT.fields_by_name['data'].message_type = proto__oms__pb2._SHIPMENTDATA
_REQUESTORDERLINEITEM.fields_by_name['data'].message_type = proto__oms__pb2._ORDERLINEITEM
_REQUESTSETTLEMENT.fields_by_name['data'].message_type = proto__oms__pb2._SETTLEMENT
DESCRIPTOR.message_types_by_name['RequestCreateOrder'] = _REQUESTCREATEORDER
DESCRIPTOR.message_types_by_name['RequestOrderDetailByOrderNumber'] = _REQUESTORDERDETAILBYORDERNUMBER
DESCRIPTOR.message_types_by_name['RequestOrder'] = _REQUESTORDER
DESCRIPTOR.message_types_by_name['RequestPaymentOrder'] = _REQUESTPAYMENTORDER
DESCRIPTOR.message_types_by_name['RequestShipmentOrder'] = _REQUESTSHIPMENTORDER
DESCRIPTOR.message_types_by_name['RequestShipmentOrderPackage'] = _REQUESTSHIPMENTORDERPACKAGE
DESCRIPTOR.message_types_by_name['RequestCommitUpdateOrder'] = _REQUESTCOMMITUPDATEORDER
DESCRIPTOR.message_types_by_name['RequestCommitUpdatePaymentOrder'] = _REQUESTCOMMITUPDATEPAYMENTORDER
DESCRIPTOR.message_types_by_name['RequestCommitUpdateShipmentOrder'] = _REQUESTCOMMITUPDATESHIPMENTORDER
DESCRIPTOR.message_types_by_name['RequestCommitUpdateShipmentOrderPackage'] = _REQUESTCOMMITUPDATESHIPMENTORDERPACKAGE
DESCRIPTOR.message_types_by_name['RequestUpdateOrderPayment'] = _REQUESTUPDATEORDERPAYMENT
DESCRIPTOR.message_types_by_name['RequestUpdateOrderShipment'] = _REQUESTUPDATEORDERSHIPMENT
DESCRIPTOR.message_types_by_name['RequestOrderLineItem'] = _REQUESTORDERLINEITEM
DESCRIPTOR.message_types_by_name['RequestSettlement'] = _REQUESTSETTLEMENT

RequestCreateOrder = _reflection.GeneratedProtocolMessageType('RequestCreateOrder', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTCREATEORDER,
  __module__ = 'proto_result_pb2'
  # @@protoc_insertion_point(class_scope:RequestCreateOrder)
  ))
_sym_db.RegisterMessage(RequestCreateOrder)

RequestOrderDetailByOrderNumber = _reflection.GeneratedProtocolMessageType('RequestOrderDetailByOrderNumber', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTORDERDETAILBYORDERNUMBER,
  __module__ = 'proto_result_pb2'
  # @@protoc_insertion_point(class_scope:RequestOrderDetailByOrderNumber)
  ))
_sym_db.RegisterMessage(RequestOrderDetailByOrderNumber)

RequestOrder = _reflection.GeneratedProtocolMessageType('RequestOrder', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTORDER,
  __module__ = 'proto_result_pb2'
  # @@protoc_insertion_point(class_scope:RequestOrder)
  ))
_sym_db.RegisterMessage(RequestOrder)

RequestPaymentOrder = _reflection.GeneratedProtocolMessageType('RequestPaymentOrder', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTPAYMENTORDER,
  __module__ = 'proto_result_pb2'
  # @@protoc_insertion_point(class_scope:RequestPaymentOrder)
  ))
_sym_db.RegisterMessage(RequestPaymentOrder)

RequestShipmentOrder = _reflection.GeneratedProtocolMessageType('RequestShipmentOrder', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTSHIPMENTORDER,
  __module__ = 'proto_result_pb2'
  # @@protoc_insertion_point(class_scope:RequestShipmentOrder)
  ))
_sym_db.RegisterMessage(RequestShipmentOrder)

RequestShipmentOrderPackage = _reflection.GeneratedProtocolMessageType('RequestShipmentOrderPackage', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTSHIPMENTORDERPACKAGE,
  __module__ = 'proto_result_pb2'
  # @@protoc_insertion_point(class_scope:RequestShipmentOrderPackage)
  ))
_sym_db.RegisterMessage(RequestShipmentOrderPackage)

RequestCommitUpdateOrder = _reflection.GeneratedProtocolMessageType('RequestCommitUpdateOrder', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTCOMMITUPDATEORDER,
  __module__ = 'proto_result_pb2'
  # @@protoc_insertion_point(class_scope:RequestCommitUpdateOrder)
  ))
_sym_db.RegisterMessage(RequestCommitUpdateOrder)

RequestCommitUpdatePaymentOrder = _reflection.GeneratedProtocolMessageType('RequestCommitUpdatePaymentOrder', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTCOMMITUPDATEPAYMENTORDER,
  __module__ = 'proto_result_pb2'
  # @@protoc_insertion_point(class_scope:RequestCommitUpdatePaymentOrder)
  ))
_sym_db.RegisterMessage(RequestCommitUpdatePaymentOrder)

RequestCommitUpdateShipmentOrder = _reflection.GeneratedProtocolMessageType('RequestCommitUpdateShipmentOrder', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTCOMMITUPDATESHIPMENTORDER,
  __module__ = 'proto_result_pb2'
  # @@protoc_insertion_point(class_scope:RequestCommitUpdateShipmentOrder)
  ))
_sym_db.RegisterMessage(RequestCommitUpdateShipmentOrder)

RequestCommitUpdateShipmentOrderPackage = _reflection.GeneratedProtocolMessageType('RequestCommitUpdateShipmentOrderPackage', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTCOMMITUPDATESHIPMENTORDERPACKAGE,
  __module__ = 'proto_result_pb2'
  # @@protoc_insertion_point(class_scope:RequestCommitUpdateShipmentOrderPackage)
  ))
_sym_db.RegisterMessage(RequestCommitUpdateShipmentOrderPackage)

RequestUpdateOrderPayment = _reflection.GeneratedProtocolMessageType('RequestUpdateOrderPayment', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTUPDATEORDERPAYMENT,
  __module__ = 'proto_result_pb2'
  # @@protoc_insertion_point(class_scope:RequestUpdateOrderPayment)
  ))
_sym_db.RegisterMessage(RequestUpdateOrderPayment)

RequestUpdateOrderShipment = _reflection.GeneratedProtocolMessageType('RequestUpdateOrderShipment', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTUPDATEORDERSHIPMENT,
  __module__ = 'proto_result_pb2'
  # @@protoc_insertion_point(class_scope:RequestUpdateOrderShipment)
  ))
_sym_db.RegisterMessage(RequestUpdateOrderShipment)

RequestOrderLineItem = _reflection.GeneratedProtocolMessageType('RequestOrderLineItem', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTORDERLINEITEM,
  __module__ = 'proto_result_pb2'
  # @@protoc_insertion_point(class_scope:RequestOrderLineItem)
  ))
_sym_db.RegisterMessage(RequestOrderLineItem)

RequestSettlement = _reflection.GeneratedProtocolMessageType('RequestSettlement', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTSETTLEMENT,
  __module__ = 'proto_result_pb2'
  # @@protoc_insertion_point(class_scope:RequestSettlement)
  ))
_sym_db.RegisterMessage(RequestSettlement)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032com.mapan.boronjai.requestB\007Request'))
# @@protoc_insertion_point(module_scope)
