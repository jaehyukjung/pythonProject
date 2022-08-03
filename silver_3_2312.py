import math

def isPrime(num):
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


testcase = int(input())

for _ in range(testcase):
    N = int(input())
    dic = {}
    lst = []
    for i in range(2,math.floor(math.sqrt(N)) + 1):
        if isPrime(i):
            dic[i] = 0
            lst.append(i)
    i = 0
    while i < len(lst):
        if N % lst[i] == 0:
            dic[lst[i]] += 1
            N = N / lst[i]
        else:
            i += 1

    for key in dic.keys():
        if dic[key] != 0:
            print(key, dic[key])


