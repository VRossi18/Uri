while (True):
    n = int(input())
    if (n == 0):
        break
    lst = []

    for i in range(n):
        lst.append((n-i) ** 2)

    print(sum(lst))