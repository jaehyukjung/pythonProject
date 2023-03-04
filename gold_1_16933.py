from collections import deque
from sys import stdin

def bfs(si, sj):
    q = deque()
    v = [[[0] * (k + 1) for x in range(m)] for _ in range(n)]
    v[si][sj][0] = 1
    q.append((si, sj, 0, 0))
    lst = []

    while q:
        ci, cj, bk, cnt = q.popleft()
        if ci == n - 1 and cj == m - 1:
            lst.append(v[ci][cj][bk])
            continue

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m:

                if arr[ni][nj] == "0":
                    if (v[ni][nj][bk] == 0 or v[ni][nj][bk] > v[ci][cj][bk] + 1):
                        v[ni][nj][bk] = v[ci][cj][bk] + 1
                        q.append((ni, nj, bk, cnt + 1))

                elif arr[ni][nj] == "1" and cnt % 2 == 0 and bk+1 <= k:
                    if v[ni][nj][bk+1] == 0 or v[ni][nj][bk + 1] > v[ci][cj][bk] + 1:
                        v[ni][nj][bk + 1] = v[ci][cj][bk] + 1
                        q.append((ni, nj, bk + 1, cnt + 1))


                elif arr[ni][nj] == "1" and cnt % 2 == 1:
                    q.append((ci, cj, bk, cnt + 1))
                    # if v[ni][nj][bk+1] == 0 or v[ni][nj][bk + 1] > v[ci][cj][bk] + 2:
                    #     v[ni][nj][bk + 1] = v[ci][cj][bk] + 2
                    #     q.append((ni, nj, bk + 1, cnt + 2))

    if len(lst) == 0:
        print(-1)
    else:
        print(min(lst))
if __name__ == "__main__":
    n, m, k = map(int, stdin.readline().split())
    arr = [stdin.readline() for _ in range(n)]
    bfs(0, 0)
