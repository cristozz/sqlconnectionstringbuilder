from sqlconnstrbuilder.utils.constants import ConnParamKeywords, TRUSTED_CONN_NO_VALUE, TRUSTED_CONN_YES_VALUE, SQLCONNBUILDER_CONNSTRING_PARAM

class SqlConnectionStringBuilder:

    Driver:str
    Server:str 
    Database:str 
    User:str
    Password:str
    Trusted_connection:bool
    Application_Name:str = ''

    def __init__(self, **kwargs):
        """
        Two-dimensional, size-mutable, potentially heterogeneous tabular data.
        Data structure also contains labeled axes (rows and columns).
        Arithmetic operations align on both row and column labels. Can be
        thought of as a dict-like container for Series objects. The primary
        pandas data structure.
        Parameters
        ----------
        Driver : str, default None
            Driver name to be used, without brackets.
        Server : str, default None
            Server name or IP to be used.
        DataBase : str, default None
            Database to be used.
        User : str, default None
            If Trusted_Connection is True, this param has to be specified.
            If Trusted_Connection is False, although the field is specified it will not be used in the connection.
        Password : str, default None
            If Trusted_Connection is True, this param has to be specified.
            If Trusted_Connection is False, although the field is specified it will not be used in the connection.
        Trusted_Connection : bool, default None
            A Trusted connection means Windows Authentication (i.e. a Windows login). 
            SQL Server has two Authentication modes: Mixed and Windows Authentication Mode. 
            Mixed has the option of SQL server logins (username and password) and Windows Authentication.
        Application_Name : str, default None
            Always Include the optional Application Name parameter in your connection strings when connecting to SQL Server.
            This way the SQL Server will have info on what application is using the connection. 
            This can be invaluable info when locating errors in the database server.
        Examples
        --------
        Constructing SqlConnectionStringBuilder from params.
        >>> sqlconn = SqlConnectionStringBuilder(
            Driver = 'ODBC Driver 17 for SQL Server', 
            Server = 'BTBBID10', 
            Database = 'BD_ODS_STAGEBCP', 
            Trusted_Connection = True)
        >>> connstring = sqlconn.ConnectionString
        >>> connstring
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=BTBBID10;DATABASE=BD_ODS_STAGEBCP;TRUSTED_CONNECTION=YES'
        >>> sqlconn.Server = 'DEVTST00'
        >>> sqlconn.ConnectionString
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DEVTST00;DATABASE=BD_ODS_STAGEBCP;TRUSTED_CONNECTION=YES'
        Constructing SqlConnectionStringBuilder from a connection string:
        >>> sqlconn = SqlConnectionStringBuilder(
            ConnectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=BTBBID10;DATABASE=BD_ODS_STAGEBCP;TRUSTED_CONNECTION=YES')
        >>> sqlconn.Driver
        'ODBC Driver 17 for SQL Server'
        >>> sqlconn.Server
        'BTBBID10'
        >>> sqlconn.Database
        'BD_ODS_STAGEBCP'
        >>> sqlconn.Trusted_Connection
        True
        >>> sqlconn.Server = 'DEVTST00'
        >>> sqlconn.ConnectionString
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DEVTST00;DATABASE=BD_ODS_STAGEBCP;TRUSTED_CONNECTION=YES'
        """
        self.Driver = kwargs.get(ConnParamKeywords.DRIVER.value, None)
        self.Server = kwargs.get(ConnParamKeywords.SERVER.value, None)
        self.Database = kwargs.get(ConnParamKeywords.DATABASE.value, None)
        self.User = kwargs.get(ConnParamKeywords.UID.value, None)
        self.Password = kwargs.get(ConnParamKeywords.PWD.value, None)
        self.Trusted_Connection = kwargs.get(ConnParamKeywords.TRUSTED_CONNECTION.value, None)
        self.Application_Name = kwargs.get(ConnParamKeywords.APP.value, None)

        self.__connectionstring = kwargs.get(SQLCONNBUILDER_CONNSTRING_PARAM, '')

    @property
    def ConnectionString(self) -> str:
        self.__buildConnectionString()
        return self.__connectionstring

    @ConnectionString.setter
    def ConnectionString(self, var):
        self.__connectionstring = var

        connstring_dict = dict((k.upper(), v) for k, v in dict(param.split("=") for param in var.split(";") if len(param)==2).items())
        
        self.Application_Name = connstring_dict[ConnParamKeywords.APP.name] if ConnParamKeywords.APP.name in connstring_dict else self.Application_Name
        self.Driver = connstring_dict[ConnParamKeywords.DRIVER.name] if ConnParamKeywords.DRIVER.name in connstring_dict else self.Driver
        self.Server = connstring_dict[ConnParamKeywords.SERVER.name] if ConnParamKeywords.SERVER.name in connstring_dict else self.Server
        self.Database = connstring_dict[ConnParamKeywords.DATABASE.name] if ConnParamKeywords.DATABASE.name in connstring_dict else self.Database
        self.User = connstring_dict[ConnParamKeywords.UID.name] if ConnParamKeywords.UID.name in connstring_dict else self.User
        self.Password = connstring_dict[ConnParamKeywords.PWD.name] if ConnParamKeywords.PWD.name in connstring_dict else self.Password
        self.Trusted_Connection = connstring_dict[ConnParamKeywords.TRUSTED_CONNECTION.name].upper() == TRUSTED_CONN_YES_VALUE if ConnParamKeywords.TRUSTED_CONNECTION.name in connstring_dict else self.Trusted_Connection

    def __buildConnectionString(self) -> str:
        self.ConnectionString = ';'.join(filter(None,[
            None if not self.Driver else f'{ConnParamKeywords.DRIVER.name}={{{self.Driver}}}',
            None if not self.Application_Name else f'{ConnParamKeywords.APP.name}={self.Application_Name}',
            None if not self.Server else f'{ConnParamKeywords.SERVER.name}={self.Server}' ,
            None if not self.Database else f'{ConnParamKeywords.DATABASE.name}={self.Database}',
            None if not self.Trusted_Connection else f"{ConnParamKeywords.TRUSTED_CONNECTION.name}={TRUSTED_CONN_YES_VALUE if self.Trusted_Connection else TRUSTED_CONN_NO_VALUE}", 
            None if not self.User and not self.Trusted_Connection else (f'{ConnParamKeywords.UID.name}={self.User}' if not self.Trusted_Connection else None),
            None if not self.Password and not self.Trusted_Connection else f'{ConnParamKeywords.PWD.name}={self.Password}' if not self.Trusted_Connection else None,
        ]))