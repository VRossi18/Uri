while(True):   
    n = int(input())
    if (n == 0):
        break
    lst_impares = []
    lst_quadrados = []
    quadrados = 0

    for i in range(n*2):
        if (i % 2 != 0):
            lst_impares.append(i)

    for i in lst_impares:
        quadrados = quadrados + i
        lst_quadrados.append(quadrados)

    print(sum(lst_quadrados))