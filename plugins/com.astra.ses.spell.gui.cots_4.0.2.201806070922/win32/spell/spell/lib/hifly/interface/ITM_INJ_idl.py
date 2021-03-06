# Python stubs generated by omniidl from ITM_INJ.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)

# #include "IBASE.idl"
import spell.lib.hifly.interface.IBASE_idl
_0_IBASE = omniORB.openModule("spell.lib.hifly.interface.IBASE")
_0_IBASE__POA = omniORB.openModule("spell.lib.hifly.interface.IBASE__POA")
# #include "IBASE_IF.idl"
import spell.lib.hifly.interface.IBASE_IF_idl
_0_IBASE_IF = omniORB.openModule("spell.lib.hifly.interface.IBASE_IF")
_0_IBASE_IF__POA = omniORB.openModule("spell.lib.hifly.interface.IBASE_IF__POA")
# #include "ITM.idl"
import spell.lib.hifly.interface.ITM_idl
_0_ITM = omniORB.openModule("spell.lib.hifly.interface.ITM")
_0_ITM__POA = omniORB.openModule("spell.lib.hifly.interface.ITM__POA")

#
# Start of module "ITM_INJ"
#
__name__ = "spell.lib.hifly.interface.ITM_INJ"
_0_ITM_INJ = omniORB.openModule("spell.lib.hifly.interface.ITM_INJ", r"ITM_INJ.idl")
_0_ITM_INJ__POA = omniORB.openModule("spell.lib.hifly.interface.ITM_INJ__POA", r"ITM_INJ.idl")


# interface ParamInjectMngr
_0_ITM_INJ._d_ParamInjectMngr = (omniORB.tcInternal.tv_objref, "IDL:ITM_INJ/ParamInjectMngr:1.0", "ParamInjectMngr")
omniORB.typeMapping["IDL:ITM_INJ/ParamInjectMngr:1.0"] = _0_ITM_INJ._d_ParamInjectMngr
_0_ITM_INJ.ParamInjectMngr = omniORB.newEmptyClass()
class ParamInjectMngr (_0_IBASE_IF.IBASE_IFheartbeatSvr):
    _NP_RepositoryId = _0_ITM_INJ._d_ParamInjectMngr[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil

    ServiceName = "TM_INJ"


_0_ITM_INJ.ParamInjectMngr = ParamInjectMngr
_0_ITM_INJ._tc_ParamInjectMngr = omniORB.tcInternal.createTypeCode(_0_ITM_INJ._d_ParamInjectMngr)
omniORB.registerType(ParamInjectMngr._NP_RepositoryId, _0_ITM_INJ._d_ParamInjectMngr, _0_ITM_INJ._tc_ParamInjectMngr)

# ParamInjectMngr operations and attributes
ParamInjectMngr._d_getUTC = ((), (omniORB.typeMapping["IDL:IBASE/Time:1.0"], ), None)
ParamInjectMngr._d_getDeltaTimeToUTC = ((), (omniORB.typeMapping["IDL:IBASE/Time:1.0"], ), None)
ParamInjectMngr._d_getDefaultDataStream = ((), (omniORB.tcInternal.tv_long, ), None)
ParamInjectMngr._d_getDefaultSpacecraftID = ((), ((omniORB.tcInternal.tv_string,0), ), None)
ParamInjectMngr._d_injectParameter = ((omniORB.typeMapping["IDL:ITM/InjectParam:1.0"], (omniORB.tcInternal.tv_string,0), omniORB.typeMapping["IDL:IBASE/Time:1.0"], omniORB.tcInternal.tv_long, (omniORB.tcInternal.tv_string,0)), (), {_0_IBASE.NotFound._NP_RepositoryId: _0_IBASE._d_NotFound, _0_IBASE.NotProcessed._NP_RepositoryId: _0_IBASE._d_NotProcessed})
ParamInjectMngr._d_injectParameterWithDefaults = ((omniORB.typeMapping["IDL:ITM/InjectParam:1.0"], (omniORB.tcInternal.tv_string,0)), (), {_0_IBASE.NotFound._NP_RepositoryId: _0_IBASE._d_NotFound, _0_IBASE.NotProcessed._NP_RepositoryId: _0_IBASE._d_NotProcessed})
ParamInjectMngr._d_injectParameters = ((omniORB.typeMapping["IDL:ITM/InjectParams:1.0"], (omniORB.tcInternal.tv_string,0), omniORB.typeMapping["IDL:IBASE/Time:1.0"], omniORB.tcInternal.tv_long, (omniORB.tcInternal.tv_string,0)), (), {_0_IBASE.NotFound._NP_RepositoryId: _0_IBASE._d_NotFound, _0_IBASE.NotProcessed._NP_RepositoryId: _0_IBASE._d_NotProcessed})
ParamInjectMngr._d_injectParametersWithDefaults = ((omniORB.typeMapping["IDL:ITM/InjectParams:1.0"], (omniORB.tcInternal.tv_string,0)), (), {_0_IBASE.NotFound._NP_RepositoryId: _0_IBASE._d_NotFound, _0_IBASE.NotProcessed._NP_RepositoryId: _0_IBASE._d_NotProcessed})
ParamInjectMngr._d_injectParametersInPacket = ((omniORB.typeMapping["IDL:ITM/InjectRawParams:1.0"], omniORB.tcInternal.tv_long, (omniORB.tcInternal.tv_string,0), omniORB.typeMapping["IDL:IBASE/Time:1.0"]), (), {_0_IBASE.NotFound._NP_RepositoryId: _0_IBASE._d_NotFound, _0_IBASE.NotProcessed._NP_RepositoryId: _0_IBASE._d_NotProcessed})
ParamInjectMngr._d_injectParametersInPacketServerTime = ((omniORB.typeMapping["IDL:ITM/InjectRawParams:1.0"], omniORB.tcInternal.tv_long, (omniORB.tcInternal.tv_string,0)), (), {_0_IBASE.NotFound._NP_RepositoryId: _0_IBASE._d_NotFound, _0_IBASE.NotProcessed._NP_RepositoryId: _0_IBASE._d_NotProcessed})
ParamInjectMngr._d_getEquipmentSpid = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_long, ), {_0_IBASE.NotFound._NP_RepositoryId: _0_IBASE._d_NotFound})

