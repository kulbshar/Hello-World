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



import saspy
import pandas as pd
import sys

# Execution Example with Dataframe and CSV path
file_path = 'transaction.csv'
# read successfully
df=pd.read_sas("develop.sas7bdat",format='sas7bdat', encoding="utf-8")

print(df.head(10))
print(df.columns)
# print(df.dtypes)

df_to_csv(df, file_path)

