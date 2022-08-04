N, M = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

left = []
right = []

for x in lst:
    if x < 0:
        left.append(x)
    else:
        right.append(x)
ans = []
for i in range(len(left) // M):
    ans.append(abs(left[M*i]))
if len(left) % M > 0:
    ans.append(abs(left[(len(left)//M)*M]))


right.reverse()
for i in range(len(right) // M):
    ans.append(right[M*i])
if len(right) % M > 0:
    ans.append(abs(right[(len(right)//M)*M]))

ans.sort()

answer = ans.pop()
answer += 2*sum(ans)
print(answer)