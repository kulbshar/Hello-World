

# while True:
#     with open('C:\\Users\\ksharma\\python\\csv\\Employees.csv') as myfile:
#         content = myfile.read()
#     print(content)

# import sys
# sys.builtin_module_names
# which gives you buildin modules
# 
# import time
# dir(time)
# time.sleep(3)


# import time
# while True:
#     with open('C:\\Users\\ksharma\\python\\csv\\Employees_1.csv') as myfile:
#         content = myfile.read()
#         time.sleep(5)
#     print(content)


import time
import os

# while True:
#     if os.path.exists("C:\\Users\\ksharma\\python\\csv\\Employees_1.csv"):
#         with open('C:\\Users\\ksharma\\python\\csv\\Employees_1.csv') as myfile:
#             content = myfile.read()
#             print(content)
#     else:
#         print("File doesn't exists.")
#     time.sleep(5)

import pandas as pd

while True:
    if os.path.exists("C:\\Users\\ksharma\\python\\csv\\Employees_12.csv"):
        data = pd.read_csv("C:\\Users\\ksharma\\python\\csv\\Employees_12.csv")
        print("Dataframe: ", data)
        print("Mean: ", data.mean())
        print("Mean first column: ", data.mean()['st1'])
        print("Mean second column: ", data.mean()['st2'])
    else:
        print("File doesn't exists.")
    time.sleep(5)

