N = int(input())

n = len(str(N))


if N < 10:
    l = N

else:
    l =0
    sum1 =0
    for i in range(0,n-1):
        sum1 = sum1+9*(10**i)
    sum2 =0
    for i in range(1,n):
        sum2 = sum2 + i*9*(10**(i-1))
    l = (N-sum1)*n + sum2

print(l)

