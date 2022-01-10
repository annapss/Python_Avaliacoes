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
#Primeira opção feita
def primeiraOpcao(nomeArquivoA, nomeArquivoB, modeloEscolhido):
    arquivoMod = open(nomeArquivoA)
    arquivoCompleto = open(nomeArquivoB)
    modelo = ""
    codigoA = ""
    linha = arquivoMod.readline()
    while(linha != "" or modelo == modeloEscolhido):
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
                if(virgulas == 0):
                    codigoB += linha[i]
                if(virgulas == 3):
                    qtd += linha[i]
            if(codigoB == codigoA):
                total += int(qtd)
        print(f"Temos {qtd} de carros do modelo {modeloEscolhido}")