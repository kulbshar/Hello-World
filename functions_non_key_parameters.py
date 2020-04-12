def mean(*args):
    return args

print(mean(1, 2, 3, 4, 5))


def mean1(*args):
    return sum(args) / len(args)

print(mean1(1, 2, 3, 4, 5))


def mean2(**kwargs):
    return kwargs

print(mean2(a=1, b=10, c=20, d=4, e=5))




def mean3(*args):
    return max(args)

print(mean3(1, 2, 3, 4, 5))


def mean4(**kwargs):
    return max(kwargs)

print(mean4(a=1, b=10, c=20, d=4, e=5))


def mean5(**kwargs):
    return max(kwargs.values())

print(mean5(a=1, b=10, c=20, d=4, e=5))

