def bfs(si,ei):
    q = list(filter(lambda x: x[0] == si, lst))
    c1, c2 = 0, 0
    while q:
        c1, c2 = q.pop(0)
        if c1 == ei:
            return
        if c1 in arr:
            arr.remove(c1)
        if c2 in arr:
            arr.remove(c2)
            node_lst = list(filter(lambda x : x[0] == c2 and x[1] in arr, lst))
            q.extend(node_lst)
    return

if __name__ == "__main__":
    N, M = map(int, input().split())
    lst = []
    for i in range(M):
        n1,n2 = map(int, input().split())
        if n1 > n2:
            temp = n2
            n2 = n1
            n1 = temp
        lst.append((n1,n2))

    arr = [i+1 for i in range(N)]
    count = 0
    while arr:
        bfs(arr.pop(0),6)
        count += 1

    print(count)