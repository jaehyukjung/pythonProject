def bfs(si, sj, ei, ej):
    q = []  # 큐 ( 값들이 들어가는 곳)
    v = [[0]*M for _ in range(N)]

    q.append((si,sj)) # 현재 위치
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        # 정답 구간
        if (ci, cj) == (ei, ej):
            return v[ei][ej]

        # 4방향 범위
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<= nj<M and v[ni][nj] == 0 and arr[ni][nj] ==1:
                v[ni][nj] = v[ci][cj]+1
                q.append((ni,nj))


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    ans = bfs(0,0,N-1,M-1)
    print(ans)