count = 0
soma = 0 
while True:
    if count < 2:
        nota = float(input())
        if (nota <= 10 and nota >= 0):
            soma = soma + nota
            count = count + 1
        else:
            print('nota invalida')
    else:
        print('media =', soma/2, sep=' ')
        break
