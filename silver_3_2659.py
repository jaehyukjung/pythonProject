def find(n):
    lst =[]
    for i in str(n):
        lst.append(i)
    ans_lst = []
    for i in range(4):
        s = ''
        for x in lst:
            s += x
        ans_lst.append(int(s))
        lst.append(lst.pop(0))

    return str(min(ans_lst))

a,b,c,d = map(int,input().split())
n = a*1000+b*100+c*10+d

ans = find(n)
cnt = 1
for i in range(1111,int(ans)):
    s = str(i)
    if '0' not in s:
        if s == find(s):
            cnt += 1

print(cnt)