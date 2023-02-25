from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = True
    cnt = 1
    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci + di,cj + dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]==1 and not v[ni][nj]:
                cnt += 1
                v[ni][nj] = True
                q.append((ni,nj))

    return cnt



if __name__ == '__main__':
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    v = [[0]*m for _ in range(n)]
    maximum = 0
    p_cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not v[i][j]:
                p_cnt += 1
                maximum = max(maximum,bfs(i,j))
    print(p_cnt)
    print(maximum)