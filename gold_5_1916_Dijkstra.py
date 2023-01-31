import heapq

if __name__ == "__main__":
    N = int(input())
    M = int(input())

    graph = [[]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        n1, n2, price = map(int, input().split())
        graph[n1].append((n2, price))

    start, end = map(int, input().split())

    dist = [100000 * N+1] * (N+1)
    heap = []

    heapq.heappush(heap,[start,0])
    dist[start] = 0

    while heap:
        node, price = heapq.heappop(heap)
        if price > dist[node]:
            continue

        for i in graph[node]:
            nextNode, nextPrice = i
            cost = nextPrice + price

            if dist[nextNode] > cost:
                dist[nextNode] = cost
                heapq.heappush(heap,[nextNode, cost])
            else:
                continue

    print(dist[end])
