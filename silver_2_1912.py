if __name__ == "__main__":
    n = int(input())
    lst = list(map(int, input().split()))
    a = [lst[0]]
    for i in range(len(lst) - 1):
        a.append(max(a[i] + lst[i + 1], lst[i + 1]))

    print(max(a))
