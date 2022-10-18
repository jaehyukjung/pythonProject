n = int(input())

arr = []

for i in range(n):
    arr2 = []
    for j in range(3):
        arr2 = list(map(int,input().split()))
    arr.append(arr2)


f = 0
n = 0
for i in range(3*(2**(n-1))):
    cost = 0
    for j in range(n):
        for k in range(3):
            if k == n :
                k = (n+1) %3
            cost +=arr[j][k]


