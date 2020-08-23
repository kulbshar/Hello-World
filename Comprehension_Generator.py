import timeit

LIMIT = 9999
REPEATS = 2000


def loopsq(limit=LIMIT):
    x = []
    for i in range(limit):
        x.append(i*i)
    return x


def gensq(limit=LIMIT):
    x = (i*i for i in range(limit))
    return x


def compsq(limit=LIMIT):
    x = [i*i for i in range(limit)]
    return x


def _floaty(v1, v2):
    return v2/42.0*v1


def loop_float(limit=LIMIT, value=23.0):
    x = []
    for i in range(limit):
        x.append(_floaty(i, value))


def comp_float(limit=LIMIT, value=23.0):
    return [_floaty(i, value) for i in range(limit)]


def gen_float(limit=LIMIT, value=23.0):
    return (_floaty(i, value) for i in range(limit))


print("String Things ", "-"*60)
print("Looping ", timeit.timeit(loopsq, number=REPEATS))
print("List comprehension: ", timeit.timeit(compsq, number=REPEATS))
print("Generator ", timeit.timeit(gensq, number=REPEATS))
print(compsq(limit=5))


print("floating ", "-"*60)
print("Looping ", timeit.timeit(loop_float, number=REPEATS))
print("List comprehension: ", timeit.timeit(comp_float, number=REPEATS))
print("Generator ", timeit.timeit(gen_float, number=REPEATS))
