n = int(input())

i = 0

cnt = 0
for i in range(2**(n-1),2**(n)):
    s = str(bin(i))[2:]
    if '11' not in (s):
        cnt+=1

print(cnt)