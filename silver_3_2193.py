n = int(input())

lst = list(int(input()) for _ in range(n))

lst.sort()

print(int(round(sum(lst) / len(lst),0)))

print(lst[(round(len(lst)/2))])


max_count = 0

count_lst = []
for i in lst:
    if lst.count(i) > max_count and (i not in count_lst):
        count_lst.clear()
        count_lst.append(i)
        max_count = lst.count(i)

    elif lst.count(i) == max_count and (i not in count_lst):
        count_lst.append(i)


if len(count_lst) > 1 :
    count_lst.remove(min(count_lst))
    print(count_lst[0])
else:
    print(count_lst[0])

print(lst[len(lst)-1]-lst[0])