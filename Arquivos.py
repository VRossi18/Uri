#r - somente leitura
#w - escrita
#a - leitura e escrita (adiciona conteudo ao final do arquivo)
#r+ - leitura e escrita
#w+ - escrita (apaga conteudo anterior do arquivo)
#a+ - leitura e escrita (abre o arquivo para atualizacao)

arq = open("teste.txt", "a")
# linhas = arq.readlines()
# for linha in linhas:
#     print(linha)

arq.write("\nsadasdasd")
arq.close()