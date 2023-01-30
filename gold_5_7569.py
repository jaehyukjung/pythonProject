from collections import deque

if __name__ == "__main__":
    M, N, H = map(int, input().split())
    arr = []
    for h in range(H):
        a = [list(map(int, input().split())) for _ in range(N)]
        arr.append(a)

    v = [[[False]*M for _ in range(N)] for i in range(H)]

    q = deque()
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if arr[k][i][j] == 1:
                    q.append((k,i,j))
    while q:
        ck, ci, cj = q.popleft()
        v[ck][ci][cj] = True
        for dk, di, dj in ((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)):
            nk, ni, nj = ck + dk, ci +di, cj + dj
            if 0<=nk<H and 0<=ni<N and 0<=nj<M and not v[nk][ni][nj] and arr[nk][ni][nj] ==0:
                v[nk][ni][nj] =True
                arr[nk][ni][nj] = arr[ck][ci][cj] + 1
                q.append((nk,ni,nj))
    ans = False
    for k in range(H):
        for i in arr[k]:
            if 0 in i:
                ans = True
                break

    if ans:
        print(-1)
    else:
        m =[]
        for k in range(H):
            m.append(max(map(max,arr[k]))-1)
        print(max(m))