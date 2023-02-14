from collections import deque


def bfs(si, sj, ei, ej):
    q = deque()
    q.append((si, sj, 1))
    v = [[[0] * 2 for j in range(M)] for i in range(N)]
    v[si][sj][1] = 1
    while q:
        ci, cj, b = q.popleft()
        if ci == ei and cj == ej:
            return v[ei][ej][b]

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj][b] == 0 and arr[ni][nj] == 0:
                v[ni][nj][b] = v[ci][cj][b] + 1
                q.append((ni, nj, b))
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and b == 1:
                v[ni][nj][b - 1] = v[ci][cj][b] + 1
                q.append((ni, nj, b - 1))
    return -1


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        s = input()
        arr2 = [0 if s[i] == "0" else 1 for i in range(M)]
        arr.append(arr2)

    print(bfs(0, 0, N - 1, M - 1))
