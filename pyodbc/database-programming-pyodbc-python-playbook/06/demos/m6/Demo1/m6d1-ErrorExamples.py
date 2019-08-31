import pyodbc

server = r'localhost\SQLEXPRESS'
database = 'WideWorldImporters'
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;APP=Pluralsight Course;'

#Establish connection
#Stop SQL Server
print('Establishing Connection...')
try:
        connection  = pyodbc.connect(connectionString)
except pyodbc.OperationalError as pyodbcerror:
        print('Error: ' + str(pyodbcerror))
        
input('Press Enter to continue...')

#Start SQL Server
connection = pyodbc.connect(connectionString)
cursor = connection.cursor()

#Disconnect
#Stop SQL Server while the WAITFOR is running
print('Disconnect Example...')
tsql = "WAITFOR DELAY '00:00:30';"

try:
        cursor.execute(tsql)
        rows = cursor.fetchall()
except pyodbc.Error as pyodbcerror:
        print('Error: ' + str(pyodbcerror))
        connection.close()

input('Press Enter to continue...')

#Start SQL Server
connection = pyodbc.connect(connectionString)
cursor = connection.cursor()

#Integrity
print('Integrity Example...')
tsql = '''UPDATE [Application].[Countries]
        SET [CountryID] = (SELECT CountryID FROM [Application].[Countries]
        WHERE CountryName='Costa Rica')
        WHERE CountryName='Canada';'''

try:
        cursor.execute(tsql)
        rows = cursor.fetchall()
except pyodbc.IntegrityError as pyodbcerror:
        print('Error: ' + str(pyodbcerror))

input('Press Enter to continue...')

#Data Error
print('Data Error Example...')
tsql = 'SELECT cast(100000000000000000000 AS int)'

try:
        cursor.execute(tsql)
        rows = cursor.fetchall()
except pyodbc.DataError as pyodbcerror:
        print('Error: ' + str(pyodbcerror))

input('Press Enter to continue...')


