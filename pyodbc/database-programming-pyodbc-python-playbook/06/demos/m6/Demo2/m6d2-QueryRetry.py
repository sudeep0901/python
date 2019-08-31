import pyodbc
import sys
sys.path.append(sys.path[0]+'/../..')
import printFunctions as pf
import time

server = r'localhost\SQLEXPRESS'
database = 'WideWorldImporters'
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;APP=Pluralsight Course;'

def getAverageTaxRate(invoiceid, connection):
        tsql = '''SET LOCK_TIMEOUT 0
                  SELECT AVG(TaxRate) averageTaxRate 
                  FROM Sales.InvoiceLines
                  WHERE InvoiceID=?'''
        cursor = connection.cursor()
        cursor.execute(tsql,invoiceid)
        return cursor.fetchall()

def retryableOperation(maxattempts, operation, arguments):
        backoff = 1
        attempt = 1
        while True :
                try:
                        return operation(*arguments)
                except:
                        print("Operation failure, waiting: " + str(backoff) + " seconds...")
                        time.sleep(backoff)
                        backoff *= 2
                        attempt += 1
                        if attempt > maxattempts:
                                raise
        


#Establish connection
with pyodbc.connect(connectionString) as connection:

        #start SQL transaction and run this block
        try:
                rows = retryableOperation(3,getAverageTaxRate,[2,connection])
                pf.printResults(rows)
        except pyodbc.Error as pyodbcerror:
                print('Error: ' + str(pyodbcerror))        
        
        input('Press Enter to continue...')

        #Rollback the SQL transaction while this other block waits
        try:
                rows = retryableOperation(10,getAverageTaxRate,[2,connection])
                pf.printResults(rows)
        except pyodbc.Error as pyodbcerror:
                print('Error: ' + str(pyodbcerror))        
        
        input('Press Enter to continue...')



