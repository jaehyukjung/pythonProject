if __name__ == "__main__":
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    R, C, K = map(int,input().split())
    maps = [list(input()) for _ in range(R)]
    visited = [[0 for _ in range(C)] for _ in range(R)]
    visited[R-1][0] =1
    answer = 0
    def bfs(x,y,k):
        global answer

        if k == K:
            if (x,y) ==(0,C-1): answer+=1
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <R and 0<= ny <C and visited[nx][ny] == 0 and maps[nx][ny] != 'T':
                visited[nx][ny] = 1
                bfs(nx,ny,k+1)
                visited[nx][ny] = 0


    bfs(R-1,0,1)
    print(answer)