from collections import deque

def bfs(lst):
    q = deque()
    v = [[False]*(m) for _ in range(n)]
    for x in lst:
        q.append((x[0],x[1]))
        v[x[0]][x[1]] = True
    while q:
        ci,cj = q.popleft()

        if ci == n-1:
            break
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci + di, cj +dj
            if 0<=ni<n and 0<=nj <m:
                if not v[ni][nj] and arr[ni][nj] == "0":
                    q.append((ni,nj))
                    v[ni][nj] = True

    if True in v[n-1]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    n,m= map(int,input().split())
    arr = [input() for _ in range(n)]
    lst = []

    for i in range(m):
        if arr[0][i] == "0":
            lst.append((0,i))

    bfs(lst)