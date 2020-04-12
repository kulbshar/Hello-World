# import json
# json_data = json.load(open("C:\\Users\\ksharma\\python\\python_mega_course\\teaching\\data.json"))

import pandas

df7 = pandas.read_json("http://pythonhow.com/supermarkets.json")
print(df7)

# set index
df7 = df7.set_index("Address")
print(df7)


# filter rows and columns using label values
df7.loc["735 Dolores St":"332 Hill St","Country":"Name"]
df7.loc["735 Dolores St","Country":"Name"]
df7.loc[:,"Name"]

# convert to list
list(df7.loc[:,"Name"])

# filter dataframe by position
df7.iloc[1:3,1:3]


# drop rows & columns in dataframe

df7.drop("City",1)
df7.drop("3666 21st St",0)

# drop columns by position 
df = df7.drop(df7.columns[0:3],1)

# drop rows by position

df = df7.drop(df7.index[0:3],0)

# Add new columns 
df7["Continent"] = df7.shape[0]*["North America"]

# Modify columns in dataframe 
df7["Continent"] = df7["Country"] + "," + "North America"


# Add new row. Transpose style

print(df7)
df7["Continent"] = df7["Country"] + "," + "North America"

df7_t = df7.T

df7_t["My Address"] = [10,"My City","My State","My Country","My Shop",7, "My Continent"]
df=  df7_t.T

print(df)


# update existing row using  transpose

print(df)
df7_t["3666 21st St"] = [10,"My City","My State","My Country","My Shop",7, "My Continent"]
df= df7_t.T
print(df)











