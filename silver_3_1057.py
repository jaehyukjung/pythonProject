N, p1, p2 = map(int, input().split())

round = 1

while N > 1:
    if p1 < p2 and p1 % 2 == 1 and p1 +1 ==p2:
        break
    elif p1 > p2 and p1 % 2 == 0 and p1 - 1 ==p2:
        break


    if p1 % 2 == 0:
        p1 = p1 // 2
    elif p1 % 2 == 1:
        p1 = (p1 // 2) + 1

    if p2 % 2 == 0:
        p2 = p2 // 2
    elif p2 % 2 == 1:
        p2 = (p2 // 2) + 1

    round += 1

    if N % 2 == 0:
        N = N // 2
    else:
        N = (N // 2) +1

print(round)