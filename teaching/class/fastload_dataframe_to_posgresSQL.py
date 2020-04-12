import pandas as pd
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from io import StringIO
import time

# Execution Example
# file_path = 'transaction.csv'
# table_name = 'develop_load'
# schema  = 'public'
# dbname = 'xoriant'
# host = 'localhost'
# port = '5432'
# user = 'postgres'
# pwd = 'xoriant@123'

def df_to_database(engine, df, schema, table_name, if_exists='replace'):
    # Writing Dataframe to PostgreSQL and replacing table if it already exists
    df.to_sql(table_name, engine, if_exists=if_exists, index=False, schema=schema)
    # df.to_sql(name='helloworld', con=engine, if_exists = 'replace', index=False)

def df_to_csv_to_sql(output, engine, df, schema, table_name, if_exists='replace', sep='\x01', encoding='utf-8'):
    # Create Table use header to create columns
    df[:0].to_sql(table_name, engine, if_exists=if_exists, index=False, schema=schema)
    # Prepare data
    output = StringIO()
    # Prepare data in csv
    df.to_csv(output, sep=sep, header=False, encoding=encoding, index=False)
    output.seek(0)
    try:
        schema_tablename = '{}.{}'.format(schema, table_name)        
        # # create a session using session maker of sqlalchemy
        Session = sessionmaker(bind=engine)
        session = Session()
        #Truncate table        
        session.execute('TRUNCATE TABLE {}'.format(schema_tablename))
        session.commit()
        session.close()
        
        # Make sqlalchemy connection using engine
        connection = engine.raw_connection()
        cursor = connection.cursor()
        # Load table from the file with header
        cursor.copy_from(output, schema_tablename, sep=sep, null='')
        connection.commit()
        print("Loaded data into {}".format(table_name))
        cursor.close()
        print("Cursor & DB connection closed.")
        connection.close()
    except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)


def read_sql(table_name, data):
    # ====== Reading table ======
    # Reading PostgreSQL table into a pandas DataFrame
    data = pd.read_sql('SELECT * FROM {}'.format(table_name), engine)
    print(data.head())


# Convert SAS Dataset to Pandas Dataframe
df=pd.read_sas("develop.sas7bdat",format='sas7bdat', encoding="utf-8")
#print(df.head(10))
#print(df.columns)

# ====== Connection ======
# Connecting to PostgreSQL by providing a sqlachemy engine
#engine = create_engine('postgresql://'+os.environ['postgres']+':'+os.environ['xoriant@123']+'@'+os.environ['localhost']+':'+os.environ['5432']+'/'+os.environ['xoriant'],echo=False)
engine = create_engine('postgresql://postgres:xoriant@123@localhost:5432/xoriant')

# Execution Example
table_name = 'develop_load'
schema  = 'public'
# dbname = 'xoriant'
# host = 'localhost'
# port = '5432'
# user = 'postgres'
# pwd = 'xoriant@123'

start_time = time.time()
#df_to_database(engine, df, schema, table_name, if_exists='replace')
#print("sqlalchemy to_sql CPU TIME: ","--- %s seconds ---" % (time.time() - start_time))
#read_sql(table_name, df)

# Convert df to csv, cretae table using header of dataframe & load csv to  table
output = 'develop_load.csv'
start_time = time.time()
df_to_csv_to_sql(output, engine, df, schema, table_name, if_exists='replace', sep=',', encoding='utf-8')
print("Cursor copy from CSV CPU TIME: ","--- %s seconds ---" % (time.time() - start_time))
#read_sql(table_name, df)


# $ ipython fastload_dataframe_to_posgresSQL.py
# sqlalchemy to_sql CPU TIME:  --- 16.150993824005127 seconds ---


# $ ipython fastload_dataframe_to_posgresSQL.py
# Loaded data into develop_load
# Cursor & DB connection closed.
# Cursor copy from CSV CPU TIME:  --- 2.3214499950408936 seconds ---
