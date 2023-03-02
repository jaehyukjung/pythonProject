from collections import deque


def bfs(si, h):
    q = deque()
    q.append((si, h))
    v = [False] * (n + 1)
    v[si] = True
    lst = []
    while q:
        ci, h = q.popleft()
        if h == 2:
            break
        for ni in graph[ci]:
            if not v[ni]:
                v[ni] = True
                q.append((ni, h + 1))
                lst.append(ni)

    print(len(lst))


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    bfs(1, 0)
