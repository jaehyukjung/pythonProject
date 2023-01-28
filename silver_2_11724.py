def bfs(si):
    q = [si]
    v[si] = True
    while q:
        node = q.pop(0)
        for i in graph[node]:
            if not v[i]:
                v[i] = True
                q.append(i)


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range((N+1))]
    for i in range(M):
        n1,n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    v = [False for _ in range(N+1)]
    count = 0

    for i in range(1,N+1):
        if v[i] == False:
            if not graph[i]:
                count += 1
                v[i] =True
            else:
                bfs(i)
                count +=1

    print(count)