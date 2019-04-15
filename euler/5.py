ssq=0
sum=0

for i in range(1,101):
    ssq=ssq+i**2
    sum=sum+i

sumsq=sum**2
print(sumsq-ssq)