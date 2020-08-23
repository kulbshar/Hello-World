def double_list(x):
    i = 0
    while i < len(x):
        x[i] = x[i] * 2
        i = i + 1


a = [1, 2, 3, 4, 5]
print("Before: ", a)
double_list(a)
print("After: ", a)


# Variable-Length Argument Lists

def avg(a, b, c):
    return (a + b + c) / 3


print(avg(3, 4, 5))


def avg1(a):
    total = 0
    for v in a:
        total += v
    return total / len(a)


print(avg1([1, 2, 3]))
print(avg1([1, 2, 3, 4, 5]))
# can pass a tuple too
t = (1, 2, 3, 4, 5)
avg1(t)


def f(*arg):
    print(arg)
    print(type(arg), len(arg))
    for x in arg:
        print(x)


f(1, 2, 3, 4, 5)
f('foo', 'bar', 'baz', 'qux', 'quux')


def mean(*args):
    total = 0
    print(args)
    print(type(args), len(args))
    for i in args:
        total += i
    return total


print(mean(123, 123, 475, 9967, 53638))


# Argument Tuple Unpacking
# An analogous operation is available on the other side of the equation in a Python function call.
# When an argument in a function call is preceded by an asterisk (*),
# it indicates that the argument is a tuple that should be unpacked and passed to the function as separate values

def avg2(*args):
    return sum(args)/len(args)


print(avg2(123, 432, 546, 678, 984, 123))


def func(x, y, z):
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'z = {z}')


func(1, 2, 3)
t = ('foo', 'bar', 'baz')
f(*t)

a = ['foo', 'bar', 'baz']
print(type(a))
f(*a)


s = {1, 2, 3}
print(type(s))
f(*s)

# You can even use tuple packing and unpacking at the same time:


def func1(*args):
    print(type(args), args)


a = ['foo', 'bar', 'baz', 'qux']
f(*a)


# Argument Dictionary Packing
# Python has a similar operator, the double asterisk (**),
# which can be used with Python function parameters and
# arguments to specify dictionary packing and unpacking.
# Preceding a parameter in a Python function definition
#  by a double asterisk (**) indicates that the corresponding
#  arguments, which are expected to be key=value pairs, should be packed into a dictionary:

def f_dict(**kwargs):
    print(kwargs)
    print(type(kwargs), len(kwargs))
    for key, val in kwargs.items():
        print(key, '-->', val)


f_dict(Employee="Kulbhushan", Salary=10000, Designation="Software Engineer")


# Argument Dictionary Unpacking
# Argument dictionary unpacking is analogous to argument tuple unpacking.
# When the double asterisk (**) precedes an argument in a Python function call,
# it specifies that the argument is a dictionary that should be unpacked,
# with the resulting items passed to the function as keyword arguments:
def f_arg_unpack(a, b, c):
    print(f'a = {a}')
    print(F'a = {a}')
    print(F'a = {a}')


d = {'a': 'foo', 'b': 25, 'c': 'qux'}
f_arg_unpack(**d)

f_arg_unpack(**dict(a='foo', b=25, c='qux'))

# Putting It All Together
# Think of *args as a variable-length positional argument list,
# and **kwargs as a variable-length keyword argument list.


def func_kw_args(a, b, *args, **kwargs):
    print(F'a = {a}')
    print(F'b = {b}')
    print(type(args), len(args), F'args = {args}')
    print(type(kwargs), len(kwargs), F'kwargs = {kwargs}')


func_kw_args(2, 3, "Kul", "20000", 'SE', name='Kulbhushan',
             salary=40000, designation='Software Engineer')


# Multiple Unpackings in a Python Function Call
# Python version 3.5 introduced support for additional unpacking generalizations,
# as outlined in PEP 448. One thing these enhancements allow is multiple unpackings
# in a single Python function call:

def f_mult_unpack(*args):
    for i in args:
        print(f'i --> {i}')


l = [1, 2, 3, 46, 5]
t = (45, 65, 4, 5, 78, 98)
s = {6, 7, 4, 68, 86}

f_mult_unpack(*l, *t, *s)
f_mult_unpack(*[1000, 2000, 3000], *[4000, 5000, 6000])


def f_mult_dict_unpack(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} --> {value}')


d1 = {'a': 1, 'b': 2}
d2 = {'x': 3, 'y': 4}

f_mult_dict_unpack(**d1, **d2)
f_mult_dict_unpack(**{'a': 1000, 'b': 2000}, **{'x': 3000, 'y': 4000})


def concat(*args, prefix='-> ', sep='.'):
    print(f'{prefix}{sep.join(args)}')


concat('a', 'b', 'c')
concat('a', 'b', 'c', prefix='//')
concat('a', 'b', 'c', prefix='//', sep='-')


# Docstrings

def avg_doc(*args):
    """Returns the average of a list of numeric values."""
    return sum(args) / len(args)


print(avg_doc.__doc__)
