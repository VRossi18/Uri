numerica = [1,2,3,4,5,6,7]
soma = 0
lista = [123,5,45,364,53757,657]

numerica.append(8)

for item in numerica:
    soma = soma + item

print(soma)

del numerica[2:]
print(numerica)

lista.sort()
print(lista)