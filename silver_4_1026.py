n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

S = list(map(lambda x,y: x*y,A,B))

print(sum(S))