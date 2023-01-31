from collections import deque
# import sys
# sys.setrecursionlimit(10000)
# #
# # def dfs(i,j,e,p, pre_p):
# #     if j == e:
# #         price.append(pre_p+p)
# #     if not v[j]:
# #         v[j] = True
# #         qu = deque(list(filter(lambda x: x[0] == j, node)))
# #         for k, z, pr in qu:
# #             dfs(k,z,end,pr, pre_p+p)

def dfs(s, pre_price, h):
    q = deque(list(filter(lambda x: x[0] == s, node)))
    while q:
        if h == 0:
            for i in range(1, N+1):
                if i ==s: v[i] = True
                else: v[i] = False
        s, e, p = q.popleft()
        if e == end:
            price.append(pre_price + p)
            return
        if not v[e]:
            v[e] = True
            dfs(e, pre_price + p, h+1)

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    node = [list(map(int,input().split())) for _ in range(M)]
    start, end = map(int, input().split())
    v = [False for _ in range(N + 1)]
    price = []
    dfs(start, 0,0)

    print(min(price))
