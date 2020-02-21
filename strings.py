a = "Rossi"
b = "Vinicius"
minha_string = "o rato roeu a roupa do rei de roma"

print(a , b , sep=" ")

for i in minha_string.split():
    print(i, sep="\n")

busca = minha_string.find("rei")
print(busca)
print(minha_string[busca:])
minha_string = minha_string.replace("rei","rainha")
print(minha_string)