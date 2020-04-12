import pandas
df = pandas.read_csv("C:\\Users\\ksharma\\python\\python_mega_course\\teaching\\supermarkets.csv")

df["Address"] = df["Address"] + ", " + df["City"] + ", " + df["State"] + ", " + df["Country"]

print(df)

import geopy
from geopy.geocoders import Nominatim
nom = Nominatim()

nom.geocode("735 Dolores St, San Francisco CA 94119")
n = nom.geocode("735 Dolores St, San Francisco CA 94119")
print(n.latitude)
print(n.longitude)

type(n)

df["Coordinates"] = df["Address"].apply(nom.geocode)
print(df)
print(df.Coordinates)
print(df.Coordinates[0])
print(df.Coordinates[0].latitude)

df["Latitude"] = df["Coordinates"].apply(lambda x:x.latitude if x != None else None)

df["Longitude"] = df["Coordinates"].apply(lambda x:x.longitude)

print(df)





