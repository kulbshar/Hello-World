user_input = input("Enter your name: ")
suname = input("Enter your surname: ")
message = "Hello %s!" %user_input
message1 = "Hello {}!".format(user_input)
message2 = "Hello {} {}!".format(user_input, suname)
print(message)
print(message1)