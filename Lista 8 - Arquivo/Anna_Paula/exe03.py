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

def arquivoNaMatriz(nomeArquivo, matriz): #Colocando arq1.txt em uma matriz pra facilitar a vida
    arquivo = open(nomeArquivo)
    linha = arquivo.readline()
    numero = ""
    nome = ""
    codigos = []
    modelos = []
    while(linha != ""):
        if(linha != "Codigo,Cor,Preco,Quantidade\n"):
            for i in range(len(linha)):
                if(i < linha.index(",")):
                    numero += linha[i]
                else:
                    nome += linha[i]
        codigos.append(numero)
        modelos.append(nome)
    matriz.append(codigos)
    matriz.append(modelos)

#Primeira Opção feita
def primeiraOpcao(nomeArquivoA, nomeArquivoB, modeloEscolhido):
    arquivoMod = open(nomeArquivoA)
    arquivoCompleto = open(nomeArquivoB)
    modelo = ""
    codigoA = ""
    codigos = []
    modelos = []
    linha = arquivoMod.readline()
    while(linha != "" or modelo == modeloEscolhido):
        if(linha != "Codigo,Modelo\n"):
            for i in range(len(linha)):
                if(i < linha.index(",")):
                    codigoA += linha[i]
                else:
                    modelo += linha[i]
    if(modelo != modeloEscolhido):
        print("O modelo não existe!")
    else:
        linha = arquivoCompleto.readline()
        codigoB = ""
        total = 0
        qtd = ""
        while(linha != ""):
            virgulas = 0
            for i in range(len(linha)):
                if(linha[i] == ","):
                    virgulas += 1
                if(virgulas == 0):
                    codigoB += linha[i]
                if(virgulas == 3):
                    qtd += linha[i]
            if(codigoB == codigoA):
                total += int(qtd)
        print(f"Temos {qtd} de carros do modelo {modeloEscolhido}")

def segundaOpcao(nomeArquivo, matriz, valorMin, valorMax):
    arquivo = open(nomeArquivo)
    arquivoNaMatriz(nomeArquivo, matriz)
    linha = arquivo.readline()
    codigo = ""
    cor = ""
    preco = ""
    tenho = 0
    while(linha != ""):
        virgulas = 0
        for i in range(len(linha)):
            if(linha[i] == ','):
                virgulas += 1
            if(virgulas == 0):
                codigo += linha[i]
            if(virgulas == 1):
                cor += linha[i]
            if(virgulas == 2):
                preco += linha[i]
        if(float(preco) >= valorMin and float(preco) <= valorMax):
            tenho += 1
            print(f"O carro {matriz[1][matriz[0].index(codigo)]} na cor {cor} tem {preco} valor")
    if(tenho == 0):
        print("Não temos carros nessa faixa de preço")