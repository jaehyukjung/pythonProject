if __name__ == '__main__':
    n = int(input())

    RGB = []


    arr2 = []
    for i in range(n): # 이것 때문에 계속 런타임 오류 뜬것
        arr2 = list(map(int, input().split()))
        RGB.append(arr2)

    price = []

    for i in range(1, n):
        RGB[i][0] = min(RGB[i - 1][1], RGB[i - 1][2]) + RGB[i][0]
        RGB[i][1] = min(RGB[i - 1][0], RGB[i - 1][2]) + RGB[i][1]
        RGB[i][2] = min(RGB[i - 1][0], RGB[i - 1][1]) + RGB[i][2]

    print(min(RGB[n - 1]))


