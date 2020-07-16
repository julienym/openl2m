#
# This file is part of Open Layer 2 Management (OpenL2M).
#
# OpenL2M is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License version 3 as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.  You should have received a copy of the GNU General Public
# License along with OpenL2M. If not, see <http://www.gnu.org/licenses/>.
#
# SNMP constants, v1 not supported!
SNMP_VERSION_2C = 2
SNMP_VERSION_3 = 3
SNMP_VERSION_CHOICES = (
    (SNMP_VERSION_2C, '2c'),
    (SNMP_VERSION_3, '3'),
)

SNMP_V3_AUTH_NONE = 0
SNMP_V3_AUTH_MD5 = 1
SNMP_V3_AUTH_SHA = 2
SNMP_V3_AUTH_CHOICES = (
    (SNMP_V3_AUTH_NONE, 'none'),
    (SNMP_V3_AUTH_MD5, 'MD5'),
    (SNMP_V3_AUTH_SHA, 'SHA'),
)

SNMP_V3_PRIV_NONE = 0
SNMP_V3_PRIV_DES = 1
# SNMP_V3_PRIV_3DES = 2
SNMP_V3_PRIV_AES = 3
SNMP_V3_PRIV_CHOICES = (
    (SNMP_V3_PRIV_NONE, 'none'),
    (SNMP_V3_PRIV_DES, 'DES'),
    (SNMP_V3_PRIV_AES, 'AES'),
)

SNMP_V3_SECURITY_NOAUTH_NOPRIV = 0
SNMP_V3_SECURITY_AUTH_NOPRIV = 1
SNMP_V3_SECURITY_AUTH_PRIV = 2
SNMP_V3_SECURITY_CHOICES = (
    (SNMP_V3_SECURITY_NOAUTH_NOPRIV, 'NoAuth-NoPriv'),
    (SNMP_V3_SECURITY_AUTH_NOPRIV, 'Auth-NoPriv'),
    (SNMP_V3_SECURITY_AUTH_PRIV, 'Auth-Priv'),
)

SNMP_TIMEOUT = 5000
SNMP_RETRIES = 3
SNMP_MAXREPITITIONS = 25

# Switch default views
SWITCH_VIEW_BASIC = 0
SWITCH_VIEW_DETAILS = 1
SWITCH_VIEW_CHOICES = [
    [SWITCH_VIEW_BASIC, 'Basic'],
    [SWITCH_VIEW_DETAILS, 'Details'],
]

# Switch statuses
SWITCH_STATUS_OFFLINE = 0
SWITCH_STATUS_ACTIVE = 1
SWITCH_STATUS_PLANNED = 2
SWITCH_STATUS_STAGED = 3
SWITCH_STATUS_FAILED = 4
SWITCH_STATUS_INVENTORY = 5
SWITCH_STATUS_DECOMMISSIONING = 6
SWITCH_STATUS_CHOICES = [
    [SWITCH_STATUS_ACTIVE, 'Active'],
    [SWITCH_STATUS_OFFLINE, 'Offline'],
    [SWITCH_STATUS_PLANNED, 'Planned'],
    [SWITCH_STATUS_STAGED, 'Staged'],
    [SWITCH_STATUS_FAILED, 'Failed'],
    [SWITCH_STATUS_INVENTORY, 'Inventory'],
    [SWITCH_STATUS_DECOMMISSIONING, 'Decommissioning'],
]

# Switch capabilities. This is a bit map.
# Specific bits if set indicate a certain MIB is supported.
CAPABILITIES_NONE = 0x0
CAPABILITIES_IF_MIB = 0x00000001          # 1 the newer IF-MIB spec
CAPABILITIES_QBRIDGE_MIB = 0x00000002     # 2
CAPABILITIES_NET2MEDIA_MIB = 0x00000004   # 4 old ARP mib
CAPABILITIES_POE_MIB = 0x00000010         # 8
CAPABILITIES_LLDP_MIB = 0x00000020        # 16
CAPABILITIES_NET2PHYS_MIB = 0x00000040    # 32 new ARP mib :-)
# vendor specific mib
# Cisco
CAPABILITIES_CISCO_VTP_MIB = 0x00010000
CAPABILITIES_CISCO_POE_MIB = 0x00020000
CAPABILITIES_CISCO_STACK_MIB = 0x00040000


CMD_TYPE_GLOBAL = 0
CMD_TYPE_INTERFACE = 1
CMD_TYPE_CHOICES = [
    [CMD_TYPE_GLOBAL, 'Global'],
    [CMD_TYPE_INTERFACE, 'Interface'],
]

