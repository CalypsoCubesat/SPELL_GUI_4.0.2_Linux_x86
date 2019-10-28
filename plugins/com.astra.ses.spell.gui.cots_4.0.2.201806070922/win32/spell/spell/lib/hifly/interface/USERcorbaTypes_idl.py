# Python stubs generated by omniidl from USERcorbaTypes.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "_GlobalIDL"
#
__name__ = "spell.lib.hifly.interface._GlobalIDL"
_0__GlobalIDL = omniORB.openModule("spell.lib.hifly.interface._GlobalIDL", r"USERcorbaTypes.idl")
_0__GlobalIDL__POA = omniORB.openModule("spell.lib.hifly.interface._GlobalIDL__POA", r"USERcorbaTypes.idl")


# typedef ... USERcorbaStringSequence
class USERcorbaStringSequence:
    _NP_RepositoryId = "IDL:USERcorbaStringSequence:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.USERcorbaStringSequence = USERcorbaStringSequence
_0__GlobalIDL._d_USERcorbaStringSequence  = (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_string,0), 0)
_0__GlobalIDL._ad_USERcorbaStringSequence = (omniORB.tcInternal.tv_alias, USERcorbaStringSequence._NP_RepositoryId, "USERcorbaStringSequence", (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_string,0), 0))
_0__GlobalIDL._tc_USERcorbaStringSequence = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_USERcorbaStringSequence)
omniORB.registerType(USERcorbaStringSequence._NP_RepositoryId, _0__GlobalIDL._ad_USERcorbaStringSequence, _0__GlobalIDL._tc_USERcorbaStringSequence)
del USERcorbaStringSequence

# typedef ... USERcorbaLongSequence
class USERcorbaLongSequence:
    _NP_RepositoryId = "IDL:USERcorbaLongSequence:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.USERcorbaLongSequence = USERcorbaLongSequence
_0__GlobalIDL._d_USERcorbaLongSequence  = (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_long, 0)
_0__GlobalIDL._ad_USERcorbaLongSequence = (omniORB.tcInternal.tv_alias, USERcorbaLongSequence._NP_RepositoryId, "USERcorbaLongSequence", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_long, 0))
_0__GlobalIDL._tc_USERcorbaLongSequence = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_USERcorbaLongSequence)
omniORB.registerType(USERcorbaLongSequence._NP_RepositoryId, _0__GlobalIDL._ad_USERcorbaLongSequence, _0__GlobalIDL._tc_USERcorbaLongSequence)
del USERcorbaLongSequence

# struct USERtime
_0__GlobalIDL.USERtime = omniORB.newEmptyClass()
class USERtime (omniORB.StructBase):
    _NP_RepositoryId = "IDL:USERtime:1.0"

    def __init__(self, seconds, uSeconds):
        self.seconds = seconds
        self.uSeconds = uSeconds

_0__GlobalIDL.USERtime = USERtime
_0__GlobalIDL._d_USERtime  = (omniORB.tcInternal.tv_struct, USERtime, USERtime._NP_RepositoryId, "USERtime", "seconds", omniORB.tcInternal.tv_long, "uSeconds", omniORB.tcInternal.tv_long)
_0__GlobalIDL._tc_USERtime = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_USERtime)
omniORB.registerType(USERtime._NP_RepositoryId, _0__GlobalIDL._d_USERtime, _0__GlobalIDL._tc_USERtime)
del USERtime

# struct USERcorbaPairStringString
_0__GlobalIDL.USERcorbaPairStringString = omniORB.newEmptyClass()
class USERcorbaPairStringString (omniORB.StructBase):
    _NP_RepositoryId = "IDL:USERcorbaPairStringString:1.0"

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

_0__GlobalIDL.USERcorbaPairStringString = USERcorbaPairStringString
_0__GlobalIDL._d_USERcorbaPairStringString  = (omniORB.tcInternal.tv_struct, USERcorbaPairStringString, USERcorbaPairStringString._NP_RepositoryId, "USERcorbaPairStringString", "s1", (omniORB.tcInternal.tv_string,0), "s2", (omniORB.tcInternal.tv_string,0))
_0__GlobalIDL._tc_USERcorbaPairStringString = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_USERcorbaPairStringString)
omniORB.registerType(USERcorbaPairStringString._NP_RepositoryId, _0__GlobalIDL._d_USERcorbaPairStringString, _0__GlobalIDL._tc_USERcorbaPairStringString)
del USERcorbaPairStringString

