#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.net.proto import ProtocolBuffer
import array
import dummy_thread as thread

__pychecker__ = """maxreturns=0 maxbranches=0 no-callinit
                   unusednames=printElemNumber,debug_strs no-special"""

from google.net.proto.RawMessage import RawMessage
from google.appengine.datastore.datastore_pb import PutRequest
from google.appengine.datastore.datastore_pb import DeleteRequest
from google.appengine.datastore.entity_pb import Reference
class Request(ProtocolBuffer.ProtocolMessage):
  has_service_name_ = 0
  service_name_ = ""
  has_method_ = 0
  method_ = ""
  has_request_ = 0

  def __init__(self, contents=None):
    self.request_ = RawMessage()
    if contents is not None: self.MergeFromString(contents)

  def service_name(self): return self.service_name_

  def set_service_name(self, x):
    self.has_service_name_ = 1
    self.service_name_ = x

  def clear_service_name(self):
    if self.has_service_name_:
      self.has_service_name_ = 0
      self.service_name_ = ""

  def has_service_name(self): return self.has_service_name_

  def method(self): return self.method_

  def set_method(self, x):
    self.has_method_ = 1
    self.method_ = x

  def clear_method(self):
    if self.has_method_:
      self.has_method_ = 0
      self.method_ = ""

  def has_method(self): return self.has_method_

  def request(self): return self.request_

  def mutable_request(self): self.has_request_ = 1; return self.request_

  def clear_request(self):self.has_request_ = 0; self.request_.Clear()

  def has_request(self): return self.has_request_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_service_name()): self.set_service_name(x.service_name())
    if (x.has_method()): self.set_method(x.method())
    if (x.has_request()): self.mutable_request().MergeFrom(x.request())

  def Equals(self, x):
    if x is self: return 1
    if self.has_service_name_ != x.has_service_name_: return 0
    if self.has_service_name_ and self.service_name_ != x.service_name_: return 0
    if self.has_method_ != x.has_method_: return 0
    if self.has_method_ and self.method_ != x.method_: return 0
    if self.has_request_ != x.has_request_: return 0
    if self.has_request_ and self.request_ != x.request_: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_service_name_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: service_name not set.')
    if (not self.has_method_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: method not set.')
    if (not self.has_request_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: request not set.')
    elif not self.request_.IsInitialized(debug_strs): initialized = 0
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthString(len(self.service_name_))
    n += self.lengthString(len(self.method_))
    n += self.lengthString(self.request_.ByteSize())
    return n + 3

  def ByteSizePartial(self):
    n = 0
    if (self.has_service_name_):
      n += 1
      n += self.lengthString(len(self.service_name_))
    if (self.has_method_):
      n += 1
      n += self.lengthString(len(self.method_))
    if (self.has_request_):
      n += 1
      n += self.lengthString(self.request_.ByteSizePartial())
    return n

  def Clear(self):
    self.clear_service_name()
    self.clear_method()
    self.clear_request()

  def OutputUnchecked(self, out):
    out.putVarInt32(18)
    out.putPrefixedString(self.service_name_)
    out.putVarInt32(26)
    out.putPrefixedString(self.method_)
    out.putVarInt32(34)
    out.putVarInt32(self.request_.ByteSize())
    self.request_.OutputUnchecked(out)

  def OutputPartial(self, out):
    if (self.has_service_name_):
      out.putVarInt32(18)
      out.putPrefixedString(self.service_name_)
    if (self.has_method_):
      out.putVarInt32(26)
      out.putPrefixedString(self.method_)
    if (self.has_request_):
      out.putVarInt32(34)
      out.putVarInt32(self.request_.ByteSizePartial())
      self.request_.OutputPartial(out)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 18:
        self.set_service_name(d.getPrefixedString())
        continue
      if tt == 26:
        self.set_method(d.getPrefixedString())
        continue
      if tt == 34:
        length = d.getVarInt32()
        tmp = ProtocolBuffer.Decoder(d.buffer(), d.pos(), d.pos() + length)
        d.skip(length)
        self.mutable_request().TryMerge(tmp)
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_service_name_: res+=prefix+("service_name: %s\n" % self.DebugFormatString(self.service_name_))
    if self.has_method_: res+=prefix+("method: %s\n" % self.DebugFormatString(self.method_))
    if self.has_request_:
      res+=prefix+"request <\n"
      res+=self.request_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+">\n"
    return res


  def _BuildTagLookupTable(sparse, maxtag, default=None):
    return tuple([sparse.get(i, default) for i in xrange(0, 1+maxtag)])

  kservice_name = 2
  kmethod = 3
  krequest = 4

  _TEXT = _BuildTagLookupTable({
    0: "ErrorCode",
    2: "service_name",
    3: "method",
    4: "request",
  }, 4)

  _TYPES = _BuildTagLookupTable({
    0: ProtocolBuffer.Encoder.NUMERIC,
    2: ProtocolBuffer.Encoder.STRING,
    3: ProtocolBuffer.Encoder.STRING,
    4: ProtocolBuffer.Encoder.STRING,
  }, 4, ProtocolBuffer.Encoder.MAX_TYPE)

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class ApplicationError(ProtocolBuffer.ProtocolMessage):
  has_code_ = 0
  code_ = 0
  has_detail_ = 0
  detail_ = ""

  def __init__(self, contents=None):
    if contents is not None: self.MergeFromString(contents)

  def code(self): return self.code_

  def set_code(self, x):
    self.has_code_ = 1
    self.code_ = x

  def clear_code(self):
    if self.has_code_:
      self.has_code_ = 0
      self.code_ = 0

  def has_code(self): return self.has_code_

  def detail(self): return self.detail_

  def set_detail(self, x):
    self.has_detail_ = 1
    self.detail_ = x

  def clear_detail(self):
    if self.has_detail_:
      self.has_detail_ = 0
      self.detail_ = ""

  def has_detail(self): return self.has_detail_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_code()): self.set_code(x.code())
    if (x.has_detail()): self.set_detail(x.detail())

  def Equals(self, x):
    if x is self: return 1
    if self.has_code_ != x.has_code_: return 0
    if self.has_code_ and self.code_ != x.code_: return 0
    if self.has_detail_ != x.has_detail_: return 0
    if self.has_detail_ and self.detail_ != x.detail_: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_code_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: code not set.')
    if (not self.has_detail_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: detail not set.')
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthVarInt64(self.code_)
    n += self.lengthString(len(self.detail_))
    return n + 2

  def ByteSizePartial(self):
    n = 0
    if (self.has_code_):
      n += 1
      n += self.lengthVarInt64(self.code_)
    if (self.has_detail_):
      n += 1
      n += self.lengthString(len(self.detail_))
    return n

  def Clear(self):
    self.clear_code()
    self.clear_detail()

  def OutputUnchecked(self, out):
    out.putVarInt32(8)
    out.putVarInt32(self.code_)
    out.putVarInt32(18)
    out.putPrefixedString(self.detail_)

  def OutputPartial(self, out):
    if (self.has_code_):
      out.putVarInt32(8)
      out.putVarInt32(self.code_)
    if (self.has_detail_):
      out.putVarInt32(18)
      out.putPrefixedString(self.detail_)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 8:
        self.set_code(d.getVarInt32())
        continue
      if tt == 18:
        self.set_detail(d.getPrefixedString())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_code_: res+=prefix+("code: %s\n" % self.DebugFormatInt32(self.code_))
    if self.has_detail_: res+=prefix+("detail: %s\n" % self.DebugFormatString(self.detail_))
    return res


  def _BuildTagLookupTable(sparse, maxtag, default=None):
    return tuple([sparse.get(i, default) for i in xrange(0, 1+maxtag)])

  kcode = 1
  kdetail = 2

  _TEXT = _BuildTagLookupTable({
    0: "ErrorCode",
    1: "code",
    2: "detail",
  }, 2)

  _TYPES = _BuildTagLookupTable({
    0: ProtocolBuffer.Encoder.NUMERIC,
    1: ProtocolBuffer.Encoder.NUMERIC,
    2: ProtocolBuffer.Encoder.STRING,
  }, 2, ProtocolBuffer.Encoder.MAX_TYPE)

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class Response(ProtocolBuffer.ProtocolMessage):
  has_response_ = 0
  response_ = None
  has_exception_ = 0
  exception_ = None
  has_application_error_ = 0
  application_error_ = None
  has_java_exception_ = 0
  java_exception_ = None

  def __init__(self, contents=None):
    self.lazy_init_lock_ = thread.allocate_lock()
    if contents is not None: self.MergeFromString(contents)

  def response(self):
    if self.response_ is None:
      self.lazy_init_lock_.acquire()
      try:
        if self.response_ is None: self.response_ = RawMessage()
      finally:
        self.lazy_init_lock_.release()
    return self.response_

  def mutable_response(self): self.has_response_ = 1; return self.response()

  def clear_response(self):
    if self.has_response_:
      self.has_response_ = 0;
      if self.response_ is not None: self.response_.Clear()

  def has_response(self): return self.has_response_

  def exception(self):
    if self.exception_ is None:
      self.lazy_init_lock_.acquire()
      try:
        if self.exception_ is None: self.exception_ = RawMessage()
      finally:
        self.lazy_init_lock_.release()
    return self.exception_

  def mutable_exception(self): self.has_exception_ = 1; return self.exception()

  def clear_exception(self):
    if self.has_exception_:
      self.has_exception_ = 0;
      if self.exception_ is not None: self.exception_.Clear()

  def has_exception(self): return self.has_exception_

  def application_error(self):
    if self.application_error_ is None:
      self.lazy_init_lock_.acquire()
      try:
        if self.application_error_ is None: self.application_error_ = ApplicationError()
      finally:
        self.lazy_init_lock_.release()
    return self.application_error_

  def mutable_application_error(self): self.has_application_error_ = 1; return self.application_error()

  def clear_application_error(self):
    if self.has_application_error_:
      self.has_application_error_ = 0;
      if self.application_error_ is not None: self.application_error_.Clear()

  def has_application_error(self): return self.has_application_error_

  def java_exception(self):
    if self.java_exception_ is None:
      self.lazy_init_lock_.acquire()
      try:
        if self.java_exception_ is None: self.java_exception_ = RawMessage()
      finally:
        self.lazy_init_lock_.release()
    return self.java_exception_

  def mutable_java_exception(self): self.has_java_exception_ = 1; return self.java_exception()

  def clear_java_exception(self):
    if self.has_java_exception_:
      self.has_java_exception_ = 0;
      if self.java_exception_ is not None: self.java_exception_.Clear()

  def has_java_exception(self): return self.has_java_exception_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_response()): self.mutable_response().MergeFrom(x.response())
    if (x.has_exception()): self.mutable_exception().MergeFrom(x.exception())
    if (x.has_application_error()): self.mutable_application_error().MergeFrom(x.application_error())
    if (x.has_java_exception()): self.mutable_java_exception().MergeFrom(x.java_exception())

  def Equals(self, x):
    if x is self: return 1
    if self.has_response_ != x.has_response_: return 0
    if self.has_response_ and self.response_ != x.response_: return 0
    if self.has_exception_ != x.has_exception_: return 0
    if self.has_exception_ and self.exception_ != x.exception_: return 0
    if self.has_application_error_ != x.has_application_error_: return 0
    if self.has_application_error_ and self.application_error_ != x.application_error_: return 0
    if self.has_java_exception_ != x.has_java_exception_: return 0
    if self.has_java_exception_ and self.java_exception_ != x.java_exception_: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (self.has_response_ and not self.response_.IsInitialized(debug_strs)): initialized = 0
    if (self.has_exception_ and not self.exception_.IsInitialized(debug_strs)): initialized = 0
    if (self.has_application_error_ and not self.application_error_.IsInitialized(debug_strs)): initialized = 0
    if (self.has_java_exception_ and not self.java_exception_.IsInitialized(debug_strs)): initialized = 0
    return initialized

  def ByteSize(self):
    n = 0
    if (self.has_response_): n += 1 + self.lengthString(self.response_.ByteSize())
    if (self.has_exception_): n += 1 + self.lengthString(self.exception_.ByteSize())
    if (self.has_application_error_): n += 1 + self.lengthString(self.application_error_.ByteSize())
    if (self.has_java_exception_): n += 1 + self.lengthString(self.java_exception_.ByteSize())
    return n

  def ByteSizePartial(self):
    n = 0
    if (self.has_response_): n += 1 + self.lengthString(self.response_.ByteSizePartial())
    if (self.has_exception_): n += 1 + self.lengthString(self.exception_.ByteSizePartial())
    if (self.has_application_error_): n += 1 + self.lengthString(self.application_error_.ByteSizePartial())
    if (self.has_java_exception_): n += 1 + self.lengthString(self.java_exception_.ByteSizePartial())
    return n

  def Clear(self):
    self.clear_response()
    self.clear_exception()
    self.clear_application_error()
    self.clear_java_exception()

  def OutputUnchecked(self, out):
    if (self.has_response_):
      out.putVarInt32(10)
      out.putVarInt32(self.response_.ByteSize())
      self.response_.OutputUnchecked(out)
    if (self.has_exception_):
      out.putVarInt32(18)
      out.putVarInt32(self.exception_.ByteSize())
      self.exception_.OutputUnchecked(out)
    if (self.has_application_error_):
      out.putVarInt32(26)
      out.putVarInt32(self.application_error_.ByteSize())
      self.application_error_.OutputUnchecked(out)
    if (self.has_java_exception_):
      out.putVarInt32(34)
      out.putVarInt32(self.java_exception_.ByteSize())
      self.java_exception_.OutputUnchecked(out)

  def OutputPartial(self, out):
    if (self.has_response_):
      out.putVarInt32(10)
      out.putVarInt32(self.response_.ByteSizePartial())
      self.response_.OutputPartial(out)
    if (self.has_exception_):
      out.putVarInt32(18)
      out.putVarInt32(self.exception_.ByteSizePartial())
      self.exception_.OutputPartial(out)
    if (self.has_application_error_):
      out.putVarInt32(26)
      out.putVarInt32(self.application_error_.ByteSizePartial())
      self.application_error_.OutputPartial(out)
    if (self.has_java_exception_):
      out.putVarInt32(34)
      out.putVarInt32(self.java_exception_.ByteSizePartial())
      self.java_exception_.OutputPartial(out)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 10:
        length = d.getVarInt32()
        tmp = ProtocolBuffer.Decoder(d.buffer(), d.pos(), d.pos() + length)
        d.skip(length)
        self.mutable_response().TryMerge(tmp)
        continue
      if tt == 18:
        length = d.getVarInt32()
        tmp = ProtocolBuffer.Decoder(d.buffer(), d.pos(), d.pos() + length)
        d.skip(length)
        self.mutable_exception().TryMerge(tmp)
        continue
      if tt == 26:
        length = d.getVarInt32()
        tmp = ProtocolBuffer.Decoder(d.buffer(), d.pos(), d.pos() + length)
        d.skip(length)
        self.mutable_application_error().TryMerge(tmp)
        continue
      if tt == 34:
        length = d.getVarInt32()
        tmp = ProtocolBuffer.Decoder(d.buffer(), d.pos(), d.pos() + length)
        d.skip(length)
        self.mutable_java_exception().TryMerge(tmp)
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_response_:
      res+=prefix+"response <\n"
      res+=self.response_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+">\n"
    if self.has_exception_:
      res+=prefix+"exception <\n"
      res+=self.exception_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+">\n"
    if self.has_application_error_:
      res+=prefix+"application_error <\n"
      res+=self.application_error_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+">\n"
    if self.has_java_exception_:
      res+=prefix+"java_exception <\n"
      res+=self.java_exception_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+">\n"
    return res


  def _BuildTagLookupTable(sparse, maxtag, default=None):
    return tuple([sparse.get(i, default) for i in xrange(0, 1+maxtag)])

  kresponse = 1
  kexception = 2
  kapplication_error = 3
  kjava_exception = 4

  _TEXT = _BuildTagLookupTable({
    0: "ErrorCode",
    1: "response",
    2: "exception",
    3: "application_error",
    4: "java_exception",
  }, 4)

  _TYPES = _BuildTagLookupTable({
    0: ProtocolBuffer.Encoder.NUMERIC,
    1: ProtocolBuffer.Encoder.STRING,
    2: ProtocolBuffer.Encoder.STRING,
    3: ProtocolBuffer.Encoder.STRING,
    4: ProtocolBuffer.Encoder.STRING,
  }, 4, ProtocolBuffer.Encoder.MAX_TYPE)

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class TransactionRequest_Precondition(ProtocolBuffer.ProtocolMessage):
  has_key_ = 0
  has_hash_ = 0
  hash_ = ""

  def __init__(self, contents=None):
    self.key_ = Reference()
    if contents is not None: self.MergeFromString(contents)

  def key(self): return self.key_

  def mutable_key(self): self.has_key_ = 1; return self.key_

  def clear_key(self):self.has_key_ = 0; self.key_.Clear()

  def has_key(self): return self.has_key_

  def hash(self): return self.hash_

  def set_hash(self, x):
    self.has_hash_ = 1
    self.hash_ = x

  def clear_hash(self):
    if self.has_hash_:
      self.has_hash_ = 0
      self.hash_ = ""

  def has_hash(self): return self.has_hash_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_key()): self.mutable_key().MergeFrom(x.key())
    if (x.has_hash()): self.set_hash(x.hash())

  def Equals(self, x):
    if x is self: return 1
    if self.has_key_ != x.has_key_: return 0
    if self.has_key_ and self.key_ != x.key_: return 0
    if self.has_hash_ != x.has_hash_: return 0
    if self.has_hash_ and self.hash_ != x.hash_: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_key_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: key not set.')
    elif not self.key_.IsInitialized(debug_strs): initialized = 0
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthString(self.key_.ByteSize())
    if (self.has_hash_): n += 1 + self.lengthString(len(self.hash_))
    return n + 1

  def ByteSizePartial(self):
    n = 0
    if (self.has_key_):
      n += 1
      n += self.lengthString(self.key_.ByteSizePartial())
    if (self.has_hash_): n += 1 + self.lengthString(len(self.hash_))
    return n

  def Clear(self):
    self.clear_key()
    self.clear_hash()

  def OutputUnchecked(self, out):
    out.putVarInt32(18)
    out.putVarInt32(self.key_.ByteSize())
    self.key_.OutputUnchecked(out)
    if (self.has_hash_):
      out.putVarInt32(26)
      out.putPrefixedString(self.hash_)

  def OutputPartial(self, out):
    if (self.has_key_):
      out.putVarInt32(18)
      out.putVarInt32(self.key_.ByteSizePartial())
      self.key_.OutputPartial(out)
    if (self.has_hash_):
      out.putVarInt32(26)
      out.putPrefixedString(self.hash_)

  def TryMerge(self, d):
    while 1:
      tt = d.getVarInt32()
      if tt == 12: break
      if tt == 18:
        length = d.getVarInt32()
        tmp = ProtocolBuffer.Decoder(d.buffer(), d.pos(), d.pos() + length)
        d.skip(length)
        self.mutable_key().TryMerge(tmp)
        continue
      if tt == 26:
        self.set_hash(d.getPrefixedString())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_key_:
      res+=prefix+"key <\n"
      res+=self.key_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+">\n"
    if self.has_hash_: res+=prefix+("hash: %s\n" % self.DebugFormatString(self.hash_))
    return res

