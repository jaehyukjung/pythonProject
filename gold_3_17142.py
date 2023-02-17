from itertools import combinations
from collections import deque


def bfs(change_list):
    q = deque()
    result = 0
    v = [[-1] * N for _ in range(N)]

    for i, j in change_list:
        v[i][j] = 0
        q.append((i,j))

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == -1 and arr[ni][nj] == 0:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))
                result = max(result,v[ni][nj])
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == -1 and arr[ni][nj] == 2:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))


    if list(sum(v,[])).count(-1) != w_cnt:
        return N**2

    return result


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    combi_list = []
    w_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                w_cnt += 1
            if arr[i][j] == 2:
                combi_list.append((i, j))



    ans = N**2
    for change_list in combinations(combi_list, M):
        ans = min(ans, bfs(change_list))

    print(ans if ans != N**2 else -1)

