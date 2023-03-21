from sys import stdin

if __name__ == "__main__":
    n = stdin.readline()
    s = n
    l = n
    s = n.replace('6','5')
    a,b = map(int,s.split())
    print(a+b, end=" ")
    l = n.replace('5','6')
    a, b = map(int, l.split())
    print(a + b)
    print(1)
    print(2)