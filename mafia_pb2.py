# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mafia.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmafia.proto\x12\x05mafia\"\x1f\n\x0fGetRoleResponse\x12\x0c\n\x04role\x18\x01 \x01(\t\"@\n\x11\x43ityVotingRequest\x12\x0f\n\x07game_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04vote\x18\x03 \x01(\t\"?\n\x12\x43ityVotingResponse\x12\x0e\n\x06is_end\x18\x01 \x01(\x08\x12\x0b\n\x03\x65nd\x18\x02 \x01(\t\x12\x0c\n\x04\x63ity\x18\x03 \x03(\t\"3\n\x12KillCitizenRequest\x12\x0f\n\x07game_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"4\n\x13\x43heckCitizenRequest\x12\x0f\n\x07game_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"&\n\x14\x43heckCitizenResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\"6\n\x15GetNightResultRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07game_id\x18\x02 \x01(\t\"C\n\x16GetNightResultResponse\x12\x0e\n\x06is_end\x18\x01 \x01(\x08\x12\x0b\n\x03\x65nd\x18\x02 \x01(\t\x12\x0c\n\x04\x63ity\x18\x03 \x03(\t\"\'\n\x06SingUp\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07game_id\x18\x02 \x01(\t\"2\n\x0eSingUpResponse\x12\x0f\n\x07game_id\x18\x01 \x01(\t\x12\x0f\n\x07players\x18\x02 \x03(\t\"1\n\x10SubscribeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07game_id\x18\x02 \x01(\t\" \n\x11SubscribeResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2\xe2\x04\n\x05Mafia\x12\x32\n\x08GoSingUp\x12\r.mafia.SingUp\x1a\x15.mafia.SingUpResponse\"\x00\x12Q\n\x18SubscribeToNotifications\x12\x17.mafia.SubscribeRequest\x1a\x18.mafia.SubscribeResponse\"\x00\x30\x01\x12.\n\rDisconectRoom\x12\r.mafia.SingUp\x1a\x0c.mafia.Empty\"\x00\x12\x35\n\x0b\x43onnectRoom\x12\r.mafia.SingUp\x1a\x15.mafia.SingUpResponse\"\x00\x12+\n\nDeadSignal\x12\r.mafia.SingUp\x1a\x0c.mafia.Empty\"\x00\x12\x43\n\nCityVoting\x12\x18.mafia.CityVotingRequest\x1a\x19.mafia.CityVotingResponse\"\x00\x12\x38\n\x0bKillCitizen\x12\x19.mafia.KillCitizenRequest\x1a\x0c.mafia.Empty\"\x00\x12:\n\x0c\x43heckCitizen\x12\x1a.mafia.CheckCitizenRequest\x1a\x0c.mafia.Empty\"\x00\x12O\n\x0eGetNightResult\x12\x1c.mafia.GetNightResultRequest\x1a\x1d.mafia.GetNightResultResponse\"\x00\x12\x32\n\x07GetRole\x12\r.mafia.SingUp\x1a\x16.mafia.GetRoleResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mafia_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETROLERESPONSE._serialized_start=22
  _GETROLERESPONSE._serialized_end=53
  _CITYVOTINGREQUEST._serialized_start=55
  _CITYVOTINGREQUEST._serialized_end=119
  _CITYVOTINGRESPONSE._serialized_start=121
  _CITYVOTINGRESPONSE._serialized_end=184
  _KILLCITIZENREQUEST._serialized_start=186
  _KILLCITIZENREQUEST._serialized_end=237
  _CHECKCITIZENREQUEST._serialized_start=239
  _CHECKCITIZENREQUEST._serialized_end=291
  _CHECKCITIZENRESPONSE._serialized_start=293
  _CHECKCITIZENRESPONSE._serialized_end=331
  _GETNIGHTRESULTREQUEST._serialized_start=333
  _GETNIGHTRESULTREQUEST._serialized_end=387
  _GETNIGHTRESULTRESPONSE._serialized_start=389
  _GETNIGHTRESULTRESPONSE._serialized_end=456
  _SINGUP._serialized_start=458
  _SINGUP._serialized_end=497
  _SINGUPRESPONSE._serialized_start=499
  _SINGUPRESPONSE._serialized_end=549
  _SUBSCRIBEREQUEST._serialized_start=551
  _SUBSCRIBEREQUEST._serialized_end=600
  _SUBSCRIBERESPONSE._serialized_start=602
  _SUBSCRIBERESPONSE._serialized_end=634
  _EMPTY._serialized_start=636
  _EMPTY._serialized_end=643
  _MAFIA._serialized_start=646
  _MAFIA._serialized_end=1256
# @@protoc_insertion_point(module_scope)