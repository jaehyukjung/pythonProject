testcase = int(input())

for _ in range(testcase):
    n = int(input())
    dic = {}
    for i in range(n):
        name, kind = input().split()
        if kind in dic.keys():
            dic[kind].append(name)
        else:
            dic[kind] = []
            dic[kind].append(name)
    ans = 1
    for i in dic.keys():
        ans *= (len(dic[i])+1)
    print(ans-1)

