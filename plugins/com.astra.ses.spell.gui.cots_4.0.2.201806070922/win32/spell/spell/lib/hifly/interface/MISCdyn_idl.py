# Python stubs generated by omniidl from MISCdyn.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "_GlobalIDL"
#
__name__ = "spell.lib.hifly.interface._GlobalIDL"
_0__GlobalIDL = omniORB.openModule("spell.lib.hifly.interface._GlobalIDL", r"MISCdyn.idl")
_0__GlobalIDL__POA = omniORB.openModule("spell.lib.hifly.interface._GlobalIDL__POA", r"MISCdyn.idl")

# #include "AAIDL/IBASE.idl"
import spell.lib.hifly.interface.IBASE_idl
_0_IBASE = omniORB.openModule("spell.lib.hifly.interface.IBASE")
_0_IBASE__POA = omniORB.openModule("spell.lib.hifly.interface.IBASE__POA")

# interface MISCdynClient
_0__GlobalIDL._d_MISCdynClient = (omniORB.tcInternal.tv_objref, "IDL:MISCdynClient:1.0", "MISCdynClient")
omniORB.typeMapping["IDL:MISCdynClient:1.0"] = _0__GlobalIDL._d_MISCdynClient
_0__GlobalIDL.MISCdynClient = omniORB.newEmptyClass()
class MISCdynClient :
    _NP_RepositoryId = _0__GlobalIDL._d_MISCdynClient[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0__GlobalIDL.MISCdynClient = MISCdynClient
_0__GlobalIDL._tc_MISCdynClient = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_MISCdynClient)
omniORB.registerType(MISCdynClient._NP_RepositoryId, _0__GlobalIDL._d_MISCdynClient, _0__GlobalIDL._tc_MISCdynClient)

# MISCdynClient operations and attributes
MISCdynClient._d_invalidate = (((omniORB.tcInternal.tv_string,0), ), None, None)

# MISCdynClient object reference
class _objref_MISCdynClient (CORBA.Object):
    _NP_RepositoryId = MISCdynClient._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def invalidate(self, *args):
        return _omnipy.invoke(self, "invalidate", _0__GlobalIDL.MISCdynClient._d_invalidate, args)

    __methods__ = ["invalidate"] + CORBA.Object.__methods__

omniORB.registerObjref(MISCdynClient._NP_RepositoryId, _objref_MISCdynClient)
_0__GlobalIDL._objref_MISCdynClient = _objref_MISCdynClient
del MISCdynClient, _objref_MISCdynClient

# MISCdynClient skeleton
__name__ = "spell.lib.hifly.interface._GlobalIDL__POA"
class MISCdynClient (PortableServer.Servant):
    _NP_RepositoryId = _0__GlobalIDL.MISCdynClient._NP_RepositoryId


    _omni_op_d = {"invalidate": _0__GlobalIDL.MISCdynClient._d_invalidate}

MISCdynClient._omni_skeleton = MISCdynClient
_0__GlobalIDL__POA.MISCdynClient = MISCdynClient
omniORB.registerSkeleton(MISCdynClient._NP_RepositoryId, MISCdynClient)
del MISCdynClient
__name__ = "spell.lib.hifly.interface._GlobalIDL"

# interface MISCdynServer
_0__GlobalIDL._d_MISCdynServer = (omniORB.tcInternal.tv_objref, "IDL:MISCdynServer:1.0", "MISCdynServer")
omniORB.typeMapping["IDL:MISCdynServer:1.0"] = _0__GlobalIDL._d_MISCdynServer
_0__GlobalIDL.MISCdynServer = omniORB.newEmptyClass()
class MISCdynServer (_0__GlobalIDL.MISCdynClient):
    _NP_RepositoryId = _0__GlobalIDL._d_MISCdynServer[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0__GlobalIDL.MISCdynServer = MISCdynServer
_0__GlobalIDL._tc_MISCdynServer = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_MISCdynServer)
omniORB.registerType(MISCdynServer._NP_RepositoryId, _0__GlobalIDL._d_MISCdynServer, _0__GlobalIDL._tc_MISCdynServer)

