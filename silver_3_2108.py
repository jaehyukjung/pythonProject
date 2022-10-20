if __name__ == "__main__":
    n = int(input())

    arr = []
    for i in range(n):
        arr.append(int(input()))


    print(round(sum(arr)/len(arr)))

    arr.sort()
    print(arr[int(n/2)])

    max_arr =[arr[0]]
    count = 1
    M_count = 1
    if n == 1:
        print(arr[0])
    else:
        for i in range(1,n):
            if arr[i-1] == arr[i]:
                count += 1
            else:
                count = 1

            if count == M_count:
                max_arr.append(arr[i])
            elif count > M_count:
                M_count = count
                max_arr = [arr[i]]

        if len(max_arr) > 1:
            print(max_arr[1])
        else:
            print(max_arr[0])

    print(arr[n-1] - arr[0])
