from math import *
n = int(input())

for _ in range(n):
    left, right = map(int, input().split())
    print(comb(right,left))