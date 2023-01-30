from collections import deque

if __name__ == "__main__":
    M, N = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    v = [[False]*M for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i,j))
    while q:
        ci, cj = q.popleft()
        v[ci][cj] = True
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci +di, cj + dj
            if 0<=ni<N and 0<=nj<M and not v[ni][nj] and arr[ni][nj] ==0:
                v[ni][nj] =True
                arr[ni][nj] = arr[ci][cj] + 1
                q.append((ni,nj))
    ans = False
    for i in arr:
        if 0 in i:
            ans = True
    if ans:
        print(-1)
    else:
        print(max(map(max,arr))-1)