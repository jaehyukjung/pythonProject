from collections import deque
from itertools import combinations

def bfs(si,sj):
    q = deque()
    v[si][sj] = True
    q.append((si,sj))

    while q:
        ci, cj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<=nj<M and not v[ni][nj] and new_arr[ni][nj] == 0:
                new_arr[ni][nj] = 2
                v[ni][nj] = True
                q.append((ni,nj))


if __name__ == "__main__":
    N,M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    combi_list = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                combi_list.append((i,j))


    combi_q = deque(combinations(combi_list,3))
    ans = []
    while combi_q:
        change_list = combi_q.popleft()
        new_arr = [[arr[i][j] for j in range(M)] for i in range(N)]


        for i,j in change_list:
            new_arr[i][j] = 1

        v = [[False] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if new_arr[i][j] == 2 and not v[i][j]:
                   bfs(i,j)
        cnt = [x.count(0) for x in new_arr]
        ans.append(sum(cnt))

    print(max(ans))