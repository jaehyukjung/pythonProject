number = input()

lst =[x for x in number]
sum =0
for x in number:
    sum += int(x)

if '0' in lst and sum % 3 == 0:
    lst.sort(reverse=True)
    s=''
    for x in lst:
       s += x
    print(s)

else:
    print(-1)




