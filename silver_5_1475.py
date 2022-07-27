s = input()
lst = [str(x) for x in range(10)]
dic = {}
for x in lst:
    dic[x] = 0

for i in s:
    for x in lst:
        if i == x:
            dic[x] += 1
if (dic['6']+dic['9']) %2 ==0:
    dic['6'] = int((dic['6'] + dic['9'])/2)
else:
    dic['6'] = int((dic['6'] + dic['9'])//2 +1)

dic.pop('9')
print(max(dic.values()))