# ParamInjectMngr object reference
class _objref_ParamInjectMngr (_0_IBASE_IF._objref_IBASE_IFheartbeatSvr):
    _NP_RepositoryId = ParamInjectMngr._NP_RepositoryId

    def __init__(self):
        _0_IBASE_IF._objref_IBASE_IFheartbeatSvr.__init__(self)

    def getUTC(self, *args):
        return _omnipy.invoke(self, "getUTC", _0_ITM_INJ.ParamInjectMngr._d_getUTC, args)

    def getDeltaTimeToUTC(self, *args):
        return _omnipy.invoke(self, "getDeltaTimeToUTC", _0_ITM_INJ.ParamInjectMngr._d_getDeltaTimeToUTC, args)

    def getDefaultDataStream(self, *args):
        return _omnipy.invoke(self, "getDefaultDataStream", _0_ITM_INJ.ParamInjectMngr._d_getDefaultDataStream, args)

    def getDefaultSpacecraftID(self, *args):
        return _omnipy.invoke(self, "getDefaultSpacecraftID", _0_ITM_INJ.ParamInjectMngr._d_getDefaultSpacecraftID, args)

    def injectParameter(self, *args):
        return _omnipy.invoke(self, "injectParameter", _0_ITM_INJ.ParamInjectMngr._d_injectParameter, args)

    def injectParameterWithDefaults(self, *args):
        return _omnipy.invoke(self, "injectParameterWithDefaults", _0_ITM_INJ.ParamInjectMngr._d_injectParameterWithDefaults, args)

    def injectParameters(self, *args):
        return _omnipy.invoke(self, "injectParameters", _0_ITM_INJ.ParamInjectMngr._d_injectParameters, args)

    def injectParametersWithDefaults(self, *args):
        return _omnipy.invoke(self, "injectParametersWithDefaults", _0_ITM_INJ.ParamInjectMngr._d_injectParametersWithDefaults, args)

    def injectParametersInPacket(self, *args):
        return _omnipy.invoke(self, "injectParametersInPacket", _0_ITM_INJ.ParamInjectMngr._d_injectParametersInPacket, args)

    def injectParametersInPacketServerTime(self, *args):
        return _omnipy.invoke(self, "injectParametersInPacketServerTime", _0_ITM_INJ.ParamInjectMngr._d_injectParametersInPacketServerTime, args)

    def getEquipmentSpid(self, *args):
        return _omnipy.invoke(self, "getEquipmentSpid", _0_ITM_INJ.ParamInjectMngr._d_getEquipmentSpid, args)

    __methods__ = ["getUTC", "getDeltaTimeToUTC", "getDefaultDataStream", "getDefaultSpacecraftID", "injectParameter", "injectParameterWithDefaults", "injectParameters", "injectParametersWithDefaults", "injectParametersInPacket", "injectParametersInPacketServerTime", "getEquipmentSpid"] + _0_IBASE_IF._objref_IBASE_IFheartbeatSvr.__methods__

