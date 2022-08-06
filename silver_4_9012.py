N = int(input())

for _ in range(N):
    s = input()
    lst = []
    ans = True
    for i in s:
        if i == '(':
            lst.append(i)
        elif i == ')':
            if not lst:
                ans = False
                break
            else:
                lst.pop(len(lst)-1)
    if ans and not lst:
        print('YES')
    else:
        print('NO')