# typedef ... USERcorbaStringMap
class USERcorbaStringMap:
    _NP_RepositoryId = "IDL:USERcorbaStringMap:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.USERcorbaStringMap = USERcorbaStringMap
_0__GlobalIDL._d_USERcorbaStringMap  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:USERcorbaPairStringString:1.0"], 0)
_0__GlobalIDL._ad_USERcorbaStringMap = (omniORB.tcInternal.tv_alias, USERcorbaStringMap._NP_RepositoryId, "USERcorbaStringMap", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:USERcorbaPairStringString:1.0"], 0))
_0__GlobalIDL._tc_USERcorbaStringMap = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_USERcorbaStringMap)
omniORB.registerType(USERcorbaStringMap._NP_RepositoryId, _0__GlobalIDL._ad_USERcorbaStringMap, _0__GlobalIDL._tc_USERcorbaStringMap)
del USERcorbaStringMap

# struct USERcorbaCompletePrivData
_0__GlobalIDL.USERcorbaCompletePrivData = omniORB.newEmptyClass()
class USERcorbaCompletePrivData (omniORB.StructBase):
    _NP_RepositoryId = "IDL:USERcorbaCompletePrivData:1.0"

    def __init__(self, name, desc, donated):
        self.name = name
        self.desc = desc
        self.donated = donated

_0__GlobalIDL.USERcorbaCompletePrivData = USERcorbaCompletePrivData
_0__GlobalIDL._d_USERcorbaCompletePrivData  = (omniORB.tcInternal.tv_struct, USERcorbaCompletePrivData, USERcorbaCompletePrivData._NP_RepositoryId, "USERcorbaCompletePrivData", "name", (omniORB.tcInternal.tv_string,0), "desc", (omniORB.tcInternal.tv_string,0), "donated", (omniORB.tcInternal.tv_string,0))
_0__GlobalIDL._tc_USERcorbaCompletePrivData = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_USERcorbaCompletePrivData)
omniORB.registerType(USERcorbaCompletePrivData._NP_RepositoryId, _0__GlobalIDL._d_USERcorbaCompletePrivData, _0__GlobalIDL._tc_USERcorbaCompletePrivData)
del USERcorbaCompletePrivData

# struct USERcorbaStringListMap
_0__GlobalIDL.USERcorbaStringListMap = omniORB.newEmptyClass()
class USERcorbaStringListMap (omniORB.StructBase):
    _NP_RepositoryId = "IDL:USERcorbaStringListMap:1.0"

    def __init__(self, s1, s2, list):
        self.s1 = s1
        self.s2 = s2
        self.list = list

_0__GlobalIDL.USERcorbaStringListMap = USERcorbaStringListMap
_0__GlobalIDL._d_USERcorbaStringListMap  = (omniORB.tcInternal.tv_struct, USERcorbaStringListMap, USERcorbaStringListMap._NP_RepositoryId, "USERcorbaStringListMap", "s1", (omniORB.tcInternal.tv_string,0), "s2", (omniORB.tcInternal.tv_string,0), "list", omniORB.typeMapping["IDL:USERcorbaStringSequence:1.0"])
_0__GlobalIDL._tc_USERcorbaStringListMap = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_USERcorbaStringListMap)
omniORB.registerType(USERcorbaStringListMap._NP_RepositoryId, _0__GlobalIDL._d_USERcorbaStringListMap, _0__GlobalIDL._tc_USERcorbaStringListMap)
del USERcorbaStringListMap

# typedef ... USERcorbaStringListMapSequence
class USERcorbaStringListMapSequence:
    _NP_RepositoryId = "IDL:USERcorbaStringListMapSequence:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.USERcorbaStringListMapSequence = USERcorbaStringListMapSequence
