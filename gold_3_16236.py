from collections import deque


def bfs(si, sj, h):
    q = deque()
    v = [[0] * N for _ in range(N)]
    q.append((si, sj))
    new_lst = []
    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] <= h and v[ni][nj] == 0:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))
                if 0 < arr[ni][nj] < h:
                    new_lst.append([ni, nj, v[ni][nj]])
    if len(new_lst) == 0:
        return False
    else:
        new_lst.sort(key=lambda x: (x[2], x[0], x[1]))
        return (new_lst[0][0], new_lst[0][1], new_lst[0][2])


def check():
    count = 0
    for x in arr:
        for j in range(1, h):
            if j in x:
                count += 1

    if count == 0:
        return False
    else:
        return True


if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    h = 2
    ea = 0
    ans = 0

    while check():
        ci, cj = 0, 0  # 현재 위치 찾기
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 9:
                    ci, cj = i, j
                    arr[i][j] = 0
                    break

        t = bfs(ci, cj, h)
        if t == False:
            break

        x, y, dist = bfs(ci, cj, h)
        ans += dist
        arr[x][y] = 9
        ea += 1
        if ea == h:
            h += 1
            ea = 0

    print(ans)
