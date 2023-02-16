from itertools import combinations
from collections import deque


def bfs(change_list):
    q = deque(change_list)
    v = [[-1] * N for _ in range(N)]
    for i, j in change_list:
        v[i][j] = 0
    min_ans = 0
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == -1 and arr[ni][nj] == 0:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))
                min_ans = max(min_ans,v[ni][nj])
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == -1 and arr[ni][nj] == 2:
                v[ni][nj] = v[ci][cj]
                q.append((ni, nj))

    a = 0
    for i in range(N):
        if v[i].count(-1) != arr[i].count(1):
            return N**2

    return min_ans


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

    combi_q = deque(combinations(combi_list, M))

    ans = []
    while combi_q:
        change_list = combi_q.popleft()
        ans.append(bfs(change_list))

    print(min(ans))

n = int(input())
arr = list(map(int,input().split()))
m = int(input())

print(arr.count(m))