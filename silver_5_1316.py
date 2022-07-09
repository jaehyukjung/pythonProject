n = int(input())
cnt = n

for i in range(n):
    s = input()
    j = 1
    arr =[s[0]]
    while j<len(s):
        if s[j]==s[j-1] :
           j += 1
        elif s[j] not in arr :
            arr.append(s[j])
            j += 1
        else :
            cnt -= 1
            break


print(cnt)