from sys import stdin
from collections import deque
if __name__ == "__main__":

    n = int(stdin.readline())
    q = deque()
    for i in range(1,n+1):
        q.append(i)
    i = 0
    while len(q)!=1:
        if i%2:
            q.append(q.popleft())
        else:
            q.popleft()
        i +=1

    print(q.popleft())
