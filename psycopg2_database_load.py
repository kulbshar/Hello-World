# Execution Example
# file_path = 'transaction.csv'
# table_name = 'develop_load'
# schema  = 'public'
# dbname = 'xoriant'
# host = 'localhost'
# port = '5432'
# user = 'postgres'
# pwd = 'xoriant@123'

# Connect to Postgres SQL

import psycopg2
from psycopg2 import OperationalError
import sys
import time
import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from io import StringIO


class DatabaseConnection:

    def __init__(self, db_name, db_user, db_password, db_host, db_port):
        self.connection = None
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port

    # Connection
    def create_connection(self):
        try:
            self.connection = psycopg2.connect(
                database=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port,
            )
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            print(f"The error '{e}' occurred")
        return self.connection

    def create_postgre_engine(self):
        '''
        Connecting to PostgreSQL by providing a sqlachemy engine
        '''
        engine = create_engine(
            'postgresql://{}:{}@{}:{}/{}'.format(self.db_user, self.db_password, self.db_host, self.db_port, self.db_name))

    def close_connection(self):
        self.connection.close()

    def execute_dml_query(self, query):
        self.connection.autocommit = True
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            print("DML Query executed successfully")
        except OperationalError as e:
            print(f"The error '{e}' occurred")

    # Read from table
    def execute_read_query(self, query):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"The error '{e}' occurred")

    def csv_load_into_table(self, file_path, table_name):
        '''
        This function upload csv to a target table
        '''
        try:
            # Create DB Cursor
            cur = self.connection.cursor()
            f = open(file_path, "r")

            # Truncate the table first
            cur.execute("Truncate {} Cascade;".format(table_name))
            print("Truncated {}".format(table_name))

            # Load table from the file with header
            cur.copy_expert(
                "copy {} from STDIN CSV HEADER QUOTE '\"'".format(table_name), f)
            cur.execute("commit;")
            print("Loaded data into {} Successfully.".format(table_name))

        except Exception as e:
            print("Error: {}".format(str(e)))
            sys.exit(1)

    def csv_copy_into_table(self, file_path, table_name, dlim=' '):
        '''
        This function copy rows from csv to a target table using iteration
        '''
        try:
            # Create DB Cursor
            cur = self.connection.cursor()

            # Truncate the table first
            cur.execute("Truncate {} Cascade;".format(table_name))
            print("Truncated {}".format(table_name))

            # Load table from the file with header
            with open(file_path, 'r') as f:
                next(f)
                cur.copy_from(f, table_name, sep=dlim)
                # print(f)
            self.connection.commit()
            print("Copied data into {} Successfully.".format(table_name))

        except Exception as e:
            print("Error: {}".format(str(e)))
            sys.exit(1)

    def csv_insert_into_table(self, file_path, table_name):
        '''
        This function insert rows from csv to a target table using iteration
        '''
        try:
            # Create DB Cursor
            cur = self.connection.cursor()

            # Truncate the table first
            cur.execute("Truncate {} Cascade;".format(table_name))
            print("Truncated {}".format(table_name))

            # Load table from the file with header
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # skip header
                for row in reader:
                    cur.execute("""insert into {}(AcctAge,
            DDA, DDABal, CashBk, Checks, DirDep, NSF, NSFAmt, Phone, Teller,
            Sav, SavBal, ATM, ATMAmt,  POS, POSAmt, CD, CDBal,
            IRA, IRABal, LOC, LOCBal, ILS, ILSBal, MM, MMBal,
            MMCred, MTG, MTGBal, CC, CCBal, CCPurc, SDB, Income,
            HMOwn, LORes, HMVal, Age, CRScore, Moved, InArea, Ins,
            Branch, Res, Dep, DepAmt, Inv, InvBal) values(%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
           %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
           %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)""".format(table_name), row)
            self.connection.commit()
            print("Insert data into {} Successfully.".format(table_name))

        except Exception as e:
            print("Error: {}".format(str(e)))
            sys.exit(1)


def main():
    # Create Connection
    dbase = DatabaseConnection("xoriant", "postgres",
                               "xoriant@123", "localhost", "5432")
    dbase.create_connection()

    # Drop table
    print("drop Table 'develop'")
    query_drop_table = """
    drop table if exists develop_transc;
"""
    dbase.execute_dml_query(query_drop_table)

    # Create table
    print("Create Table 'develop'")
    query_create_table = """
        create table if not exists
        develop_transc(AcctAge   float8, DDA    float8, DDABal   float8, CashBk     float8,  Checks     float8,
        DirDep     float8, NSF        float8, NSFAmt     float8, Phone      float8, Teller     float8,
        Sav        float8, SavBal     float8, ATM        float8, ATMAmt     float8, POS        float,
        POSAmt     float8, CD         float8, CDBal      float8, IRA        float8, IRABal     float8,
        LOC        float8, LOCBal     float8, ILS        float8, ILSBal     float8, MM         float8,
        MMBal      float8, MMCred     float8, MTG        float8, MTGBal     float8, CC         float8,
        CCBal      float8, CCPurc     float8, SDB        float8, Income     float8, HMOwn      float8,
        LORes      float8, HMVal      float8, Age        float8, CRScore    float8, Moved      float8,
        InArea     float8, Ins        float8, Branch      text,  Res         text,  Dep        float8,
        DepAmt     float8, Inv        float8, InvBal     float8  );
"""
    dbase.execute_dml_query(query_create_table)

    # Upload CSV to the table
    file_path = 'transaction_transc.csv'
    table_name = 'develop_transc'

    start_time = time.time()
    dbase.csv_load_into_table(file_path, table_name)
    print("PSYCOPG2 cpu time copy_expert from CSV: ",
          "--- %s seconds ---" % (time.time() - start_time))

    # Copy CSV into the table
    file_path = 'transaction.csv'

    # start_time = time.time()
    # dbase.csv_copy_into_table(file_path, table_name, dlim=',')
    # print("PSYCOPG2 cpu time iteration copy from CSV: ",
    #       "--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    dbase.csv_insert_into_table(file_path, table_name)
    print("PSYCOPG2 cpu time Insert into table iteration from CSV: ",
          "--- %s seconds ---" % (time.time() - start_time))

    # Update rows in Table
    update_post_description = """
    UPDATE
    develop
    SET
    res = 'FFFFFFFFFFFFFFFFFFFFFFFFF'
    WHERE
    branch = 'B17'
    """
    dbase.execute_dml_query(update_post_description)

    # Delete
    delete_comment = "DELETE FROM develop WHERE res = 'U' "
    dbase.execute_dml_query(delete_comment)

    # Read Data
    print("read from table 'develop'")
    select_users = "SELECT * from public.develop"
    results = dbase.execute_read_query(select_users)
    print(type(results))
    # for result in results:
    #     print(type(result))

    print("DB connection closed.")
    dbase.close_connection()

    engine = dbase.create_postgre_engine()
    table_name = 'develop_transc'
    schema = 'public'


if __name__ == "__main__":
    main()
