""""
Grupo: Anna Paula Siqueira da Silva, Maria Laura Barbosa Soares, Luanda Rodrigues da Silva e Ariane Arantes dos Santos
Turma: 2BINFO

Com os dois arquivos criados na questão anterior, faça um programa que simule um sistema para consulta e 
vendas de carros. O sistema deve ter o seguinte menu de opções: 
- Consulta da quantidade disponível de um determinado modelo de carro. Ex.: Se o usuário escolher essa opção, o 
programa deverá pedir o modelo do carro; então o usuário digitará o modelo e em seguida o programa informará o 
total de veículos disponíveis para a venda daquele modelo. Caso o modelo não exista, deverá aparecer a mensagem: 
“modelo inexistente”. Lembre-se que podem existir várias cores para o mesmo modelo. 

- Consulta de modelos disponíveis de uma determinada cor e entre uma determinada faixa de preços. Ex.: Se o usuário 
escolher essa opção, o programa deverá pedir a cor do carro e a faixa de preço, isto é, o valor mínimo e o valor 
máximo de preço que o usuário irá informar. Em seguida o programa irá retornar os nomes dos modelos da cor e faixa 
de preços especificados pelo usuário. 

- Fim de programa 
"""
def arquivoNaMatriz(nomeArquivo, matriz): #Colocando arq1.txt em uma matriz para facilitar a vida
    arquivo = open(nomeArquivo)
    linha = arquivo.readline()
    codigos = [] #Linha de códigos
    modelos = [] #Linha de modelos
    while(linha != ""):
        if(linha != "Codigo,Modelo\n"):
            numero = "" #codigo
            nome = "" #modelo
            for i in range(len(linha)):
                if(i < linha.index(",")):
                    numero += linha[i]
                else:
                    if(linha[i] != '\n' and linha[i] != ","):
                        nome += linha[i]
            codigos.append(numero)
            modelos.append(nome)
        linha = arquivo.readline()
    matriz.append(codigos) #linha 0
    matriz.append(modelos) #linha 1
    arquivo.close()

#Primeira Opção
def primeiraOpcao(nomeArquivoA, nomeArquivoB, modeloEscolhido):
    arquivoMod = open(nomeArquivoA) #Abrindo arquivo 1
    arquivoCompleto = open(nomeArquivoB) #Abrind arquivo 2
    linha = arquivoMod.readline()
    while(linha != "" and modelo.lower() != modeloEscolhido.lower()): #Pegando as informacoes do arquivo 'arq1.txt'
        modelo = ""
        codigoA = ""
        if(linha != "Codigo,Modelo\n"):
            for i in range(len(linha)):
                #Virgulas mostram quais informacoes estão sendo lidas
                if(i < linha.index(",")):
                    codigoA += linha[i]
                elif(i > linha.index(",")):
                    if(linha[i] != '\n'):
                        modelo += linha[i]
        linha = arquivoMod.readline()
    if(modelo != modeloEscolhido):
        print("Modelo inexistente!")
    else:
        linha = arquivoCompleto.readline() #Arquivo 2
        total = 0
        while(linha != ""): #Pegando informacoes de 'arq2.txt'
            if(linha != "Codigo,Cor,Preco,Quantidade\n"):
                virgulas = 0
                codigoB = ""
                qtd = ""
                for i in range(len(linha)):
                    if(linha[i] == ","):
                        virgulas += 1
                    if(linha [i] != '\n' and linha[i] != ","):
                        if(virgulas == 0):
                            codigoB += linha[i]
                        if(virgulas == 3):
                            qtd += linha[i]
                if(codigoB == codigoA): #Encontrando o modelo e adicionando sua quantidade
                    total += int(qtd)
            linha = arquivoCompleto.readline()
        print(f"Temos {total} de carros do modelo {modeloEscolhido}")
    arquivoCompleto.close()
    arquivoMod.close()

#Segunda Opção
def segundaOpcao(nomeArquivo, matriz, valorMin, valorMax):
    arquivo = open(nomeArquivo)
    arquivoNaMatriz('arq1.txt', matriz) #Funcao que coloca as informacoes de 'arq1.txt' em uma matriz
    linha = arquivo.readline()
    tenho = 0
    while(linha != ""): #Pegando informacoes do 'arq2.txt'
        if(linha != "Codigo,Cor,Preco,Quantidade\n"):
            virgulas = 0
            codigo = ""
            cor = ""
            preco = ""
            for i in range(len(linha)):
                if(linha[i] == ','): #Virgulas indicam qual informacao está sendo lida
                    virgulas += 1
                if(linha[i] != '\n' and linha[i] != ","):
                    if(virgulas == 0):
                        codigo += linha[i]
                    if(virgulas == 1):
                        cor += linha[i]
                    if(virgulas == 2):
                        preco += linha[i]
            if(float(preco) >= valorMin and float(preco) <= valorMax): 
                #Confere se o preco do carro está dentro da faixa de preco escolhida
                tenho += 1
                print(f"O carro {matriz[1][matriz[0].index(codigo)]} na cor {cor} tem valor {preco}")
        linha = arquivo.readline()
    if(tenho == 0):
        print("Não temos carros nessa faixa de preço")
    arquivo.close()

print("Seja bem-vindo ao programa de consultas!\n")
print("Escolha uma opção:")
print("Digite 1 - Consulta da quantidade disponível de um determinado modelo de carro")
print("Digite 2 - Consulta de modelos disponíveis de uma determinada cor e entre uma determinada faixa de preços")
print("Digite FIM - Finalizar programa\n")

#Programa Principal
consulta = ""
matrizArqA = []
while(consulta != 'FIM'):
    consulta = input("Digite a opção desejada: ")
    if(consulta == '1'): #Primeira opcao de consulta
        modelo = input("Digite o modelo desejado: ")
        primeiraOpcao("arq1.txt", 'arq2.txt', modelo)
        print()
    elif(consulta == '2'): #Segunda opcao de consulta
        valorMin = float(input("Digite o valor mínimo: "))
        valorMax = float(input("Digite o valor máximo: "))
        segundaOpcao("arq2.txt", matrizArqA, valorMin, valorMax)
        print()