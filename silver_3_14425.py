n, m = map(int, input().split())


set1 = {input() for _ in range(n)}
# set2 = {input() for _ in range(m)}
cnt =0
for i in range(m):
    s = input()
    if s in set1:
        cnt += 1
print(cnt)