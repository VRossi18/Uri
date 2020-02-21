while True:
    x = int(input())
    lista = []
    if (x != 0):
        for i in range(1,x+1):
            lista.append(i)
        print(*lista, sep=' ')
    else:
        break