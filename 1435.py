while True:
    ordem = int(input())
    if ordem != 0:
        matrix = [[0 for x in range(ordem)] for y in range(ordem)]
        print(matrix)
    else:
        break