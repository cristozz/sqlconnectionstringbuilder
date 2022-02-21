# SqlConnectionStringBuilder for python

[![BSD License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg?style=flat-square)](https://opensource.org/licenses/BSD-3-Clause)
[![PyPI](https://img.shields.io/pypi/v/sqlconnstrbuilder?color=brightgreen)](https://pypi.org/project/sqlconnstrbuilder/1.0.4/)




sqlconnstrbuilder is an open source Python module that makes create a ODBC connection string simple.

The easiest way to install is to use pip:

    pip install sqlconnstrbuilder

## How to Use

A simple example:

``` Python

from sqlconnstrbuilder import SqlConnectionStringBuilder

sqlConnBuilder = SqlConnectionStringBuilder(
    Driver = 'ODBC Driver 17 for SQL Server',
    Server = 'DEVTST00',
    Trusted_Connection = True)

conns = {}

sqlConnBuilder.Database = 'MylocalDB'
conns['CONN_STRG_1'] = sqlConnBuilder.ConnectionString
sqlConnBuilder.Server = 'DEVTST01'
sqlConnBuilder.Database = 'MylocalDB_2'
conns['CONN_STRG_2'] = sqlConnBuilder.ConnectionString
sqlConnBuilder.Trusted_Connection = False
sqlConnBuilder.User = 'MyUser'
sqlConnBuilder.Password = 'MyFu**ingPass'
conns['CONN_STRG_3'] = sqlConnBuilder.ConnectionString

print(conns)
``` 

Output

```bash
{'CONN_STRG_1': 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DEVTST00;DATABASE=MylocalDB;TRUSTED_CONNECTION=YES',
 'CONN_STRG_2': 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DEVTST01;DATABASE=MylocalDB_2;TRUSTED_CONNECTION=YES',
 'CONN_STRG_3': 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DEVTST01;DATABASE=MylocalDB_2;UID=MyUser;PWD=MyFu**ingPass'}
```

A example from connection string:

``` Python

from sqlconnstrbuilder import SqlConnectionStringBuilder

sqlConnBuilder = SqlConnectionStringBuilder(ConnectionString='DRIVER={ODBC Driver 17 for SQL Server};SERVER=DEVTST00;DATABASE=MylocalDB;TRUSTED_CONNECTION=YES')

conns = {}

conns['CONN_STRG_1'] = sqlConnBuilder.ConnectionString
sqlConnBuilder.Server = 'DEVTST01'
sqlConnBuilder.Database = 'MylocalDB_2'
conns['CONN_STRG_2'] = sqlConnBuilder.ConnectionString

print(conns)
``` 

Output

```bash
{'CONN_STRG_1': 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DEVTST00;DATABASE=MylocalDB;TRUSTED_CONNECTION=YES',
 'CONN_STRG_2': 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DEVTST01;DATABASE=MylocalDB_2;TRUSTED_CONNECTION=YES'}
```


See the [docs](https://github.com/cristozz/sqlconnectionstringbuilder/wiki/Install) for details.

[Documentation](https://github.com/cristozz/sqlconnectionstringbuilder/wiki)

[Release Notes](https://github.com/cristozz/sqlconnectionstringbuilder/releases)