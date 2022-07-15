N = int(input())

arr = list(map(int, input().split()))

k = -1

for i in range(N-1):
    if arr[i] > arr[i+1]:
        k = i

if k == -1:
    print(-1)

else:
    m =k
    for i in range(k+1,N):
        if arr[k] > arr[i]:
            m = i

    arr[k], arr[m] = arr[m], arr[k]

    temp1 = arr[:k+1]
    temp2 = arr[k+1:]
    temp2.sort(reverse= True)

    arr = temp1 + temp2

    for x in arr:
        print(x, end=" ")


        