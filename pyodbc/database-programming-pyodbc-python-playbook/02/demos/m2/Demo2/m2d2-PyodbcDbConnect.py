import pyodbc
server = r'localhost\SQLEXPRESS'
database = 'WideWorldImporters'
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server + \
    ';DATABASE='+database+';Trusted_Connection=yes;APP=Pluralsight Course;'
# Connection #1
connection = pyodbc.connect(connectionString)

print('Connection Attributes:')
print('Autocommit: ' + str(connection.autocommit))
print('Timeout: ' + str(connection.timeout))

input('Press Enter to continue...')

connection.close()

# Connection #2 overriding odbc timeout
try:
    with pyodbc.connect(connectionString, timeout=5) as connection:
        print('Connection did not time out')
except:
    print('Connection timed out')
finally:
    input('Press Enter to continue...')

# Connection #3 using ODBC constants for advanced changes
# SQL Log is written in %TEMP% Folder named SQL.LOG
SQL_ATTR_TRACE = 104
SQL_ATTR_PACKET_SIZE = 112
with pyodbc.connect(connectionString, attrs_before={SQL_ATTR_TRACE: 1,
                                                    SQL_ATTR_PACKET_SIZE: 1024 * 32}) as connection:
    input('Press Enter to continue...')
