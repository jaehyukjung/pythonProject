arr = list(map(int, input().split()))

arr.sort()
arr.reverse()

cnt = 0

while (len(arr) > 0 and arr[0] <= len(arr)):
    n = arr[0]
    for i in range(n):
        arr.pop(0)
    cnt += 1

print(cnt)