import psycopg2
import pandas as pd
import sys
import time

# Exporting DF to CSV
def df_to_csv(df, file_path):
    '''
    This function creates a csv file from Pandas Dataframe
    '''
    try:
        # Write to csv file
        df.to_csv(file_path, encoding='utf-8', header = True,\
         doublequote = True, sep=',', index=False)
        print("CSV File has been created")
    except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)


def pg_load_table(file_path, query_create, table_name, dbname, host, port, user, pwd):
    '''
    This function upload csv to a target table
    '''
    try:
        conn = psycopg2.connect(dbname=dbname, host=host, port=port,\
         user=user, password=pwd)
        print("Connecting to Database")
        cur = conn.cursor()
        f = open(file_path, "r")
        #create table if not exist
        cur.execute(query_create)
        # Truncate the table first
        cur.execute("Truncate {} Cascade;".format(table_name))
        print("Truncated {}".format(table_name))
        
        # Load table from the file with header
        cur.copy_expert("copy {} from STDIN CSV HEADER QUOTE '\"'".format(table_name), f)
        cur.execute("commit;")
        print("Loaded data into {}".format(table_name))
        conn.close()
        print("DB connection closed.")

    except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)



# Execution Example with Dataframe and CSV path
file_path = 'transaction.csv'
# read SAS Dataset successfully to Pandas Dataframe
df=pd.read_sas("develop.sas7bdat",format='sas7bdat', encoding="utf-8")
print(df.head(10))
print(df.columns)
# print(df.dtypes)
# Convert Pandas Dataframe to CSV
df_to_csv(df, file_path)

# Execution Example
file_path = 'transaction.csv'
table_name = 'develop'
dbname = 'xoriant'
host = 'localhost'
port = '5432'
user = 'postgres'
pwd = 'xoriant@123'

query_create = """
        create table if not exists 
        develop(
        AcctAge    float8,
        DDA        float8,
        DDABal     float8,
        CashBk     float8,
        Checks     float8,
        DirDep     float8,
        NSF        float8,
        NSFAmt     float8,
        Phone      float8,
        Teller     float8,
        Sav        float8,
        SavBal     float8,
        ATM        float8,
        ATMAmt     float8,
        POS        float8,
        POSAmt     float8,
        CD         float8,
        CDBal      float8,
        IRA        float8,
        IRABal     float8,
        LOC        float8,
        LOCBal     float8,
        ILS        float8,
        ILSBal     float8,
        MM         float8,
        MMBal      float8,
        MMCred     float8,
        MTG        float8,
        MTGBal     float8,
        CC         float8,
        CCBal      float8,
        CCPurc     float8,
        SDB        float8,
        Income     float8,
        HMOwn      float8,
        LORes      float8,
        HMVal      float8,
        Age        float8,
        CRScore    float8,
        Moved      float8,
        InArea     float8,
        Ins        float8,
        Branch      text,
        Res         text,
        Dep        float8,
        DepAmt     float8,
        Inv        float8,
        InvBal     float8
        );
"""
start_time = time.time()
# Read csv and load data into postgress table. also create table if don't exist
pg_load_table(file_path,query_create, table_name, dbname, host, port, user, pwd)
print("psycopg2 Cursor copy from CSV CPU TIME: ","--- %s seconds ---" % (time.time() - start_time))

# psycopg2 Cursor copy from CSV CPU TIME:  --- 0.7127530574798584 seconds ---