_0__GlobalIDL._d_USERcorbaStringListMapSequence  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:USERcorbaStringListMap:1.0"], 0)
_0__GlobalIDL._ad_USERcorbaStringListMapSequence = (omniORB.tcInternal.tv_alias, USERcorbaStringListMapSequence._NP_RepositoryId, "USERcorbaStringListMapSequence", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:USERcorbaStringListMap:1.0"], 0))
_0__GlobalIDL._tc_USERcorbaStringListMapSequence = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_USERcorbaStringListMapSequence)
omniORB.registerType(USERcorbaStringListMapSequence._NP_RepositoryId, _0__GlobalIDL._ad_USERcorbaStringListMapSequence, _0__GlobalIDL._tc_USERcorbaStringListMapSequence)
del USERcorbaStringListMapSequence

# struct USERcorbaCompleteProfileData
_0__GlobalIDL.USERcorbaCompleteProfileData = omniORB.newEmptyClass()
class USERcorbaCompleteProfileData (omniORB.StructBase):
    _NP_RepositoryId = "IDL:USERcorbaCompleteProfileData:1.0"

    def __init__(self, name, desc, password, domains):
        self.name = name
        self.desc = desc
        self.password = password
        self.domains = domains

_0__GlobalIDL.USERcorbaCompleteProfileData = USERcorbaCompleteProfileData
_0__GlobalIDL._d_USERcorbaCompleteProfileData  = (omniORB.tcInternal.tv_struct, USERcorbaCompleteProfileData, USERcorbaCompleteProfileData._NP_RepositoryId, "USERcorbaCompleteProfileData", "name", (omniORB.tcInternal.tv_string,0), "desc", (omniORB.tcInternal.tv_string,0), "password", (omniORB.tcInternal.tv_string,0), "domains", omniORB.typeMapping["IDL:USERcorbaStringListMapSequence:1.0"])
_0__GlobalIDL._tc_USERcorbaCompleteProfileData = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_USERcorbaCompleteProfileData)
omniORB.registerType(USERcorbaCompleteProfileData._NP_RepositoryId, _0__GlobalIDL._d_USERcorbaCompleteProfileData, _0__GlobalIDL._tc_USERcorbaCompleteProfileData)
del USERcorbaCompleteProfileData

# struct USERcorbaSessionData
_0__GlobalIDL.USERcorbaSessionData = omniORB.newEmptyClass()
class USERcorbaSessionData (omniORB.StructBase):
    _NP_RepositoryId = "IDL:USERcorbaSessionData:1.0"

    def __init__(self, userName, roleName, hostName, domainID, workSpace, loginTime):
        self.userName = userName
        self.roleName = roleName
        self.hostName = hostName
        self.domainID = domainID
        self.workSpace = workSpace
        self.loginTime = loginTime

_0__GlobalIDL.USERcorbaSessionData = USERcorbaSessionData
_0__GlobalIDL._d_USERcorbaSessionData  = (omniORB.tcInternal.tv_struct, USERcorbaSessionData, USERcorbaSessionData._NP_RepositoryId, "USERcorbaSessionData", "userName", (omniORB.tcInternal.tv_string,0), "roleName", (omniORB.tcInternal.tv_string,0), "hostName", (omniORB.tcInternal.tv_string,0), "domainID", (omniORB.tcInternal.tv_string,0), "workSpace", omniORB.tcInternal.tv_long, "loginTime", omniORB.typeMapping["IDL:USERtime:1.0"])
_0__GlobalIDL._tc_USERcorbaSessionData = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_USERcorbaSessionData)
omniORB.registerType(USERcorbaSessionData._NP_RepositoryId, _0__GlobalIDL._d_USERcorbaSessionData, _0__GlobalIDL._tc_USERcorbaSessionData)
del USERcorbaSessionData

# struct USERcorbaActiveSessionDomainData
_0__GlobalIDL.USERcorbaActiveSessionDomainData = omniORB.newEmptyClass()
class USERcorbaActiveSessionDomainData (omniORB.StructBase):
    _NP_RepositoryId = "IDL:USERcorbaActiveSessionDomainData:1.0"

    def __init__(self, domainID, role, workSpace, loginTime, nativePrivileges, receivedPrivs, donatedPrivs):
        self.domainID = domainID
        self.role = role
        self.workSpace = workSpace
        self.loginTime = loginTime
        self.nativePrivileges = nativePrivileges
        self.receivedPrivs = receivedPrivs
        self.donatedPrivs = donatedPrivs

