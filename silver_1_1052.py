n, m = map(int, input().split())

def max_pow(n):
    i = 1
    while n/2 > i:
        i *= 2

    return i

while m > 0:
    k = max_pow(n)
    n -= k
    m -= 1

print(k-n)



