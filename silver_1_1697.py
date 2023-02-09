from collections import deque

if __name__ == "__main__":
    S, N = map(int, input().split())
    v = [-1] * (100001)
    v[S] = 0
    q = deque()
    q.append(S)

    while q:
        ci = q.popleft()
        if ci == N:
            break
        for di in (2,-1, 1):
            if di == 2 and 0 <= (ci * di) <= 100000 and v[ci*di] == -1:
                ni = ci * di
                v[ni] = v[ci] +1
                q.appendleft(ni)

            elif -1 <= di <= 1 and 0 <= (ci + di) <= 100000 and v[ci+di]==-1:
                ni = ci + di
                v[ni] = v[ci] + 1
                q.append(ni)
    print(v[N])
