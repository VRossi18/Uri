casos = int(input())

for i in range(casos):
    lst_inputs = input().split(' ')
    if (len(lst_inputs[0]) >= 2):
        x = lst_inputs[0][-1]
        y = lst_inputs[1][-1]
        if (x == y):
            print('encaixa')
        else:
            print('nao encaixa')
    else:
        a = lst_inputs[0][-2]
        b = lst_inputs[1][-2]
        if (a == b):
            print('encaixa')
        else:
            print('nao encaixa')
    lst_inputs.clear()