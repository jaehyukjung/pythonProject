from sys import stdin
import heapq
if __name__ == "__main__":
    n = int(stdin.readline())
    s = []
    for i in range(n):
        num = int(stdin.readline())
        if num:
            heapq.heappush(s,num)
        else:
            if s:
                print(heapq.heappop(s))
            else:
                print(0)