_0__GlobalIDL.USERcorbaActiveSessionDomainData = USERcorbaActiveSessionDomainData
_0__GlobalIDL._d_USERcorbaActiveSessionDomainData  = (omniORB.tcInternal.tv_struct, USERcorbaActiveSessionDomainData, USERcorbaActiveSessionDomainData._NP_RepositoryId, "USERcorbaActiveSessionDomainData", "domainID", (omniORB.tcInternal.tv_string,0), "role", (omniORB.tcInternal.tv_string,0), "workSpace", omniORB.tcInternal.tv_long, "loginTime", omniORB.typeMapping["IDL:USERtime:1.0"], "nativePrivileges", omniORB.typeMapping["IDL:USERcorbaStringSequence:1.0"], "receivedPrivs", omniORB.typeMapping["IDL:USERcorbaStringListMapSequence:1.0"], "donatedPrivs", omniORB.typeMapping["IDL:USERcorbaStringListMapSequence:1.0"])
_0__GlobalIDL._tc_USERcorbaActiveSessionDomainData = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_USERcorbaActiveSessionDomainData)
omniORB.registerType(USERcorbaActiveSessionDomainData._NP_RepositoryId, _0__GlobalIDL._d_USERcorbaActiveSessionDomainData, _0__GlobalIDL._tc_USERcorbaActiveSessionDomainData)
del USERcorbaActiveSessionDomainData

# typedef ... USERcorbaActiveSessionDomainDataSequence
class USERcorbaActiveSessionDomainDataSequence:
    _NP_RepositoryId = "IDL:USERcorbaActiveSessionDomainDataSequence:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.USERcorbaActiveSessionDomainDataSequence = USERcorbaActiveSessionDomainDataSequence
_0__GlobalIDL._d_USERcorbaActiveSessionDomainDataSequence  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:USERcorbaActiveSessionDomainData:1.0"], 0)
_0__GlobalIDL._ad_USERcorbaActiveSessionDomainDataSequence = (omniORB.tcInternal.tv_alias, USERcorbaActiveSessionDomainDataSequence._NP_RepositoryId, "USERcorbaActiveSessionDomainDataSequence", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:USERcorbaActiveSessionDomainData:1.0"], 0))
_0__GlobalIDL._tc_USERcorbaActiveSessionDomainDataSequence = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_USERcorbaActiveSessionDomainDataSequence)
omniORB.registerType(USERcorbaActiveSessionDomainDataSequence._NP_RepositoryId, _0__GlobalIDL._ad_USERcorbaActiveSessionDomainDataSequence, _0__GlobalIDL._tc_USERcorbaActiveSessionDomainDataSequence)
del USERcorbaActiveSessionDomainDataSequence

# struct USERcorbaActiveSessionData
_0__GlobalIDL.USERcorbaActiveSessionData = omniORB.newEmptyClass()
class USERcorbaActiveSessionData (omniORB.StructBase):
    _NP_RepositoryId = "IDL:USERcorbaActiveSessionData:1.0"

    def __init__(self, hostName, userName, domains):
        self.hostName = hostName
        self.userName = userName
        self.domains = domains

_0__GlobalIDL.USERcorbaActiveSessionData = USERcorbaActiveSessionData
_0__GlobalIDL._d_USERcorbaActiveSessionData  = (omniORB.tcInternal.tv_struct, USERcorbaActiveSessionData, USERcorbaActiveSessionData._NP_RepositoryId, "USERcorbaActiveSessionData", "hostName", (omniORB.tcInternal.tv_string,0), "userName", (omniORB.tcInternal.tv_string,0), "domains", omniORB.typeMapping["IDL:USERcorbaActiveSessionDomainDataSequence:1.0"])
_0__GlobalIDL._tc_USERcorbaActiveSessionData = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_USERcorbaActiveSessionData)
omniORB.registerType(USERcorbaActiveSessionData._NP_RepositoryId, _0__GlobalIDL._d_USERcorbaActiveSessionData, _0__GlobalIDL._tc_USERcorbaActiveSessionData)
del USERcorbaActiveSessionData

# typedef ... USERcorbaActiveSessionDataSequence
class USERcorbaActiveSessionDataSequence:
    _NP_RepositoryId = "IDL:USERcorbaActiveSessionDataSequence:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.USERcorbaActiveSessionDataSequence = USERcorbaActiveSessionDataSequence
