def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean


print("sum of list [1, 2, 3] is ", mean([1, 2, 3]))

print("[1, 2, 3, 22, 33, 12.1] is ", mean([1, 2, 3, 22, 33, 12.1]))
# print(mean([1, 2, 3]))

print(type(mean), type(sum))

# will return both None and mean
def mean1(mylist):
    the_mean = sum(mylist) / len(mylist)
    print(the_mean)

print("sum of list [1, 2, 3] is using mean1 function ", mean1([1, 2, 3]))

# The problem with mean1 function

mymean =  mean1([1, 2, 3])
# this will give mean type error as mean1 function return None by implicitly
print(mymean + 10)

# moral of story, always return values from a function if you don't have any special case






