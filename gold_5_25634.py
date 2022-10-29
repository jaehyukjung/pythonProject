if __name__ == "__main__":
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    sum = [arr1[0]]
    for i in range(1,n):
        sum.append(sum[i-1]+arr1[i])
    sum1 = 0
    for i in range(n):
        if arr2[i] ==0:
            sum += arr1[i]
        else :
            max = (max if max > sum else sum)
            sum = 0
            sum1 += arr1[i]
    print(max+sum1)


