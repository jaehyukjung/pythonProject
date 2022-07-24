row, col = map(int, input().split())
ea = int(input())
lst = [list(map(int,input().split())) for _ in range(ea)]

my = list(map(int,input().split()))
ans = 0

for x in lst:
    if my[0] == 1:
        if x[0] == 1:
            dist = abs(x[1] - my[1])
        elif x[0] == 2:
            dist = col + min(x[1] + my[1], 2 * row - x[1] - my[1])
        elif x[0] == 3:
            dist = x[1] + my[1]
        elif x[0] == 4:
            dist = (row - my[1]) + x[1]
    elif my[0] == 2:
        if x[0] == 1:
            dist = col + min(x[1] + my[1], 2 * row - x[1] - my[1])
        elif x[0] == 2:
            dist = abs(x[1] - my[1])
        elif x[0] == 3:
            dist = (col - x[1]) + my[1]
        elif x[0] == 4:
            dist = (col - x[1]) + (row - my[1])

    elif my[0] == 3:
        if x[0] == 1:
            dist = x[1] + my[1]
        elif x[0] == 2:
            dist = x[1] + (col - my[1])
        elif x[0] == 3:
            dist = abs(x[1] - my[1])
        elif x[0] == 4:
            dist = row + min(x[1] + my[1], 2 * col - x[1] - my[1])
    else:
        if x[0] == 1:
            dist = (row - x[1]) + my[1]
        elif x[0] == 2:
            dist = (row - x[1]) + (col - my[1])
        elif x[0] == 3:
            dist = row + min(x[1] + my[1], 2 * col - x[1] - my[1])
        elif x[0] == 4:
            dist = abs(x[1] - my[1])

    ans += dist

print(ans)