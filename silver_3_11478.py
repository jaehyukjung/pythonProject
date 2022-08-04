s = input()

ans = set()

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        x = s[i:j]
        ans.add(x)

print(len(ans))