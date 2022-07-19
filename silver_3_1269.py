N, M = map(int, input().split())

lst_A = list(map(int, input().split()))
lst_B = list(map(int, input().split()))

set_A = set(lst_A)
set_B = set(lst_B)

set_U = set_A.union(set_B) - set_A.intersection(set_B)

print(len(set_U))