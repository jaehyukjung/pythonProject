testcase = int(input())

for _ in range(testcase):
    ea, index = map(int, input().split())
    w = list(map(int, input().split()))
    temp = w
    cnt = 1
    index1 = index
    while(w[index] != max(temp)):
        temp1 =[]
        temp2 =[]
        k = w.index(max(w))

        for x in range(0, k):
            temp1.append(temp[x])
            if index1 == x:
                index1 = k + x
        for x in range(k + 1, len(temp)):
            temp2.append(temp[x])
            if index1 == x:
                index1 = x - (k+1)

        temp = temp2 + temp1
        cnt += 1

    if temp.count(w[index]) == 1:
        print(cnt)
    else:
        print(cnt + index1 + 1)