from collections import deque


def bfs(si):
    q = deque()
    q.append(si)
    v = [0] * (n+1)
    v[si] = 1
    lst = []
    maximum = 0
    while q:
        ci = q.popleft()

        for ni in arr[ci]:
            if v[ni] == 0:
                v[ni] = v[ci] + 1
                if maximum == v[ni]:
                    lst.append(ni)
                elif maximum < v[ni]:
                    lst = [ni]
                    maximum = v[ni]
                q.append(ni)
    lst.sort()
    print(lst[0], maximum-1, len(lst))



if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = [[] for _ in range(n+1)]

    for i in range(m):
        a,b = map(int,input().split())

        arr[a].append(b)
        arr[b].append(a)

    bfs(1)