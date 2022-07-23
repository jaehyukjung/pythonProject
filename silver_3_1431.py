testcase = int(input())

lst = [input() for _ in range(testcase)]

def sort_num(s):
    answer = 0
    for x in s:
        if x.isupper():
            continue
        else:
            answer += int(x)
    return answer

lst = sorted(lst, key = lambda x : (len(x), sort_num(x),x))

for i in lst:
    print(i)

# while len(lst) != 0:
#     cnt = 1
#     m = len(lst[0])
#     ans_lst = []
#     for i in lst:
#         if len(i) < m:
#             m = len(i)
#             ans_lst.clear()
#             ans_lst.append(i)
#         elif len(i) == m:
#             ans_lst.append(i)
#
#     if len(ans_lst) == 1:
#         print(ans_lst[0])
#         lst.remove(ans_lst[0])
#     else:
#         ans_lst2 = []
#         while len(ans_lst) != 0:
#             min = 9 * len(ans_lst[0])
#             for i in ans_lst:
#                 cnt = 0
#
#                 for x in i:
#                     if x.isupper():
#                         continue
#                     else:
#                         cnt += int(x)
#                 if cnt < min:
#                     min = cnt
#                     ans_lst2.clear()
#                     ans_lst2.append(i)
#                 elif cnt == min:
#                     ans_lst2.append(i)
#             if len(ans_lst2) <2:
#                 print(ans_lst2[0])
#                 ans_lst.remove(ans_lst2[0])
#                 lst.remove(ans_lst2[0])
#             else:
#                 lst.sort()
#                 if len(lst) > 0:
#                     print(lst.pop(0))
#                 else:
#                     break


