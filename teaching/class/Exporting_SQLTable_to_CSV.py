import psycopg2
import pandas as pd
import sys
import saspy

# Exporting Table to CSV

def table_to_csv(sql, file_path, dbname, host, port, user, pwd):
    '''
    This function creates a csv file from PostgreSQL with query
    '''
    try:
        conn = psycopg2.connect(dbname=dbname, host=host, port=port,\
         user=user, password=pwd)
        print("Connecting to Database")
        # Get data into pandas dataframe
        df = pd.read_sql(sql, conn)
        # Write to csv file
        df.to_csv(file_path, encoding='utf-8', header = True,\
         doublequote = True, sep=',', index=False)
        print("CSV File has been created")
        conn.close()

    except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)

# Execution Example with develop table

sql = 'Select * From develop'
file_path = 'develop_table.csv'
dbname = 'xoriant'
host = 'localhost'
port = '5432'
user = 'postgres'
pwd = 'xoriant@123'

table_to_csv(sql, file_path, dbname, host, port, user, pwd)











