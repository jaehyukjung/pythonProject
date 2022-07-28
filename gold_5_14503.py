N, M = map(int, input().split())

x, y, d = (map(int,input().split()))

robot_map = [list(map(int,input().split())) for _ in range(N)]

ans = 0
while True:
    if robot_map[x][y] == 0:
        ans += 1
        if d > 0:
            d -= 1
        else:
            d = 3

    elif robot_map[x][y] == 2:
        if d == 0 and robot_map[x-1][y] != 1:
            x -= 1
        elif d == 1 and robot_map[x][y+1] != 1:
            y += 1
        elif d == 2 and robot_map[x-1][y] != 1:
            x += 1
        elif d == 3 and robot_map[x][y-1] != 1:
            d -= 1
