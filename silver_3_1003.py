n = int(input())

for i in range(n):
    fibo = int(input())
    if fibo == 0:
        print(1, 0)
    elif fibo ==1:
        print(0, 1)
    else:
        fibo0 = [0, 1]
        fibo1 = [1, 1]

        for j in range(2,fibo):
            fibo0.append(fibo0[j - 1] + fibo0[j - 2])
            fibo1.append(fibo1[j - 1] + fibo1[j - 2])

        print(fibo0[fibo-1], fibo1[fibo-1])