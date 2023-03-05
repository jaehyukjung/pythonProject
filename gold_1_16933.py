from collections import deque
from sys import stdin

if __name__ == "__main__":
    input = stdin.readline()
    n, m, k = map(int, input().split())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    MAX = float('inf')
    q = deque()
    v = [[[MAX] * (k + 1) for x in range(m)] for _ in range(n)]
    v[0][0][k] = 0
    q.append((0, 0, 1, k))

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

                if arr[ni][nj] == 0 and v[ni][nj][bk] > t:
                    v[ni][nj][bk] = t
                    q.append((ni, nj, t + 1, bk))

                if arr[ni][nj] == 1 and bk and v[ni][nj][bk - 1] > t:
                    if day:
                        v[ni][nj][bk - 1] = t
                        q.append((ni, nj, t + 1, bk - 1))
                    else:
                        q.append((ci, cj, t + 1, bk))

    print(result if result < MAX else -1)
