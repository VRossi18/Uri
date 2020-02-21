import Aleatorios as al
import media as m

lista = al.geraListaInteiro(20)
print(lista)

print("A media da lista é: ", m.get_media(lista), sep=" ")
print("A moda da lista é:", m.get_moda(lista), sep=" ")
print("A mediana da lista é", m.get_mediana(lista), sep=" ")