BULKEDIT_POE_NONE = 0
BULKEDIT_POE_CHANGE = 1
BULKEDIT_POE_DOWN_UP = 2
BULKEDIT_POE_DOWN = 3
BULKEDIT_POE_UP = 4
BULKEDIT_POE_CHOICES = [
    [BULKEDIT_POE_NONE, 'No Change'],
    [BULKEDIT_POE_CHANGE, 'PoE Change'],
    [BULKEDIT_POE_DOWN_UP, 'PoE Down/Up'],
    [BULKEDIT_POE_DOWN, 'PoE Disable'],
    [BULKEDIT_POE_UP, 'PoE Enable'],
]

# Types of log entries
LOG_TYPE_VIEW = 0
LOG_TYPE_CHANGE = 1
LOG_TYPE_WARNING = 2
LOG_TYPE_ERROR = 3
LOG_TYPE_COMMAND = 4
LOG_TYPE_LOGIN_OUT = 5
LOG_TYPE_CHOICES = [
    [LOG_TYPE_VIEW, 'View'],
    [LOG_TYPE_CHANGE, 'Change'],
    [LOG_TYPE_WARNING, 'Warning'],
    [LOG_TYPE_ERROR, 'Error'],
    [LOG_TYPE_COMMAND, 'Command'],
    [LOG_TYPE_LOGIN_OUT, 'Login/out'],
]

# Actions to log
LOG_VIEW_SWITCHGROUPS = 0
LOG_VIEW_SWITCH = 1
LOG_VIEW_INTERFACE = 2
LOG_VIEW_POE = 3
LOG_VIEW_VLANS = 4
LOG_VIEW_LLDP = 5
LOG_VIEW_ALL_LOGS = 6
LOG_VIEW_ADMIN_STATS = 7
LOG_VIEW_TASKS = 8
LOG_VIEW_TASK_DETAILS = 9
LOG_VIEW_SWITCH_SEARCH = 10
LOG_LOGIN = 90
LOG_LOGOUT = 91
LOG_LOGOUT_INACTIVE = 92
LOG_LOGIN_FAILED = 93
LOG_RELOAD_SWITCH = 100
LOG_NEW_OID_FOUND = 101
LOG_NEW_HOSTNAME_FOUND = 102
LOG_CHANGE_INTERFACE_DOWN = 103
LOG_CHANGE_INTERFACE_UP = 104
LOG_CHANGE_INTERFACE_TOGGLE_DOWN_UP = 105
LOG_CHANGE_INTERFACE_POE_DOWN = 106
LOG_CHANGE_INTERFACE_POE_UP = 107
LOG_CHANGE_INTERFACE_POE_TOGGLE_DOWN_UP = 108
LOG_CHANGE_INTERFACE_PVID = 109
LOG_CHANGE_INTERFACE_ALIAS = 110
LOG_SAVE_SWITCH = 111
LOG_EXECUTE_COMMAND = 112
LOG_PORT_POE_FAULT = 113
LOG_LDAP_CREATE_GROUP = 114
LOG_CHANGE_BULK_EDIT = 115
LOG_BULK_EDIT_TASK_SUBMIT = 116
LOG_BULK_EDIT_TASK_START = 117
LOG_BULK_EDIT_TASK_END_OK = 118
LOG_BULK_EDIT_TASK_END_ERROR = 119
LOG_TASK_DELETE = 120
LOG_TASK_TERMINATE = 121
LOG_EMAIL_SENT = 122

LOG_UNDEFINED_VLAN = 256
LOG_VLAN_NAME_MISMATCH = 257
LOG_WARNING_SNMP_ERROR = 258
LOG_LDAP_ERROR_USER_TO_GROUP = 259
LOG_LDAP_ERROR_CREATE_GROUP = 260
LOG_BULK_EDIT_TASK_ERROR = 261
LOG_EMAIL_ERROR = 262

LOG_DENIED = 512

