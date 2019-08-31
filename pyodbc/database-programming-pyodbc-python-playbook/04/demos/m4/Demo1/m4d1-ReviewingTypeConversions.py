import pyodbc

server = r'localhost\SQLEXPRESS'
database = 'WideWorldImporters'
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;APP=Pluralsight Course;'

#Establish connection
with pyodbc.connect(connectionString) as connection:
        cursor = connection.cursor()
        #bool to bit
        tsqlparam = '''--bool to bit
                SELECT count(*) FROM Application.People
                WHERE IsPermittedToLogon=?'''
        parameter = False
        cursor.execute(tsqlparam,parameter)
        print('Result: ' + str(cursor.fetchval()))
        input('Press Enter to continue...')

        #Unicode to Varchar
        cursor.setinputsizes([(pyodbc.SQL_VARCHAR, 50, 0)])
        tsqlparamsized = '''--unicode to varchar
                SELECT TOP 10 cities.CityID, cities.CityName, cities.LatestRecordedPopulation,sprovs.StateProvinceName
                FROM Application.Cities cities 
                INNER JOIN Application.StateProvinces sprovs
                ON cities.StateProvinceID=sprovs.StateProvinceID
                WHERE StateProvinceName = ?
                AND cities.LatestRecordedPopulation IS NOT NULL
                ORDER BY cities.LatestRecordedPopulation DESC;'''
        state1 = 'California'
        cursor.execute(tsqlparamsized,state1)
        input('Press Enter to continue...')

        #XML to Python string
        tsqlparamsized = '''--XML to str
                SELECT TOP 3 cities.CityID, cities.CityName, cities.LatestRecordedPopulation,sprovs.StateProvinceName
                FROM Application.Cities cities 
                INNER JOIN Application.StateProvinces sprovs
                ON cities.StateProvinceID=sprovs.StateProvinceID
                WHERE StateProvinceName = ?
                AND cities.LatestRecordedPopulation IS NOT NULL
                ORDER BY cities.LatestRecordedPopulation DESC
                FOR XML AUTO;'''
        state1 = 'California'
        cursor.execute(tsqlparamsized,state1)
        result = cursor.fetchval()
        print('Result Type: ' + str(type(result)))
        print('Result: ' + result)
        input('Press Enter to continue...')





        