# MISCdynServer operations and attributes
MISCdynServer._d_isOperational = ((), (omniORB.tcInternal.tv_boolean, ), None)
MISCdynServer._d_signOn = ((omniORB.typeMapping["IDL:MISCdynClient:1.0"], ), (), None)
MISCdynServer._d_signOff = ((omniORB.typeMapping["IDL:MISCdynClient:1.0"], ), (), None)
MISCdynServer._d_getVariable = (((omniORB.tcInternal.tv_string,0), ), ((omniORB.tcInternal.tv_string,0), ), None)
MISCdynServer._d_setVariable = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (), None)
MISCdynServer._d_setMiscTMPacket = ((omniORB.typeMapping["IDL:IBASE/ByteString:1.0"], ), None, None)

# MISCdynServer object reference
class _objref_MISCdynServer (_0__GlobalIDL._objref_MISCdynClient):
    _NP_RepositoryId = MISCdynServer._NP_RepositoryId

    def __init__(self):
        _0__GlobalIDL._objref_MISCdynClient.__init__(self)

    def isOperational(self, *args):
        return _omnipy.invoke(self, "isOperational", _0__GlobalIDL.MISCdynServer._d_isOperational, args)

    def signOn(self, *args):
        return _omnipy.invoke(self, "signOn", _0__GlobalIDL.MISCdynServer._d_signOn, args)

    def signOff(self, *args):
        return _omnipy.invoke(self, "signOff", _0__GlobalIDL.MISCdynServer._d_signOff, args)

    def getVariable(self, *args):
        return _omnipy.invoke(self, "getVariable", _0__GlobalIDL.MISCdynServer._d_getVariable, args)

    def setVariable(self, *args):
        return _omnipy.invoke(self, "setVariable", _0__GlobalIDL.MISCdynServer._d_setVariable, args)

    def setMiscTMPacket(self, *args):
        return _omnipy.invoke(self, "setMiscTMPacket", _0__GlobalIDL.MISCdynServer._d_setMiscTMPacket, args)

    __methods__ = ["isOperational", "signOn", "signOff", "getVariable", "setVariable", "setMiscTMPacket"] + _0__GlobalIDL._objref_MISCdynClient.__methods__

omniORB.registerObjref(MISCdynServer._NP_RepositoryId, _objref_MISCdynServer)
_0__GlobalIDL._objref_MISCdynServer = _objref_MISCdynServer
del MISCdynServer, _objref_MISCdynServer

# MISCdynServer skeleton
__name__ = "spell.lib.hifly.interface._GlobalIDL__POA"
class MISCdynServer (_0__GlobalIDL__POA.MISCdynClient):
    _NP_RepositoryId = _0__GlobalIDL.MISCdynServer._NP_RepositoryId


    _omni_op_d = {"isOperational": _0__GlobalIDL.MISCdynServer._d_isOperational, "signOn": _0__GlobalIDL.MISCdynServer._d_signOn, "signOff": _0__GlobalIDL.MISCdynServer._d_signOff, "getVariable": _0__GlobalIDL.MISCdynServer._d_getVariable, "setVariable": _0__GlobalIDL.MISCdynServer._d_setVariable, "setMiscTMPacket": _0__GlobalIDL.MISCdynServer._d_setMiscTMPacket}
    _omni_op_d.update(_0__GlobalIDL__POA.MISCdynClient._omni_op_d)

MISCdynServer._omni_skeleton = MISCdynServer
_0__GlobalIDL__POA.MISCdynServer = MISCdynServer
omniORB.registerSkeleton(MISCdynServer._NP_RepositoryId, MISCdynServer)
del MISCdynServer
__name__ = "spell.lib.hifly.interface._GlobalIDL"

#
# End of module "_GlobalIDL"
#
__name__ = "spell.lib.hifly.interface.MISCdyn_idl"

_exported_modules = ( "spell.lib.hifly.interface._GlobalIDL", )

# The end.
