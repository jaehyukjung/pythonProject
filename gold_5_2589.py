from collections import deque

def bfs(si,sj):
    v = [[False] * M for _ in range(N)]
    map1 = [[1 if arr[i][j] == "L" else 0 for j in range(M)] for i in range(N)]

    v[si][sj] = True
    q = deque()
    q.append((si,sj))
    while q:
        ci,cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<=nj<M and not v[ni][nj] and map1[ni][nj] == 1:
                v[ni][nj] = True
                map1[ni][nj] += map1[ci][cj]
                q.append((ni,nj))
    return max(map(max,map1))

if __name__ =="__main__":
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)]

    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "L":
                q.append((i,j))
    ans = []
    while q:
        i,j = q.popleft()
        ans.append(bfs(i,j))

    print(max(ans)-1)