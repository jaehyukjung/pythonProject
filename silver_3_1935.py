import string

upper = [i for i in string.ascii_uppercase]
N = int(input())
s = input()
dic = {}
lst = []


for i in range(N):
    dic[upper[i]] = int(input())


for i in range(len(s)):
    if s[i] =='*':
        top1 = lst.pop()
        top2 = lst.pop()
        lst.append(top1*top2)
    elif s[i] == '/':
        top1 = lst.pop()
        top2 = lst.pop()
        lst.append(top2 / top1)
    elif s[i] == '+':
        top1 = lst.pop()
        top2 = lst.pop()
        lst.append(top1 + top2)
    elif s[i] == '-':
        top1 = lst.pop()
        top2 = lst.pop()
        lst.append(top2 - top1)
    else:
        for j in dic:
            if s[i] == j:
                lst.append(dic[j])

print(f"{lst[0]:.2f}")