s = input()
i = 0

ans_lst =[]
while i < len(s):
    st = ''
    lst = []
    if s[i] == '<':
        lst.append(s[i])
        i += 1
        while i < len(s):
            if s[i] == '>':
                lst.append(s[i])
                i += 1
                break
            else:
                lst.append(s[i])
                i += 1
        for j in lst:
            st += j
        ans_lst.append(st)

    else:
        lst.append(s[i])
        i += 1
        while i < len(s):
            if s[i] == '<':
                for j in lst:
                    st += j
                ans_lst.append(st)

                break
            else:
                lst.append(s[i])
                i += 1
                if i == len(s) - 1:
                    lst.append(s[i])
                    for j in lst:
                        st += j
                    ans_lst.append(st)
                    break



ans_lst2 =[]
for i, s in enumerate(ans_lst):
    if s[0] =='<':
        continue
    else:
        lst = s.split()
        w = ''
        for j, word in enumerate(lst):
            lst_word = []
            for q in word:
                lst_word.insert(0,q)

            for q in lst_word:
                w += q
            if j < len(lst)-1:
                w += ' '
        ans_lst[i] = w
for i in ans_lst:
    print(i,end='')