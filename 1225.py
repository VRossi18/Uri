while True:
    num_min, num_max = map(int,input().split(" "))

    for i in range(num_min,num_max):
        for x in list(i):
            if list.count(x) > 1:
                print()
