def bfs(si, sj, ei, ej):
    q = []

    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        if (ci,cj) == (ei,ej):
            return


        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<= nj< M and arr[ni][nj] == 1 and v[ni][nj] ==0:
                v[ni][nj] = 1
                q.append((ni,nj))
            elif 0<=ni<N-1 and 0<= nj< M-1:
                v[ni][nj] = 1
    return

if __name__ == "__main__":
    testcase = int(input())
    while testcase > 0:
        testcase -= 1
        N, M, ea = map(int, input().split())
        # map 설정
        arr = [[0]*M for _ in range(N)]
        for _ in range(ea):
            i,j = map(int, input().split())
            arr[i][j] = 1

        v = [[0]*M for _ in range(N)]   # 방문 표시 지도
        count = 0
        for i in range(N):
            for j in range(M):
                if v[i][j] == 0 and arr[i][j] == 1:
                    bfs(i,j,N-1, M-1)
                    count += 1
                else: v[i][j] = 1

        print(count)
