import sys
from collections import deque
def bfs(si,sj):
    q = deque()
    v[si][sj] = True
    q.append((si, sj))
    v2 =[[False] * N for _ in range(N)]
    v2[si][sj] = True
    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<nj<N and not v[ni][nj] and L <= abs(arr[ci][cj] -arr[ni][nj]) <= R:
                v[ni][nj] = True
                v2[ni][nj] = True
                q.append((ni,nj))
    cnt = 0
    total = 0
    for i in range(N):
        for j in range(N):
            if v2[i][j] ==True:
                total += arr[i][j]
                cnt +=1

    for i in range(N):
        for j in range(N):
            if v2[i][j] == True:
                arr[i][j] = total//cnt


def check(arr):
    for i in range(N):
        for j in range(N):
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni, nj = i + di, j + dj
                if 0<=ni<N and 0<nj<N and L <= abs(arr[i][j] -arr[ni][nj]) <= R:
                    return True
    return False

if __name__ == "__main__":
    N, L, R = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    check_pos = True
    i = 0
    while(True):
        v = [[False] * N for _ in range(N)]
        check_pos = check(arr)
        if not check_pos:
            break

        for i in range(N):
            for j in range(N):
                if not v[i][j]:
                    bfs(i,j)

        i+=1

    print(i)