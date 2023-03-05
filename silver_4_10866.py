from sys import stdin

def queue(s):
    s = s.split()

    if s[0] == "push_front":
        lst.insert(0,int(s[1]))
    elif s[0] == "push_back":
        lst.append(int(s[1]))
    elif s[0] == "pop_front":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop(0))
    elif s[0] == "pop_back":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop(len(lst)-1))
    elif s[0] == "size":
        print(len(lst))
    elif s[0] == "empty":
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == "front":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
    else:
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[len(lst)-1])

if __name__ == "__main__":

    ea = int(stdin.readline())
    lst = []
    for i in range(ea):
        s = stdin.readline()
        queue(s)