_0__GlobalIDL._d_USERcorbaActiveSessionDataSequence  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:USERcorbaActiveSessionData:1.0"], 0)
_0__GlobalIDL._ad_USERcorbaActiveSessionDataSequence = (omniORB.tcInternal.tv_alias, USERcorbaActiveSessionDataSequence._NP_RepositoryId, "USERcorbaActiveSessionDataSequence", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:USERcorbaActiveSessionData:1.0"], 0))
_0__GlobalIDL._tc_USERcorbaActiveSessionDataSequence = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_USERcorbaActiveSessionDataSequence)
omniORB.registerType(USERcorbaActiveSessionDataSequence._NP_RepositoryId, _0__GlobalIDL._ad_USERcorbaActiveSessionDataSequence, _0__GlobalIDL._tc_USERcorbaActiveSessionDataSequence)
del USERcorbaActiveSessionDataSequence

# typedef ... USERcorbaSessionDataSequence
class USERcorbaSessionDataSequence:
    _NP_RepositoryId = "IDL:USERcorbaSessionDataSequence:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.USERcorbaSessionDataSequence = USERcorbaSessionDataSequence
_0__GlobalIDL._d_USERcorbaSessionDataSequence  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:USERcorbaSessionData:1.0"], 0)
_0__GlobalIDL._ad_USERcorbaSessionDataSequence = (omniORB.tcInternal.tv_alias, USERcorbaSessionDataSequence._NP_RepositoryId, "USERcorbaSessionDataSequence", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:USERcorbaSessionData:1.0"], 0))
_0__GlobalIDL._tc_USERcorbaSessionDataSequence = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_USERcorbaSessionDataSequence)
omniORB.registerType(USERcorbaSessionDataSequence._NP_RepositoryId, _0__GlobalIDL._ad_USERcorbaSessionDataSequence, _0__GlobalIDL._tc_USERcorbaSessionDataSequence)
del USERcorbaSessionDataSequence

# typedef ... USERcorbaPrivDataSequence
class USERcorbaPrivDataSequence:
    _NP_RepositoryId = "IDL:USERcorbaPrivDataSequence:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.USERcorbaPrivDataSequence = USERcorbaPrivDataSequence
_0__GlobalIDL._d_USERcorbaPrivDataSequence  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:USERcorbaCompletePrivData:1.0"], 0)
_0__GlobalIDL._ad_USERcorbaPrivDataSequence = (omniORB.tcInternal.tv_alias, USERcorbaPrivDataSequence._NP_RepositoryId, "USERcorbaPrivDataSequence", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:USERcorbaCompletePrivData:1.0"], 0))
_0__GlobalIDL._tc_USERcorbaPrivDataSequence = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_USERcorbaPrivDataSequence)
omniORB.registerType(USERcorbaPrivDataSequence._NP_RepositoryId, _0__GlobalIDL._ad_USERcorbaPrivDataSequence, _0__GlobalIDL._tc_USERcorbaPrivDataSequence)
del USERcorbaPrivDataSequence

# typedef ... USERcorbaProfileDataSequence
class USERcorbaProfileDataSequence:
    _NP_RepositoryId = "IDL:USERcorbaProfileDataSequence:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.USERcorbaProfileDataSequence = USERcorbaProfileDataSequence
_0__GlobalIDL._d_USERcorbaProfileDataSequence  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:USERcorbaCompleteProfileData:1.0"], 0)
_0__GlobalIDL._ad_USERcorbaProfileDataSequence = (omniORB.tcInternal.tv_alias, USERcorbaProfileDataSequence._NP_RepositoryId, "USERcorbaProfileDataSequence", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:USERcorbaCompleteProfileData:1.0"], 0))
_0__GlobalIDL._tc_USERcorbaProfileDataSequence = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_USERcorbaProfileDataSequence)
omniORB.registerType(USERcorbaProfileDataSequence._NP_RepositoryId, _0__GlobalIDL._ad_USERcorbaProfileDataSequence, _0__GlobalIDL._tc_USERcorbaProfileDataSequence)
del USERcorbaProfileDataSequence

#
# End of module "_GlobalIDL"
#
__name__ = "spell.lib.hifly.interface.USERcorbaTypes_idl"

_exported_modules = ( "spell.lib.hifly.interface._GlobalIDL", )

# The end.
