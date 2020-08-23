def _do_string_thing(s, v):
    return s + str(v*v)
​
def loop_str1(s='foobar', limit=LIMIT):
    x = []
    for i in range(limit):
        x.append(_do_string_thing(s, i/1.0))
​
def comp_str1(s='foobar', limit=LIMIT):
    return [_do_string_thing(s, i) for i in range(limit)]
​
def gen_str1(s='foobar', limit=LIMIT):
    return (_do_string_thing(s, i) for i in range(limit))
​
​
print("string thing ", "-"*60)
print("Looping ", timeit.timeit(loop_str1, number=REPEATS))
print("List comprehension: ", timeit.timeit(comp_str1, number=REPEATS))
print("Generator ", timeit.timeit(gen_str1, number=REPEATS))
