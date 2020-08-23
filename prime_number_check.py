for n in range(2, 10):
    prime = True
    for x in range(2, n):
        if n % x == 0:
            prime = False
            print(f"{n} is not prime")
            break
        if prime:
            print(f"{n} is prime!")


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} is not prime")
            break
        else:
            print(f"{n} is prime!")
