while True:
    try:
        binario = input()
        while ('#' not in binario):
            cont = input()
            binario = binario + cont
        
        num = int(binario.replace('#',''),2)
        if (num % 131071 == 0):
            print('YES')
        else:
            print('NO')

    except EOFError:
        break