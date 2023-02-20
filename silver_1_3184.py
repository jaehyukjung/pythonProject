from collections import deque

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    if arr[si][sj] == "v":
        sheep, wolf = 0, 1
    else:
        sheep, wolf = 1,0
    while q:
        ci,cj = q.popleft()
        v[ci][cj] = True

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+ di, cj + dj
            if 0<=ni<n and 0<=nj <m and arr[ni][nj] != "#":
                if not v[ni][nj] and arr[ni][nj] == "o":
                    sheep +=1
                    v[ni][nj] = True
                    q.append((ni,nj))
                elif not v[ni][nj] and arr[ni][nj] == "v":
                    wolf += 1
                    v[ni][nj] = True
                    q.append((ni,nj))
                elif not v[ni][nj] and arr[ni][nj] == ".":
                    v[ni][nj] = True
                    q.append((ni,nj))
    if sheep > wolf:
        return sheep, 0
    else :
        return 0, wolf

if __name__ == "__main__":
    n,m = map(int, input().split())
    arr = [input() for _ in range(n)]
    v = [[False]*m for _ in range(n)]
    s,w = 0,0
    for i in range(n):
        for j in range(m):
            if not v[i][j] and (arr[i][j] == "o" or arr[i][j]=="v"):
                new_s, new_w = bfs(i,j)
                s += new_s
                w += new_w
    print(s,w)
