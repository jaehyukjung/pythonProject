N = int(input())

lst = [x for x in range(1,N+1)]

while len(lst)>1:
    print(lst.pop(0), end=' ')
    lst.append(lst.pop(0))

print(lst[0])