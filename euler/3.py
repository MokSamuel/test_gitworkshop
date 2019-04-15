number=int(600851475143)

for i in range(1,number):
    if number % i == 0:
        if isprime(i)[0]:
            print(i)
        