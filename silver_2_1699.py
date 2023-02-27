import math
from itertools import combinations_with_replacement

if __name__ == "__main__":
    n = int(input())
    max_num = int(math.sqrt(n))
    lst = [i**2 for i in range(1,max_num+1)]


    ans = 1
    while True:
        for x in combinations_with_replacement(lst, ans):
            if sum(x) == n:
                print(ans)
                n = 0
                break
        if n == 0:
            break

        ans += 1

