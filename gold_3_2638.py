from collections import deque

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v1[si][sj] =True
    while q:
        ci,cj = q.popleft()

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci + di , cj + dj

            if 0<=ni<n and 0<= nj <m:
                if arr[ni][nj] == 0 and not v1[ni][nj]:
                    v1[ni][nj] =True
                    q.append((ni,nj))

                if arr[ni][nj] == 1:
                    v2[ni][nj] -= 1



if __name__ =="__main__":
    n,m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    hour = 0
    while True:
        cnt = 0
        v1 = [[False]*m for _ in range(n)]
        v2= [[0]*m for _ in range(n)]
        # for i in range(n):
        #     for j in range(m):
        #         if arr[i][j] == 0 and not v1[i][j]:
        #             bfs(i,j)
        #         if arr[i][j] == 1:
        #             cnt +=1
        bfs(0, 0)

        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1 and v2[i][j] <= -2:
                    arr[i][j] = 0
                    cnt += 1


        hour += 1
        if cnt == 0:
            print(hour-1)
            break