# nice descriptions of the various log entries
LOG_ACTION_CHOICES = [
    [LOG_VIEW_SWITCHGROUPS, 'View Switch Groups'],
    [LOG_VIEW_SWITCH, 'View Switch'],
    [LOG_VIEW_INTERFACE, 'View Interface'],
    [LOG_VIEW_POE, 'View PoE'],
    [LOG_VIEW_VLANS, 'View Vlans'],
    [LOG_VIEW_LLDP, 'View LLDP'],
    [LOG_VIEW_ALL_LOGS, 'Viewing All Logs'],
    [LOG_VIEW_ADMIN_STATS, 'Viewing Site Statistics'],
    [LOG_VIEW_TASKS, 'Viewing Tasks'],
    [LOG_VIEW_TASK_DETAILS, 'Viewing Task Details'],
    [LOG_VIEW_SWITCH_SEARCH, 'Searching for Switch Name'],
    [LOG_RELOAD_SWITCH, 'Reloading Switch Data'],
    [LOG_NEW_OID_FOUND, 'New System ObjectID Found'],
    [LOG_NEW_HOSTNAME_FOUND, 'New System Name Found'],
    [LOG_LOGIN, 'Login'],
    [LOG_LOGOUT, 'Logout'],
    [LOG_LOGOUT_INACTIVE, 'Inactivity Logout'],
    [LOG_LOGIN_FAILED, 'Login Failed'],
    [LOG_CHANGE_INTERFACE_DOWN, 'Interface Disable'],
    [LOG_CHANGE_INTERFACE_UP, 'Interface Enable'],
    [LOG_CHANGE_INTERFACE_TOGGLE_DOWN_UP, 'Interface Toggle'],
    [LOG_CHANGE_INTERFACE_POE_DOWN, 'Interface PoE Disable'],
    [LOG_CHANGE_INTERFACE_POE_UP, 'Interface PoE Enable'],
    [LOG_CHANGE_INTERFACE_POE_TOGGLE_DOWN_UP, 'Interface PoE Toggle'],
    [LOG_CHANGE_INTERFACE_PVID, 'Interface PVID Vlan Change'],
    [LOG_CHANGE_INTERFACE_ALIAS, 'Interface Description Change'],
    [LOG_SAVE_SWITCH, 'Saving Configuration'],
    [LOG_EXECUTE_COMMAND, 'Execute Command'],
    [LOG_PORT_POE_FAULT, 'Port PoE Fault'],
    [LOG_LDAP_CREATE_GROUP, 'LDAP New SwitchGroup'],
    [LOG_CHANGE_BULK_EDIT, 'Bulk Edit'],
    [LOG_BULK_EDIT_TASK_SUBMIT, 'Bulk Edit Task Submit'],
    [LOG_BULK_EDIT_TASK_START, 'Bulk Edit Task Started'],
    [LOG_BULK_EDIT_TASK_END_OK, 'Bulk Edit Task Ended OK'],
    [LOG_BULK_EDIT_TASK_END_ERROR, 'Bulk Edit Task Ended With Errors'],
    [LOG_TASK_DELETE, 'Task Deleted'],
    [LOG_TASK_TERMINATE, 'Task Terminated'],
    [LOG_EMAIL_SENT, 'Email Sent'],
    [LOG_UNDEFINED_VLAN, 'Undefined Vlan'],
    [LOG_VLAN_NAME_MISMATCH, 'Vlan Name Mismatch'],
    [LOG_WARNING_SNMP_ERROR, 'SNMP Error'],
    [LOG_LDAP_ERROR_USER_TO_GROUP, 'LDAP User->SwitchGroup Error'],
    [LOG_LDAP_ERROR_CREATE_GROUP, 'LDAP SwitchGroup Error'],
    [LOG_BULK_EDIT_TASK_ERROR, 'Bulk Edit Job Start Error'],
    [LOG_EMAIL_ERROR, 'Email Error'],
]

# tasks related constants
TASK_TYPE_NONE = 0
TASK_TYPE_BULKEDIT = 1

TASK_TYPE_CHOICES = [
    [TASK_TYPE_NONE, 'No task'],
    [TASK_TYPE_BULKEDIT, 'Bulk Edit Task'],
]

TASK_STATUS_DELETED = 0
TASK_STATUS_CREATED = 1
TASK_STATUS_SCHEDULED = 2
TASK_STATUS_RUNNING = 3
TASK_STATUS_COMPLETED = 4
TASK_STATUS_ERROR = 5
TASK_STATUS_RUNNING_RETRY = 6

TASK_STATUS_CHOICES = [
    [TASK_STATUS_DELETED, 'Deleted'],
    [TASK_STATUS_CREATED, 'Created'],
    [TASK_STATUS_SCHEDULED, 'Scheduled'],
    [TASK_STATUS_RUNNING, 'Running'],
    [TASK_STATUS_COMPLETED, 'Completed'],
    [TASK_STATUS_ERROR, 'Errored'],
    [TASK_STATUS_RUNNING_RETRY, 'Running(Retry)'],
]


# Ethernet formats
ETH_FORMAT_COLON = 0    # aa:bb:cc:dd:ee:ff
ETH_FORMAT_HYPHEN = 1   # aa-bb-cc-dd-ee-ff
ETH_FORMAT_CISCO = 2    # aabb.ccdd.eeff
