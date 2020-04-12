import psycopg2
import pandas as pd
import sys
import saspy

# read SAS dataset successfully
develop=pd.read_sas("develop.sas7bdat",format='sas7bdat', encoding="utf-8")

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

def create_table(create_sql):
        # Parse in connection information
    host_parm='localhost'
    db_parm='xoriant'
    username_parm='postgres'
    pw_parm='xoriant@123'
    credentials = {'host': host_parm, 'database': db_parm, 'user': username_parm, 'password': pw_parm}
    conn = psycopg2.connect(**credentials)
    #conn = psycopg2.connect("dbname='xoriant' user='postgres' password='xoriant@123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute(create_sql)
    conn.commit()
    conn.close()

create_table(query_create)


# Here you want to change your database, username & password according to your own values
param_dic = {
    "host"      : "localhost",
    "database"  : "xoriant",
    "user"      : "postgres",
    "password"  : "xoriant@123"
}

def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    return conn

def single_insert(conn, insert_req):
    """ Execute a single INSERT request """
    cursor = conn.cursor()
    try:
        cursor.execute(insert_req)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    cursor.close()
# Connecting to the database
conn = connect(param_dic)
# Inserting each row
for i in develop.index:        
    query = """
    INSERT into develop(AcctAge,
DDA    , DDABal , CashBk , Checks , DirDep , NSF , NSFAmt , Phone  , Teller ,
Sav    , SavBal , ATM    , ATMAmt ,  POS    , POSAmt , CD     ,CDBal  ,
IRA    ,IRABal , LOC    , LOCBal , ILS    , ILSBal , MM     , MMBal  ,
MMCred , MTG    , MTGBal , CC     , CCBal  , CCPurc , SDB    , Income ,
HMOwn  , LORes  , HMVal  , Age    , CRScore, Moved  , InArea , Ins    ,
Branch , Res    , Dep    , DepAmt , Inv    , InvBal ) 
values('%f','%f','%f','%f','%f','%f','%f','%f','%f', '%f','%f','%f','%f','%f','%f',
'%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f',
'%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%s','%s','%f','%f','%f','%f');
    """ % (develop['AcctAge'], develop['DDA'], develop['DDABal'], develop['CashBk'],
develop['Checks'], develop['DirDep'], develop['NSF'], develop['NSFAmt'], develop['Phone'],
develop['Teller'], develop['Sav'], develop['SavBal'], develop['ATM'], develop['ATMAmt'],
develop['POS'], develop['POSAmt'], develop['CD'], develop['CDBal'], develop['IRA'],
develop['IRABal'], develop['LOC'], develop['LOCBal'], develop['ILS'], develop['ILSBal'],
develop['MM'], develop['MMBal'], develop['MMCred'], develop['MTG'], develop['MTGBal'],
develop['CC'], develop['CCBal'], develop['CCPurc'], develop['SDB'], develop['Income'],
develop['HMOwn'], develop['LORes'], develop['HMVal'], develop['Age'], develop['CRScore'],
develop['Moved'], develop['InArea'], develop['Ins'], develop['Branch'], develop['Res'],
develop['Dep'], develop['DepAmt'], develop['Inv'], develop['InvBal']) 
    single_insert(conn, query)
# Close the connection
conn.close()





'''

#!/usr/bin/env/python

import psycopg2
import os
from io import StringIO
import pandas as pd

# Get a database connection
dsn = os.environ.get('DB_DSN')  # Use ENV vars: keep it secret, keep it safe
conn = psycopg2.connect(dsn)

# Do something to create your dataframe here...
df = pd.read_csv("file.csv")

# Initialize a string buffer
sio = StringIO()
sio.write(df.to_csv(index=None, header=None))  # Write the Pandas DataFrame as a csv to the buffer
sio.seek(0)  # Be sure to reset the position to the start of the stream

# Copy the string buffer to the database, as if it were an actual file
with conn.cursor() as c:
    c.copy_from(sio, "schema.table", columns=dataframe.columns, sep=',')
    conn.commit()

    '''