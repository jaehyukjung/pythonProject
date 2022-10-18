## 내가 푼 방식 (피보나치 함수 활용) -> 시간초과,.

def fibo(n):
    if n == 1 or n ==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input())

print(fibo(n))
## 찾아서 본 풀이 -> 재귀를 쓰지 않고 푸는 방식

s = [0, 1, 1]
for i in range(3, 91):
  s.append(s[i - 2] + s[i - 1])

print(s[n])