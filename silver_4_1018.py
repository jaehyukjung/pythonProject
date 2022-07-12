n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(input())
count = []
for i in range(n-7):
    for j in range(m-7):
        index1 = 0
        index2 = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 ==0:
                    if arr[x][y] != 'W':
                        index1 +=1
                    if arr[x][y] != 'B':
                        index2 +=1
                else:
                    if arr[x][y] != 'B':
                        index1 +=1
                    if arr[x][y] != 'W':
                        index2 +=1
        count.append(min(index1, index2))

print(min(count))