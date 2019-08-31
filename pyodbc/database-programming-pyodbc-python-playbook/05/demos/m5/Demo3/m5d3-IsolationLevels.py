import pyodbc

server = r'localhost\SQLEXPRESS'
database = 'WideWorldImporters'
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;APP=Pluralsight Course;'

#Establish connection
with pyodbc.connect(connectionString) as connection:
        cursor = connection.cursor()

        #query with SQL Server default
        tsqlquery = '''SELECT TOP 10 * FROM [Sales].[Invoices]'''
        cursor.execute(tsqlquery)
        cursor.commit()
        input('Press Enter to continue...')

        #change the isolation level through pyodbc
        connection.set_attr(pyodbc.SQL_ATTR_TXN_ISOLATION, pyodbc.SQL_TXN_REPEATABLE_READ)
        cursor.execute(tsqlquery)
        cursor.commit()
        input('Press Enter to continue...')

        #enable the isolation level through SQL
        connection.autocommit=True
        tsqlenablenewlevel = '''ALTER DATABASE [WideWorldImporters] 
                        SET ALLOW_SNAPSHOT_ISOLATION ON'''
        cursor.execute(tsqlenablenewlevel)

        #set the connection to use this new isolation level
        connection.autocommit=False
        tsqlsetnewlevel = '''SET TRANSACTION ISOLATION LEVEL SNAPSHOT'''
        cursor.execute(tsqlsetnewlevel)
        cursor.commit()
        cursor.execute(tsqlquery)
        cursor.commit()
        input('Press Enter to continue...')
        