class TransactionRequest(ProtocolBuffer.ProtocolMessage):
  has_puts_ = 0
  puts_ = None
  has_deletes_ = 0
  deletes_ = None

  def __init__(self, contents=None):
    self.precondition_ = []
    self.lazy_init_lock_ = thread.allocate_lock()
    if contents is not None: self.MergeFromString(contents)

  def precondition_size(self): return len(self.precondition_)
  def precondition_list(self): return self.precondition_

  def precondition(self, i):
    return self.precondition_[i]

  def mutable_precondition(self, i):
    return self.precondition_[i]

  def add_precondition(self):
    x = TransactionRequest_Precondition()
    self.precondition_.append(x)
    return x

  def clear_precondition(self):
    self.precondition_ = []
  def puts(self):
    if self.puts_ is None:
      self.lazy_init_lock_.acquire()
      try:
        if self.puts_ is None: self.puts_ = PutRequest()
      finally:
        self.lazy_init_lock_.release()
    return self.puts_

  def mutable_puts(self): self.has_puts_ = 1; return self.puts()

  def clear_puts(self):
    if self.has_puts_:
      self.has_puts_ = 0;
      if self.puts_ is not None: self.puts_.Clear()

  def has_puts(self): return self.has_puts_

  def deletes(self):
    if self.deletes_ is None:
      self.lazy_init_lock_.acquire()
      try:
        if self.deletes_ is None: self.deletes_ = DeleteRequest()
      finally:
        self.lazy_init_lock_.release()
    return self.deletes_

  def mutable_deletes(self): self.has_deletes_ = 1; return self.deletes()

  def clear_deletes(self):
    if self.has_deletes_:
      self.has_deletes_ = 0;
      if self.deletes_ is not None: self.deletes_.Clear()

  def has_deletes(self): return self.has_deletes_


  def MergeFrom(self, x):
    assert x is not self
    for i in xrange(x.precondition_size()): self.add_precondition().CopyFrom(x.precondition(i))
    if (x.has_puts()): self.mutable_puts().MergeFrom(x.puts())
    if (x.has_deletes()): self.mutable_deletes().MergeFrom(x.deletes())

  def Equals(self, x):
    if x is self: return 1
    if len(self.precondition_) != len(x.precondition_): return 0
    for e1, e2 in zip(self.precondition_, x.precondition_):
      if e1 != e2: return 0
    if self.has_puts_ != x.has_puts_: return 0
    if self.has_puts_ and self.puts_ != x.puts_: return 0
    if self.has_deletes_ != x.has_deletes_: return 0
    if self.has_deletes_ and self.deletes_ != x.deletes_: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    for p in self.precondition_:
      if not p.IsInitialized(debug_strs): initialized=0
    if (self.has_puts_ and not self.puts_.IsInitialized(debug_strs)): initialized = 0
    if (self.has_deletes_ and not self.deletes_.IsInitialized(debug_strs)): initialized = 0
    return initialized

  def ByteSize(self):
    n = 0
    n += 2 * len(self.precondition_)
    for i in xrange(len(self.precondition_)): n += self.precondition_[i].ByteSize()
    if (self.has_puts_): n += 1 + self.lengthString(self.puts_.ByteSize())
    if (self.has_deletes_): n += 1 + self.lengthString(self.deletes_.ByteSize())
    return n

  def ByteSizePartial(self):
    n = 0
    n += 2 * len(self.precondition_)
    for i in xrange(len(self.precondition_)): n += self.precondition_[i].ByteSizePartial()
    if (self.has_puts_): n += 1 + self.lengthString(self.puts_.ByteSizePartial())
    if (self.has_deletes_): n += 1 + self.lengthString(self.deletes_.ByteSizePartial())
    return n

  def Clear(self):
    self.clear_precondition()
    self.clear_puts()
    self.clear_deletes()

  def OutputUnchecked(self, out):
    for i in xrange(len(self.precondition_)):
      out.putVarInt32(11)
      self.precondition_[i].OutputUnchecked(out)
      out.putVarInt32(12)
    if (self.has_puts_):
      out.putVarInt32(34)
      out.putVarInt32(self.puts_.ByteSize())
      self.puts_.OutputUnchecked(out)
    if (self.has_deletes_):
      out.putVarInt32(42)
      out.putVarInt32(self.deletes_.ByteSize())
      self.deletes_.OutputUnchecked(out)

  def OutputPartial(self, out):
    for i in xrange(len(self.precondition_)):
      out.putVarInt32(11)
      self.precondition_[i].OutputPartial(out)
      out.putVarInt32(12)
    if (self.has_puts_):
      out.putVarInt32(34)
      out.putVarInt32(self.puts_.ByteSizePartial())
      self.puts_.OutputPartial(out)
    if (self.has_deletes_):
      out.putVarInt32(42)
      out.putVarInt32(self.deletes_.ByteSizePartial())
      self.deletes_.OutputPartial(out)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 11:
        self.add_precondition().TryMerge(d)
        continue
      if tt == 34:
        length = d.getVarInt32()
        tmp = ProtocolBuffer.Decoder(d.buffer(), d.pos(), d.pos() + length)
        d.skip(length)
        self.mutable_puts().TryMerge(tmp)
        continue
      if tt == 42:
        length = d.getVarInt32()
        tmp = ProtocolBuffer.Decoder(d.buffer(), d.pos(), d.pos() + length)
        d.skip(length)
        self.mutable_deletes().TryMerge(tmp)
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    cnt=0
    for e in self.precondition_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("Precondition%s {\n" % elm)
      res+=e.__str__(prefix + "  ", printElemNumber)
      res+=prefix+"}\n"
      cnt+=1
    if self.has_puts_:
      res+=prefix+"puts <\n"
      res+=self.puts_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+">\n"
    if self.has_deletes_:
      res+=prefix+"deletes <\n"
      res+=self.deletes_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+">\n"
    return res


  def _BuildTagLookupTable(sparse, maxtag, default=None):
    return tuple([sparse.get(i, default) for i in xrange(0, 1+maxtag)])

  kPreconditionGroup = 1
  kPreconditionkey = 2
  kPreconditionhash = 3
  kputs = 4
  kdeletes = 5

  _TEXT = _BuildTagLookupTable({
    0: "ErrorCode",
    1: "Precondition",
    2: "key",
    3: "hash",
    4: "puts",
    5: "deletes",
  }, 5)

  _TYPES = _BuildTagLookupTable({
    0: ProtocolBuffer.Encoder.NUMERIC,
    1: ProtocolBuffer.Encoder.STARTGROUP,
    2: ProtocolBuffer.Encoder.STRING,
    3: ProtocolBuffer.Encoder.STRING,
    4: ProtocolBuffer.Encoder.STRING,
    5: ProtocolBuffer.Encoder.STRING,
  }, 5, ProtocolBuffer.Encoder.MAX_TYPE)

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""

__all__ = ['Request','ApplicationError','Response','TransactionRequest','TransactionRequest_Precondition']
