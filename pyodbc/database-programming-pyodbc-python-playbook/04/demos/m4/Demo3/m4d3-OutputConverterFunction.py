import struct
import pyodbc
import sys
sys.path.append(sys.path[0]+'/../..')
import printFunctions as pf

## Credit to the Pyodbc developers for the conversion function!
def handle_datetimeoffset(dto_value):
    # ref: https://github.com/mkleehammer/pyodbc/issues/134#issuecomment-281739794
    tup = struct.unpack("<6hI2h", dto_value)  # e.g., (2017, 3, 16, 10, 35, 18, 0, -6, 0)
    tweaked = [tup[i] // 100 if i == 6 else tup[i] for i in range(len(tup))]
    return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}.{:07d} {:+03d}:{:02d}".format(*tweaked)

server = r'localhost\SQLEXPRESS'
database = 'WideWorldImporters'
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;APP=Pluralsight Course;'

#Establish connection
with pyodbc.connect(connectionString) as connection:
        cursor = connection.cursor()
        
        tsql = '''SELECT TOP 5 InvoiceDate, DeliveryInstructions, 
                ToDateTimeOffset(ConfirmedDeliveryTime,120) ConfirmedDateTimeOffset
                FROM [Sales].[Invoices]
                ORDER BY ConfirmedDeliveryTime DESC'''

        #no conversion
        cursor.execute(tsql)
        try:
                rows = cursor.fetchall()
        except pyodbc.Error as pyodbcerror:
                print('Error: ' + str(pyodbcerror))

        input('Press Enter to continue...')

        #with conversion
        connection.add_output_converter(-155, handle_datetimeoffset)
        cursor.execute(tsql)
        rows = cursor.fetchall()
        pf.printResultsInfo(cursor)
        pf.printResults(rows)

        connection.clear_output_converters()
        input('Press Enter to continue...')
        





        



