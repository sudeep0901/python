import pyodbc

server = r'localhost\SQLEXPRESS'
database = 'WideWorldImporters'
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;APP=Pluralsight Course;'

#Establish connection
with pyodbc.connect(connectionString) as connection:
        cursor = connection.cursor()
        #autocommit False by default
        print('Autocommit: ' + str(connection.autocommit))

        tsqlcreatetable = '''CREATE TABLE [Sales].[SpecialDeals-Copy1](
                [SpecialDealID] [int] NOT NULL,
	        [StockItemID] [int] NULL,
	        [CustomerID] [int] NULL,
	        [BuyingGroupID] [int] NULL
	        )'''
        
        tsqlpopulatetable = '''
                INSERT INTO [Sales].[SpecialDeals-Copy1]
                SELECT [SpecialDealID],[StockItemID],[CustomerID],[BuyingGroupID]
                FROM
                [Sales].[SpecialDeals] ORDER BY DiscountPercentage DESC'''

        cursor.execute(tsqlcreatetable)
        input('Press Enter to continue...')
        cursor.execute(tsqlpopulatetable)
        input('Press Enter to continue...')
        connection.rollback()
        input('Press Enter to continue...')
        

        #autocommit set to True
        connection.autocommit=True
        print('Autocommit: ' + str(connection.autocommit))

        #same commands but with Autocommit set to True

        cursor.execute(tsqlcreatetable)
        input('Press Enter to continue...')
        cursor.execute(tsqlpopulatetable)
        input('Press Enter to continue...')
        connection.rollback()
        input('Press Enter to continue...')

        #drop the table
        tsqldroptable = 'DROP TABLE [Sales].[SpecialDeals-Copy1]'
        cursor.execute(tsqldroptable)
        input('Press Enter to continue...')
        connection.rollback()
        input('Press Enter to continue...')



