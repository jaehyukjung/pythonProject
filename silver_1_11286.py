from sys import stdin
import heapq

if __name__ == "__main__":
    n = int(stdin.readline())

    lst1 = []
    lst2 = []
    for i in range(n):
        num = int(stdin.readline())
        if num!= 0:
            if num <0:
                heapq.heappush(lst2,-1*num)
            else:
                heapq.heappush(lst1, num)
        else:
            if lst1 and not lst2:
                print(heapq.heappop(lst1))
            elif lst2 and not lst1:
                print(-1*heapq.heappop(lst2))

            elif lst1 and lst2:
                if heapq.heappushpop(lst1,lst1[0]) >= heapq.heappushpop(lst2,lst2[0]):
                    print(-1* heapq.heappop(lst2))
                else:
                    print(heapq.heappop(lst1))
            else:
                print(0)
