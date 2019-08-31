import pyodbc

server = r'localhost\SQLEXPRESS'
database = 'WideWorldImporters'
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;APP=Pluralsight Course;'

#Establish connection
with pyodbc.connect(connectionString) as connection:
        cursor1 = connection.cursor()
        cursor2 = connection.cursor()
        #autocommit False by default
        print('Autocommit: ' + str(connection.autocommit))

        tsqlcommand1 = '''SELECT * INTO Application.PeopleBackup
                        FROM Application.People'''
        
        tsqlcommand2 = '''SELECT * INTO Application.CountriesBackup
                        FROM Application.Countries'''

        cursor1.execute(tsqlcommand1)
        input('Press Enter to continue...')
        cursor2.execute(tsqlcommand2)
        input('Press Enter to continue...')
        cursor1.commit()
        input('Press Enter to continue...')
        




