#dfs
if __name__ == "__main__":
    maps = [list( input().split()) for _ in range(5)]
    max_num = 6
    result = []
    def dfs(x,y,number):
        if len(number)== max_num:
            if number not in result:
                result.append(number)
            return

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 5 and 0 <= ny < 5:
                dfs(nx,ny,number + maps[nx][ny])


    for i in range(5):
        for j in range(5):
            dfs(i,j,maps[i][j])

    print(len(result))

