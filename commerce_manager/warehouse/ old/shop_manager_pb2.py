# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shop_manager.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12shop_manager.proto\x12\x07shop.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0c\x63ommon.proto\"\x80\x01\n\rBuyingRequest\x12\x16\n\x0ewarehouse_name\x18\x01 \x01(\t\x12\x0f\n\x07good_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x02\x12\x16\n\x0egoods_quantity\x18\x05 \x01(\x05\x12\x11\n\ttotal_sum\x18\x06 \x01(\x02\"\x80\x01\n\rReturnRequest\x12\x16\n\x0ewarehouse_name\x18\x01 \x01(\t\x12\x0f\n\x07good_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x02\x12\x16\n\x0egoods_quantity\x18\x05 \x01(\x05\x12\x11\n\ttotal_sum\x18\x06 \x01(\x02\x32w\n\x12ShopManagerService\x12.\n\x07\x42uyGood\x12\x16.shop.v1.BuyingRequest\x1a\t.Response\"\x00\x12\x31\n\nReturnGood\x12\x16.shop.v1.ReturnRequest\x1a\t.Response\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'shop_manager_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BUYINGREQUEST._serialized_start=79
  _BUYINGREQUEST._serialized_end=207
  _RETURNREQUEST._serialized_start=210
  _RETURNREQUEST._serialized_end=338
  _SHOPMANAGERSERVICE._serialized_start=340
  _SHOPMANAGERSERVICE._serialized_end=459
# @@protoc_insertion_point(module_scope)
