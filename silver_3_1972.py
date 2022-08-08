while True:
    s = input()
    if s =='*':
        break
    else:
        if len(s) > 1:
            cnt = 0
            for i in range(1,len(s)):
                ans_set = set()
                for j in range(0,len(s)-i):
                    ans_set.add(s[j]+s[j+i])
                if len(ans_set) == len(s) - i:
                    cnt += 1
            if cnt == len(s) - 1:
                print(f"{s} is surprising.")
            else:
                print(f"{s} is NOT surprising.")
        else:
            print(f"{s} is surprising.")