dados = input()
notas = dados.split(' ')
notas = [float(i) for i in notas]

media = ((notas[0] * 2) + (notas[1] * 3) + (notas[2] * 4) + notas[3]) / 10

if (media >= 7.0):
    print("Media:", media, sep=" ")
    print("Aluno aprovado.")

elif (media < 5.0):
    print("Media:", media, sep=" ")
    print("Aluno reprovado.")

elif (media >= 5.0 and media <= 6.9):
    nota_exame = float(input())
    print("Media:", media, sep=" ")
    print("Aluno em exame.")
    print("Nota do exame:", nota_exame, sep=" ")
    media_exame = (nota_exame + media) / 2
    
    if (media_exame >= 5.0):
        print("Aluno reprovado.")
    else:
        print("Aluno reprovado.")

    print("Media final:", media_exame, sep=" ")