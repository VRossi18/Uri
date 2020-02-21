casos = int(input())

for i in range(casos):
    lst_alturas = []
    lst_pos = []
    atingido = 0
    num_tiros = int(input())
    
    lst_alturas = list(map(int, input().split(' ')))
    pos = input()
    [lst_pos.append(char) for char in pos]
    for i in range(num_tiros):
        if (lst_alturas[i] <= 2 and lst_pos[i] == 'S'):
            atingido = atingido + 1
        elif (lst_alturas[i] > 2 and lst_pos[i] == 'J'):
            atingido = atingido + 1
    print(atingido)
