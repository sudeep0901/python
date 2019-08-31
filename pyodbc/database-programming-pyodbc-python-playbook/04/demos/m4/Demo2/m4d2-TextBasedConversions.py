import pyodbc
import sys
sys.path.append(sys.path[0]+'/../..')
import printFunctions as pf

server = r'localhost\SQLEXPRESS'
database = 'WideWorldImporters'
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;APP=Pluralsight Course;'

#Establish connection
with pyodbc.connect(connectionString) as connection:
        cursor = connection.cursor()
        #no conversion
        tsql = '''--no conversion
                SELECT SupplierName, DeliveryLocation
                FROM [Website].[Suppliers]'''
        cursor.execute(tsql)
        try:
                rows = cursor.fetchall()
        except pyodbc.Error as pyodbcerror:
                print('Error: ' + str(pyodbcerror))

        input('Press Enter to continue...')

        #with conversion
        tsql = '''--with conversion
                SELECT SupplierName, DeliveryLocation.STAsText()
                FROM [Website].[Suppliers]'''
        cursor.execute(tsql)
        rows = cursor.fetchall()
        pf.printResultsInfo(cursor)
        pf.printResults(rows)

        input('Press Enter to continue...')
        





        



