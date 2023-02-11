from collections import deque

def bfs(si,sj,ei,ej):
    q = deque()
    q.append((si,sj))
    arr[si][sj] = 0
    while q:
        ci,cj = q.popleft()
        if ci==ei and cj == ej:
            return arr[ei][ej]

        for di, dj in ((-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == -1:
                arr[ni][nj] = arr[ci][cj] + 1
                q.append((ni,nj))

if __name__ =="__main__":
    testcase = int(input())

    for _ in range(testcase):
        N = int(input())
        arr = [[-1] * N for i in range(N)]
        si,sj = map(int,input().split())
        ei, ej = map(int,input().split())
        print(bfs(si,sj, ei,ej))