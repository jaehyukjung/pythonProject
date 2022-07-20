R, C = map(int, input().split())

lst = [input() for _ in range(R)]
ans_lst = []
for i in range(R):
    lst2 =[]
    for j in range(C):
        lst2.append(lst[i][j])
    ans_lst.append(lst2)

for i in range(R):
    for j in range(C):
        cnt = 0
        if lst[i][j] =='X':
            if i+1 >= R or lst[i+1][j] == '.':
                cnt +=1
            if i-1 < 0 or lst[i-1][j] == '.':
                cnt +=1
            if j+1 >= C or lst[i][j+1] == '.':
                cnt +=1
            if j-1 < 0 or lst[i][j-1] == '.':
                cnt +=1

            if cnt >= 3:
                ans_lst[i][j] = '.'

while True:
    if 'X' not in ans_lst[0]:
        ans_lst.pop(0)
    else:
        break

while True:
    if 'X' not in ans_lst[len(ans_lst)-1]:
        ans_lst.pop(len(ans_lst)-1)
    else:
        break

while True:
    cnt = 0
    for i in ans_lst:
        if i[0] == '.':
            cnt += 1
    if cnt == len(ans_lst):
        for i in ans_lst:
            i.pop(0)
    else:
        break

while True:
    cnt = 0
    for i in ans_lst:
        if i[len(ans_lst[0])-1] == '.':
            cnt += 1
    if cnt == len(ans_lst):
        for i in ans_lst:
            i.pop(len(ans_lst[0])-1)
    else:
        break

for i in ans_lst:
    for j in i:
        print(j,end="")
    print()



