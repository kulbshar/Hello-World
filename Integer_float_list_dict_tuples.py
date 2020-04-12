rank = 10
eggs = 12
people = 3

type(rank)
print(type(rank))

print(dir(__builtins__))

# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 
# 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 
# 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 
# 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 
# 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 
# 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 
# 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 
# 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 
# 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError',
#  'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 
#  'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__IPYTHON__', '__build_class__',
#   '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 
#   'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 
#   'credits', 'delattr', 'dict', 'dir', 'display', 
# 'divmod', 'enumerate', 'eval', 'exec', 'filter', 'float', 'format', 'frozenset', 'get_ipython', 'getattr', 'globals', 'hasattr', 
# 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 
# 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'range', 'repr', 'reversed', 'round', 'set', 
# 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']


# Python has implicit type declaration
x = 10
y = '10'
sum1 = x + x
sum2 = y + y
z=10.2

print(sum1, sum2)

print(type(x), type(y), type(z))




# Compound datatype



student_grades = [9.1, 8.8, 7.5]
print(type(student_grades))

print(dir(int))
print(dir(str))

# Complete list of python inbuilt functions
print(dir(__builtins__) )
#  for eg: print() is a builtin functions and don't need . notation
# while .upper() is a method of str


student_grades = [9.1, 8.8, 7.5]

mysum = sum(student_grades)
mycount = len(student_grades)
mean = mysum / mycount
print("mean", mean)

# Dictionaries

student_grades = {"Mary":9.1, "Ravi":10.1, "Kul":2.3 , "john":5.2 , "rock":11.1}

help(dict.values)

# In [26]: student_grades.values()
# Out[26]: dict_values([9.1, 10.1, 2.3, 5.2, 11.1])

# In [27]: student_grades.keys()
# Out[27]: dict_keys(['Mary', 'Ravi', 'Kul', 'john', 'rock'])

# tuples are immutable
temp = (1, 2, 3)
print(temp)

# list are mutable
temp1 = [1, 2, 3]
temp1.append(10)
temp1.remove(1)

# tuple doesn't have methods like append() or remove() as they immutable
# the advantages of tuples are 1) can't change 2) a bit faster than list


rainfall = [10.2, 33, "Sharma", [2, 3, 5]]
print(rainfall)



student_grades = [9.1, 8.8, 7.5, 10, 11, 12 , 'kkk',11, 11 ,11]

print(student_grades.count(11))

username = "Python123"
username.lower()

temp.clear()

student_grades = [9.1, 8.8, 7.5, 10, 11, 12]
temp.index(8.8)
temp.index(12,5)

# to get item from list
temp.__getitem__(1)

# but you don't need to use __getitem__
# use temp[1] instead but python actually call temp.__getitem__(1)
# python make is easy for us as temp[1]len
temp[1]

temp.append(11)
temp.append(11)
temp.append(11)
temp
# Out[22]: [9.1, 8.8, 7.5, 10, 11, 12, 22.2, 11, 11, 11]
set(temp)
# Out[23]: {7.5, 8.8, 9.1, 10, 11, 12, 22.2}




