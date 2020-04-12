''' Author: Kulbhushan Sharma

import datetime
x = datetime.datetime.now()
print(x)

student_grades= [1,2,3,4,5.1]
my_sum = sum(student_grades)
length = len(student_grades)
mean = my_sum / length
print(mean)

student_grades_d= {"suresh": 1, "ganesh": 2, "jeevan":3, "udit": 4, "Ravi":5.1}
print(student_grades_d.keys())
print(student_grades_d.values())


student_grades_tuple= (1,2,3,4,5.1)



def mean(mylist):
    the_mean = sum(mylist)/len(mylist)
    return the_mean

print(type(mean), type(sum))