# number = input()
#
# lst =[x for x in number]
# sum =0
# for x in number:
#     sum += int(x)
#
# if '0' in lst and sum % 3 == 0:
#     lst.sort(reverse=True)
#     s=''
#     for x in lst:
#        s += x
#     print(s)
#
# else:
#     print(-1)


cash = int(input())
n = int(input())
sum = 0
for _ in range(n):
    x, y = map(int, input().split())
    sum = sum + x*y
if cash == sum:
    print('Yes')
else:
    print('No')
