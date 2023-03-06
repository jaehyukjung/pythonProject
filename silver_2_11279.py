from sys import stdin
import heapq

if __name__ == "__main__":
    n = int(stdin.readline())

    lst = []
    for i in range(n):
        num = int(stdin.readline())
        if num:
            heapq.heappush(lst,-1*num)
        else:
            if lst:
                print(-1* heapq.heappop(lst))
            else:
                print(0)
