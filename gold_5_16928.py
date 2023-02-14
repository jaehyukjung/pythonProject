from collections import deque


def bfs(si, ei):
    q= deque()
    q.append(si)
    v = [-1]*(101)
    v[si] = 0

    while q:
        ci = q.popleft()
        if ci == ei:
            return v[ei]
        for di in range(1,7):
            ni= ci + di
            if ni <=100 and v[ni] ==-1:
                if ni in lad.keys():
                    ni = lad[ni]
                if v[ni] ==-1:
                    v[ni] = v[ci] + 1
                    q.append(ni)


if __name__ == "__main__":
    n, m = map(int, input().split())
    lad = {}
    for i in range(n+m):
        a, b = map(int, input().split())
        lad[a] = b

    print(bfs(1,100))