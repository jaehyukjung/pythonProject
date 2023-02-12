if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    dp1 = [1]*N
    dp2 = [1]*N
    for i in range(1,N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp1[i] = max(dp1[i], dp1[j] + 1)

    arr.reverse()
    for i in range(1,N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp2[i] = max(dp2[i], dp2[j] + 1)
    dp2.reverse()
    dp = [dp1[i] + dp2[i] for i in range(N)]

    print(max(dp)-1)
