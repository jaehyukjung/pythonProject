testcase = int(input())

for _ in range(testcase):
    ea, index = map(int, input().split())
    w = list(map(int, input().split()))
    temp = w.copy()
    cnt = 1
    index1 = index
    while(w[index] != max(temp)):
        if temp[0] == max(temp):
            temp.pop(0)
            cnt += 1
            index1 -= 1

        else:
            temp.append(temp[0])
            temp.pop(0)
            if index1 == 0:
                index1 = len(temp)-1

            else:
                index1 -= 1

    if temp.count(w[index]) == 1:
        print(cnt)
    else:
        for x in range(0,index1):
            if temp[x] == max(temp):
                cnt += 1
        print(cnt)