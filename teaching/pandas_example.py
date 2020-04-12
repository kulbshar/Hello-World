import pandas
df1=pandas.DataFrame([[1,2,3],[3,4,5],[6,7,8]])
print(df1)

df2=pandas.DataFrame([[1,2,3],[3,4,5],[6,7,8]], columns=["price","age","value"])
df3=pandas.DataFrame([[1,2,3],[3,4,5],[6,7,8]], columns=["price","age","value"], index=["first","second","third"])



