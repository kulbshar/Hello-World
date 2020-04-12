myfile= open('C:\\Users\\ksharma\\python\\csv\\Employees.csv')
#print(myfile.read())
#print(myfile.read())
content = myfile.read()
myfile.close()
# through you can't read file after it closed
#  myfile.read() 
print(content)
print(content)

with open('C:\\Users\\ksharma\\python\\csv\\Employees.csv') as myfile:
    content = myfile.read()

print(content)

with open('C:\\Users\\ksharma\\python\\csv\\Employees_1.csv', "w") as myfile:
    myfile.write("Tomato\nCucumber\nOnion\n")
    myfile.write("Brinjal")

# a+ for appending and reading
with open('C:\\Users\\ksharma\\python\\csv\\Employees_1.csv', "a+") as myfile:
    myfile.write("\nOkra")
    myfile.seek(0) # cursor goes to first line
    content1=myfile.read()

print(content1)





