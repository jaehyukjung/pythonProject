from collections import deque

def bfs(si,h):
    q = deque()
    v = [False]*(n+1)
    q.append((si,h))
    v[si] = True

    lst = []
    while q:
        ci, h = q.popleft()
        if h == k + 1:
            break

        if h == k:
            lst.append(ci)

        for ni in graph[ci]:
            if not v[ni]:
                v[ni] = True
                q.append((ni,h+1))

    if len(lst) ==0:
        print(-1)

    else:
        lst.sort()
        for x in lst:
            print(x)

if __name__ == "__main__":
    n,m, k,s = map(int,input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)

    bfs(s,0)