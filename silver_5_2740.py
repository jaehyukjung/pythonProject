import numpy as np

first = []
n,m = map(int, input().split())
for _ in range(n):
    first.append(list(map(int, input().split())))

second = []
n,m = map(int, input().split())
for _ in range(n):
    second.append(list(map(int, input().split())))

ans_lst = np.matmul(first, second)

for x in ans_lst:
    for y in x:
        print(y, end=' ')
    print('')