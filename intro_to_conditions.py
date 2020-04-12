def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

student_grades = {"Mary":10.1, "Ravi":12.1, "Rock":5.5}
grades = [1, 2, 3, 22, 33, 12.1]
#print(mean(student_grades))

# mean function doesn't suppport dictionaries
# Create a function which support both List and Dictionaries

avg= sum(grades) / len(grades)  
avg1= sum(student_grades.values()) / len(student_grades)
print(avg, avg1)


def average(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    
    return the_mean

print("Mean of dict student_grades ", average(student_grades))
print("Mean of List ", average(grades))


x = 1

if x ==1:
    print("yes")
else:
    print("no")

x = 1
y = 1

if x ==1 and y ==1:
    print("Yes")
else:
    print("No")

if x==1 or y==2:
    print("Hi")
else:
    print("bye")



def average1(value):
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    
    return the_mean

print("Mean of dict student_grades from average1 ", average(student_grades))
print("Mean of List from average1 ", average(grades))



def weather_condition(temp):
    if temp > 20:
        return "Warm"
    else:
        return "Cold"

user_input = float(input("Enter temperature: "))
print(weather_condition(user_input))




