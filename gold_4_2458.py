from collections import deque

def bfs(si):
    q1 = deque(arr[si][0])
    q2 = deque(arr[si][1])
    v = [False] * (N + 1)
    v[0] = True
    v[si] = True
    while q1:
        ci = q1.popleft()
        if not v[ci]:
            v[ci] = True
            l = deque(arr[ci][0])
            q1 = q1 + l

    v2 = [False] * (N + 1)
    v2[0] = True
    v2[si] = True
    while q2:
        ci = q2.popleft()
        if not v2[ci]:
            v2[ci] = True
            l = deque(arr[ci][1])
            q2 = q2 + l
    for i in range(N+1):
        if v[i] or v2[i]:
            v[i] = True

    if False in v:
        return 0
    else:
        return 1


if __name__ == "__main__":
    # N, M = map(int, input().split())
    # arr = [[[] for _ in range(2)]*(N+1) for i in range(N + 1)]
    #
    # for _ in range(M):
    #     a, b = map(int, input().split())
    #     arr[a][0].append(b)
    #     arr[b][1].append(a)
    #
    #
    # cnt = 0
    # for i in range(1, N + 1):
    #     cnt += bfs(i)
    #
    # print(cnt)

    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for i in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        arr[a][b] = 1

    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if arr[i][k] ==1 and arr[k][j]==1:
                    arr[i][j] =1
    ans = 0
    for i in range(1,1+N):
        cnt = 0
        for j in range(1,1+N):
            cnt += (arr[i][j] + arr[j][i])
        if cnt == (N-1):
            ans += 1
    print(ans)
