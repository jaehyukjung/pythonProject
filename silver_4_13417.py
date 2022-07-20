testcase = int(input())

for _ in range(testcase):
    N = int(input())
    lst = list(input().split())
    ans_lst =[lst.pop(0)]
    for i in lst:
        if ord(ans_lst[0]) >= ord(i):
            ans_lst.insert(0,i)
        else:
            ans_lst.append(i)

    for i in ans_lst:
        print(i,end='')
    print()