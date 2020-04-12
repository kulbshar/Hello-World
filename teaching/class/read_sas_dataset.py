import saspy
import pandas as pd

# read successfully
develop=pd.read_sas("develop.sas7bdat",format='sas7bdat', encoding="utf-8")

print(develop.head(10))
print(develop.columns)
print(develop.dtypes)

# AcctAge    float64
# DDA        float64
# DDABal     float64
# CashBk     float64
# Checks     float64
# DirDep     float64
# NSF        float64
# NSFAmt     float64
# Phone      float64
# Teller     float64
# Sav        float64
# SavBal     float64
# ATM        float64
# ATMAmt     float64
# POS        float64
# POSAmt     float64
# CD         float64
# CDBal      float64
# IRA        float64
# IRABal     float64
# LOC        float64
# LOCBal     float64
# ILS        float64
# ILSBal     float64
# MM         float64
# MMBal      float64
# MMCred     float64
# MTG        float64
# MTGBal     float64
# CC         float64
# CCBal      float64
# CCPurc     float64
# SDB        float64
# Income     float64
# HMOwn      float64
# LORes      float64
# HMVal      float64
# Age        float64
# CRScore    float64
# Moved      float64
# InArea     float64
# Ins        float64
# Branch      object
# Res         object
# Dep        float64
# DepAmt     float64
# Inv        float64
# InvBal     float64



#print(df_ldms_prim_ds.loc[(df_ldms_prim_ds.ptid==700429004.0) & (df_ldms_prim_ds.visitno==26) ,['ptid','spcdt','visitno']])
#print(df_ldms_prim_ds.loc[(df_ldms_prim_ds.ptid==700429004.0) & (df_ldms_prim_ds.visitno==31) ,['ptid','spcdt','visitno']])

import psycopg2

# In [5]: import psycopg2

# In [6]: psycopg2.__version__
# Out[6]: '2.8.4 (dt dec pq3 ext lo64)

def create_table():

        # Parse in connection information
    host_parm='localhost'
    db_parm='xoriant'
    username_parm='postgres'
    pw_parm='xoriant@123'
    credentials = {'host': host_parm, 'database': db_parm, 'user': username_parm, 'password': pw_parm}
    conn = psycopg2.connect(**credentials)
    #conn = psycopg2.connect("dbname='xoriant' user='postgres' password='xoriant@123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("create table if not exists store(item text, quantity integer, price real)")
    conn.commit()
    conn.close()

create_table()
