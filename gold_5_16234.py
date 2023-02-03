from collections import deque
def bfs(si,sj,h):
    q = deque()
    v[si][sj] = h
    q.append((si, sj))
    cnt, total = 1, arr[si][sj]
    ch_list = []
    while q:
        ci, cj = q.popleft()
        ch_list.append((ci,cj))
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<=nj<N and not v[ni][nj] and L <= abs(arr[ci][cj] -arr[ni][nj]) <= R:
                v[ni][nj] = h
                q.append((ni,nj))
                total += arr[ni][nj]
                cnt += 1
    for i, j in ch_list:
        arr[i][j] = total//cnt



def check(arr):
    for i in range(N):
        for j in range(N):
            for di, dj in ((1,0),(0,1)):
                ni, nj = i + di, j + dj

                if 0 <= ni<N and 0 <=nj<N:
                    m = abs(arr[i][j] - arr[ni][nj])
                    if L <= m <= R:
                        return True
    return False

if __name__ == "__main__":
    N, L, R = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    check_pos = True
    ans = 0
    check_pos = check(arr)
    while(check_pos):
        if not check_pos:
            break
        h = 1
        v = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if v[i][j] == 0:
                    bfs(i,j,h)
                    h += 1
        ans += 1
        check_pos = check(arr)

    print(ans)