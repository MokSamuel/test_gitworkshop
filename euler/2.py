i=1
current=1
sum=0

while current < 4000000:
    if current % 2 == 0:
        sum=sum+current
        print(str(current) + " added")
    i=i+1
    current=fibonacci(i,i)[0]

print(sum)