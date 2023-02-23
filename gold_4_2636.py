from collections import deque


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v1[si][sj] = True
    cnt = 0
    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni,nj = ci+di, cj+dj

            if 0<=ni<n and 0<=nj<m:
                if arr[ni][nj] == 1 and v2[ni][nj] == 0:
                    v2[ni][nj] = -1
                    cnt += 1
                elif arr[ni][nj] == 0 and not v1[ni][nj]:
                    v1[ni][nj] = True
                    q.append((ni,nj))

    return cnt

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    hour = 0
    ans = 0
    while True:
        v1 = [[False] * m for _ in range(n)]
        v2 = [[0] * m for _ in range(n)]
        total_cnt = 0


        total_cnt += bfs(0, 0)

        for i in range(n):
            for j in range(m):
                arr[i][j] = arr[i][j] + v2[i][j]

        if total_cnt == 0:
            break
        else:
            hour += 1
            ans = total_cnt
    print(hour)
    print(ans)