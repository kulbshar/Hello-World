

temps = [22, 23, 54, 33, 23, -9999]

new_temps = []
for temp in temps:
    new_temps.append(temp/10)

print(new_temps)

# you can do above using list comprehension
new_temp1 = [temp/10 for temp in temps]
print(new_temp1)

# if will be ignored
new_temp2 = [temp/10 for temp in temps if temp != - 9999] 
print(new_temp2)
# wont't work
#new_temp2 = [temp/10 for temp in temps if temp != - 9999 else 0] 

new_temp2 = [temp/10 if temp != - 9999 else 0 for temp in temps ] 
print(new_temp2)


[i*2 for i in [1,5,6,4,7,3] ]
[i*2 for i in [1,5,6,4,7,3] if i >5]

[i*2 for i in [1,5,6,4,7,3] ]
[i*2 for i in [1,5,6,4,7,3] if i >5 else 0] # Error
[i*2 if i >5 else 0 for i in [1,5,6,4,7,3] ]





