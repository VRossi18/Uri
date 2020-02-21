import math as m

def get_maior_idade(idade):
    if (idade < 18):
        print("Menor de idade")
    else:
        print("Maior de idade")

def get_aprovado(n1, n2):
    if (n1 + n2 >= 6):
        print("Aprovado(a)")
    else:
        print("Reprovado(a)")

def get_resultado_segundo_grau(a,b,c):
    lista = []
    delta = (b*b) - 4*(a*c)

    if (delta < 0):
        print("Função com o resultado no campo dos números imaginários")
        return 0
    
    result_1 = (-1*(b*b) + m.sqrt(delta)) / 2*a
    result_2 = ((b*b) + m.sqrt(delta)) / 2*a
    lista.append(result_1)
    lista.append(result_2)
    return lista

def calculadora(n1,n2,sinal):
    if (sinal == "+"):
        return n1+n2
    elif (sinal == "-"):
        return n1-n2
    elif (sinal == "*"):
        return n1*n2
    elif (sinal == ":" or sinal == "/"):
        return n1/n2
    else:
        print("Sinal inválido")
        return 0

idade = int(input())
get_maior_idade(idade)

a = int(input())
b = int(input())
c = int(input())

func = get_resultado_segundo_grau(a,b,c)
print(func)

nota1 = float(input())
nota2 = float(input())

get_aprovado(nota1,nota2)

lista = [3,2,1]
lista.sort()
print(lista)
print(calculadora(4,2,"*"))