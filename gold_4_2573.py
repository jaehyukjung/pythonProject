from collections import deque


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v[si][sj] = True

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 0:
                    v2[ci][cj] -= 1

                elif arr[ni][nj] >= 1 and not v[ni][nj]:
                    q.append((ni, nj))
                    v[ni][nj] = True
    return 1

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    while True:
        cnt = 0
        v = [[False] * m for _ in range(n)]
        v2 = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not v[i][j] and arr[i][j] > 0:
                    cnt += bfs(i, j)

        arr = [[arr[x][y] + v2[x][y] if arr[x][y] + v2[x][y] >= 0 else 0 for y in range(m)] for x in range(n)]
        if cnt == 0:
            ans = 0
            break
        if cnt > 1:
            break
        ans += 1

    if ans ==0:
        print(0)
    else:
        print(ans)
