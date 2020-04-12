monday_temp = [9.1, 1.22, 2, 6.333, 8]

for i in monday_temp:
    print(round(i, 2))

for letter in "hello":
    print(letter)


grades = {"Kul":123,"Ravi":734,"Perry":354,"Jeremy":875}

for item in grades.values():
    print(item)

for name in grades.keys():
    print(name)

for value in grades.items():
    print(value)

for key,value in grades.items():
    print(key,value)


# While Loop

# a = int(input("Enter a number: "))
a=20
while a > 10:
    print(a)
    a -=1
    # break

username= ''

# while username != 'pypy':
#     username = input("Enter Username: ")


# while True:
#     username = input("Enter username: ")
#     if username == 'pypy':
#         break
#     else:
#         continue


def sentence_maker(phrase):
    interrogative=('how','what','why')
    cap = phrase.capitalize()
    if phrase.startswith(interrogative):
        return "{}?".format(cap)
    else:
        return "{}.".format(cap)

print(sentence_maker('how are you'))
print(sentence_maker('hello'))

results = []
while True:
    phrase = input("Say Something: ")
    if phrase == '\end':
        break
    else:
        results.append(sentence_maker(phrase))

print(" ".join(results))

