from collections import deque


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v = [[0 if arr[i][j] == 0 else -1 for j in range(M)] for i in range(N)]
    while q:
        ci, cj = q.popleft()
        for di, dj in ((0, -1), (0, 1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))

            elif 0 <= ni < N and 0 <= nj < M and v[ni][nj] == -1:
                return v[ci][cj] + 1


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    lst = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                lst.append(bfs(i, j))

    print(max(lst))