omniORB.registerObjref(ParamInjectMngr._NP_RepositoryId, _objref_ParamInjectMngr)
_0_ITM_INJ._objref_ParamInjectMngr = _objref_ParamInjectMngr
del ParamInjectMngr, _objref_ParamInjectMngr

# ParamInjectMngr skeleton
__name__ = "spell.lib.hifly.interface.ITM_INJ__POA"
class ParamInjectMngr (_0_IBASE_IF__POA.IBASE_IFheartbeatSvr):
    _NP_RepositoryId = _0_ITM_INJ.ParamInjectMngr._NP_RepositoryId


    _omni_op_d = {"getUTC": _0_ITM_INJ.ParamInjectMngr._d_getUTC, "getDeltaTimeToUTC": _0_ITM_INJ.ParamInjectMngr._d_getDeltaTimeToUTC, "getDefaultDataStream": _0_ITM_INJ.ParamInjectMngr._d_getDefaultDataStream, "getDefaultSpacecraftID": _0_ITM_INJ.ParamInjectMngr._d_getDefaultSpacecraftID, "injectParameter": _0_ITM_INJ.ParamInjectMngr._d_injectParameter, "injectParameterWithDefaults": _0_ITM_INJ.ParamInjectMngr._d_injectParameterWithDefaults, "injectParameters": _0_ITM_INJ.ParamInjectMngr._d_injectParameters, "injectParametersWithDefaults": _0_ITM_INJ.ParamInjectMngr._d_injectParametersWithDefaults, "injectParametersInPacket": _0_ITM_INJ.ParamInjectMngr._d_injectParametersInPacket, "injectParametersInPacketServerTime": _0_ITM_INJ.ParamInjectMngr._d_injectParametersInPacketServerTime, "getEquipmentSpid": _0_ITM_INJ.ParamInjectMngr._d_getEquipmentSpid}
    _omni_op_d.update(_0_IBASE_IF__POA.IBASE_IFheartbeatSvr._omni_op_d)

ParamInjectMngr._omni_skeleton = ParamInjectMngr
_0_ITM_INJ__POA.ParamInjectMngr = ParamInjectMngr
omniORB.registerSkeleton(ParamInjectMngr._NP_RepositoryId, ParamInjectMngr)
del ParamInjectMngr
__name__ = "spell.lib.hifly.interface.ITM_INJ"

#
# End of module "ITM_INJ"
#
__name__ = "spell.lib.hifly.interface.ITM_INJ_idl"

_exported_modules = ( "spell.lib.hifly.interface.ITM_INJ", )

# The end.
