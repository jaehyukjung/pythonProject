word = input()

ans_lst = [word[x:] for x in range(len(word))]
ans_lst.sort()

for x in ans_lst:
    print(x)

