

n = int(input())
lst = [input() for _ in range(n)]

cnt_row = 0
cnt_col = 0

for x in lst:
    ans = x.split('X')
    for i in ans:
        if len(i) >=2:
            cnt_row += 1

col_lst =[]
for i in range(n):
    s =''
    for j in range(n):
        s += lst[j][i]
    col_lst.append(s)

for x in col_lst:
    ans = x.split('X')
    for i in ans:
        if len(i) >=2:
            cnt_col += 1

print(cnt_row, cnt_col)