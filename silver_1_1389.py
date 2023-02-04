import sys
from collections import deque

def bfs(si):
    v = [0 for _ in range(N+1)]
    v[si] = 1
    q = deque()
    q.append(si)

    while q:
        ci = q.popleft()
        for i in graph[ci]:
            if v[i] == 0:
                v[i] = v[ci] + 1
                q.append(i)

    return sum(v) - 5

if __name__ == "__main__":
    N,M = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = []
    for i in range(1,N+1):
        ans.append(bfs(i))

    print(ans.index(min(ans))+1)
