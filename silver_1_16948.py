from collections import deque

def bfs(si,sj,ei,ej):
    q = deque()
    q.append((si,sj))
    v = [[-1]*n for _ in range(n)]
    v[si][sj] = 0
    while q:
        ci,cj = q.popleft()
        if ci == ei and cj ==ej:
            return v[ci][cj]

        for di,dj in ((-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<n:
                if v[ni][nj] == -1:
                    v[ni][nj] = v[ci][cj]  +1
                    q.append((ni,nj))

    return -1

if __name__ == "__main__":
    n = int(input())
    si,sj,ei,ej = map(int,input().split())
    print(bfs(si,sj,ei,ej))