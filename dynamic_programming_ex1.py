## 막대기 길이 문제

height = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

n = int(input())

def df(n):
    price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    q = -1
    R = [0]
    for i in range(1,n+1):
        for j in range(i):
            q = max(q,price[i-j] +R[j])

        R.append(q)

    return R[n]

print(df(n))