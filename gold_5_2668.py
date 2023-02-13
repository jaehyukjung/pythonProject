def dfs(si, lst):
    for x in arr[si]:
        if v[x]:
            while lst:
                a = lst.pop()
                ans.add(a)
                if x == a:
                    break
            return

        v[x] = True
        dfs(x,lst+[x])
        v[x] = False


if __name__ == "__main__":
    N = int(input())
    arr = [[] for i in range(N+1)]
    for i in range(1,N+1):
        arr[int(input())].append(i)
    v = [False] * (N+1)


    ans = set()
    for i in range(1,N+1):
        dfs(i,[])
    ans = sorted(list(ans))
    print(len(ans), *ans, sep='\n')
