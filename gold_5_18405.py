from collections import deque

def bfs(lst):
    q = deque()
    for i,j in lst:
        q.append((i,j,0))


    while q:
        ci,cj,h = q.popleft()
        if h == s:
            break
        for di,dj in ((0,1),(0,-1),(-1,0),(1,0)):
            ni, nj = ci+ di , cj +dj

            if 0<=ni<n and 0<=nj<n and arr[ni][nj] ==0:
                arr[ni][nj] = arr[ci][cj]
                q.append((ni,nj,h+1))

    print(arr[ei-1][ej-1])


if __name__== "__main__":
    n, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    s,ei,ej = map(int, input().split())
    lst = []
    for k in range(1,K+1):
        for i in range(n):
            for j in range(n):
                if arr[i][j] == k:
                    lst.append((i,j))
    bfs(lst)