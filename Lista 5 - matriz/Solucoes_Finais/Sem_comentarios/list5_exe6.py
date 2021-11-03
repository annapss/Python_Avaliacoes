"""
Grupo: Anna Paula Siqueira, Maria Laura Soares, Ariane Arantes e Luanda Rodrigues
Turma: 2BINFO

Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Faça um programa que leia os nomes e os 
tempos (em segundos) de cada volta de cada corredor e guarde as informações em uma matriz. 
Ao final, o programa deve informar:
a. De quem foi a melhor volta da prova, e em que volta
b. Classificação final em ordem (1º o campeão)
c. Qual foi a volta com a média mais rápida
"""
nCompetidores = 6
nCorridas = 11
matrizPrin = []
melhor = [0] * 3 #nome, volta e o tempo
volta = 0
mediasComp = []
for i in range(nCompetidores): #linhas
    linha = []
    for j in range(nCorridas): #colunas
        if(j == 0):
            linha.append(input("Digite o nome: ")) #nome do competidor
        else:
            linha.append(float(input(f"Digite o tempo da volta {j}: ")))
            if(j == 1 and i == 0):
                melhor[2] = linha[1]
    matrizPrin.append(linha)
    print()
for i in range(nCompetidores):
    for j in range(1, nCorridas): #coluna = volta
        if(matrizPrin[i][j] < melhor[2]):
            melhor[2] = matrizPrin[i][j]
            melhor[0] = matrizPrin[i][0] #nome do competidor
            melhor[1] = j #numero da volta
print(f"A melhor volta foi de {melhor[0]} na {melhor[1]}° volta com o tempo {melhor[2]:.2f}")
for i in range(1, nCorridas): #coluna
    soma = 0
    for j in range(nCompetidores): #linha
        soma += matrizPrin[j][i]
    if(i == 1): #media da primeira volta
        maiorMediaV = soma / 6 
    if(soma / 6 < maiorMediaV):
        maiorMediaV = soma / 6
        volta = i
print()
print(f"A volta com média mais rápida é a {volta}")
#Usamos com critério para a classificação a média das voltas de cada corredor
for i in range(nCompetidores): 
    soma = 0
    linha = []
    for j in range(1, nCorridas):
        soma += matrizPrin[i][j]
    linha.append(soma / 10)
    linha.append(matrizPrin[i][0])
    mediasComp.append(linha)
mediasComp.sort()
print()
print("Classificação final:")
for i in range(nCompetidores):
    print(f"{i + 1}° {mediasComp[i][1]}")