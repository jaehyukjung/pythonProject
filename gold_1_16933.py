from collections import deque
from sys import stdin

def bfs(si, sj):
    q = deque()
    v = [[[MAX] * (k + 1) for x in range(m)] for _ in range(n)]
    v[si][sj][k] = 0
    q.append((si, sj, 1, k))

    result = MAX
    while q:
        ci, cj, t, bk = q.popleft()
        if ci == n - 1 and cj == m - 1:
            result = min(result, t)
            continue
        day = t % 2
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m:

                if arr[ni][nj] == "0" and v[ni][nj][bk] > t:
                    v[ni][nj][bk] = t
                    q.append((ni, nj, t+1,bk))

                elif arr[ni][nj] == "1" and bk and v[ni][nj][bk-1] > t:
                    if day:
                        v[ni][nj][bk-1] = t
                        q.append((ni,nj,t+1,bk-1))
                    else:
                        q.append((ci, cj, t+1, bk))


    print(result if result<MAX else -1)
if __name__ == "__main__":
    n, m, k = map(int, stdin.readline().split())
    arr = [stdin.readline() for _ in range(n)]
    MAX = 100000000000000000000000
    bfs(0, 0)
