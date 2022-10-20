if __name__ == "__main__":
    N, M = map(int, input().split())

    count = 0
    arr = [x for x in range(1,N+1)]
    w_lst = list(map(int, input().split()))
    my_point = 0

    for x in w_lst:
        if (arr.index(x) > my_point) and (arr.index(x) - my_point >= len(arr) - arr.index(x) + my_point):
            count += (len(arr) - arr.index(x) + my_point)
        elif (arr.index(x) > my_point) and (arr.index(x) - my_point < len(arr) - arr.index(x) + my_point):
            count += arr.index(x) - my_point
        elif (arr.index(x) < my_point) and (my_point - arr.index(x) >= len(arr) + arr.index(x) - my_point):
            count += (len(arr) + arr.index(x) - my_point)
        elif (arr.index(x) < my_point) and (my_point - arr.index(x) < len(arr) + arr.index(x) - my_point):
            count += (my_point - arr.index(x))

        if arr.index(x) == len(arr)-1:
            my_point = 0
        else: my_point = arr.index(x)
        arr.remove(x)

    print(count)