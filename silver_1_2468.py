import sys
sys.setrecursionlimit(10000)
def dfs(si,sj):
    v[si][sj] = True

    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = si + di, sj + dj
        if 0<= ni<N and 0<=nj<N and not v[ni][nj] and arr[ni][nj] > k:
            dfs(ni, nj)




if __name__ == "__main__":
    r = sys.stdin.readline
    N = int(r())
    arr = [list(map(int,r().split())) for _ in range(N)]

    answer = 1
    for k in range(max(map(max, arr))):
        v = [[False]*N for _ in range(N)]
        count = 0
        for i in range(N):
            for j in range(N):
                if not v[i][j] and arr[i][j] > k:
                    count += 1
                    dfs(i,j)
        answer = max(answer, count)

    print(answer)