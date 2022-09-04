from itertools import combinations

while True:
    lst = list(map(int,input().split()))
    if lst[0] == 0:
        break
    del lst[0]
    combi_list = list(combinations(lst,6))
    for x in combi_list:
        for j in x:
            print(j,end=' ')
        print()
    print()



