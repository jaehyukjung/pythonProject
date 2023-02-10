from collections import deque

def bfs(si,ei):
    q = deque()
    q.append(si)

    v = [-1]*(N+1)
    v[si] = 0
    while q:
        ci = q.popleft()
        if ci == ei:
            break
        for x in graph[ci]:
            if v[x] == -1:
                v[x] = v[ci] + 1
                q.append(x)

    return v[ei]

if __name__ == "__main__":
    N = int(input())

    a,b = map(int,input().split())

    M = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        i,j = map(int,input().split())
        graph[i].append(j)
        graph[j].append(i)

    print(bfs(a,b))