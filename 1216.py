lst_dist = []

while True:
    try:
        name = input()
        dist = float(input())
        lst_dist.append(dist)
    except EOFError:
        print("{:.1f}".format(sum(lst_dist) / len(lst_dist)))
        break
