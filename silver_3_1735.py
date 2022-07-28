n1, m1 = map(int, input().split())
n2, m2 = map(int, input().split())

ans1, ans2 = n2*m1 + n1*m2, m1*m2

d = 2
lst =[]
x = min(ans1, ans2)
while d <= x:
    if x % d == 0:
        lst.append(d)
        x = x / d
    else:
        d += 1

for x in lst:
    if ans1 % x ==0 and ans2 % x ==0:
        ans1 /= x
        ans2 /= x

print(int(ans1), int(ans2))