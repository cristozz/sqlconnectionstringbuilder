# Copyright (c) 2022  ttchristofer@gmail.com
# Distributed under the terms of the Modified BSD License.

TRUSTED_CONN_YES_VALUE = "YES"
TRUSTED_CONN_NO_VALUE = "NO"
TRUSTED_CONN_VALUES_SUPPORTED = [TRUSTED_CONN_YES_VALUE, TRUSTED_CONN_NO_VALUE]

SQLCONNBUILDER_CONNSTRING_PARAM = 'ConnectionString'


from enum import Enum

class ConnParamKeywords(str,Enum):
    DRIVER = 'Driver'
    SERVER = 'Server'
    DATABASE = 'DataBase'
    UID = 'User'
    PWD = 'Password'
    TRUSTED_CONNECTION = 'Trusted_Connection'
    APP = 'Application_Name'

    def __str__(self):
        return '%s' % self.value