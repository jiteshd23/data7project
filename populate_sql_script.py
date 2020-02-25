import sqlalchemy
import urllib

class SQLConnect:
    def __init__(self):
        server = 'localhost, 1433'
        database = 'AWS'
        username = 'SA'
        password = 'Passw0rd2018'
        self.quoted = urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};''SERVER='+server+';''DATABASE='+database+';''UID='+username+';PWD='+password)
        self.engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(self.quoted))

    def import_sql(self, db, sql_table_name):
        db.to_sql(sql_table_name, con = self.engine, if_exists='append', index=False)

