
"""
Grupo: Anna Paula Siqueira, Ariane Arantes, Luando Rodrigues e Maria Laura Soares
Turma: 2BINFO

5-Faça um programa que leia a ordem de uma matriz quadrada A (até
100), posteriormente leia seus valores e escreva sua transposta AT,
onde AT[i][j] = A[j][i]
"""

ordem = int(input('Para uma matriz quadrada A, informe sua ordem:  '))

#Ao invés de usar o if e o while, pode usar só o while
"""if ordem < 1 or ordem > 100:
    cont = 1
    while cont == 1:
        print('Valor inválido')
        ordem = int(input('Para uma matriz quadrada A, informe sua ordem:  '))
        cont = 0
        if ordem < 1 or ordem > 100:
            cont = 1
"""
while(ordem < 1 or ordem > 100):
    print("Valor invalido")
    ordem = int(input('Para uma matriz quadrada A, informe sua ordem:  '))

#não é bom usar nome de variavel com letra maiúscula pois geralmente usamos letra maiúscula quando é um const
matrizA = []
for i in range(ordem):
    linha = []
    for j in range(ordem):
        linha.append(int(input('Digite um valor: ')))
    matrizA.append(linha)

print('\nMatriz original: A')
for i in range(ordem):
    print(matrizA[i])

#formação da matriz transposta:
matrizT = []
for i in range(ordem):
    linha = []
    for j in range(ordem):
        linha.append(0)
    matrizT.append(linha)

for i in range(ordem):
    for j in range(ordem):
        #Esse if e elif funciona mas é mais fácil só fazer matriz[i][j] = matrizA[j][i] como ele colocou
        #no enunciado
        matrizT[i][j] = matrizA[j][i]
        """if i == j:
            matrizT[i][j] = matrizA[i][j]
        elif i != j:
            matrizT[j][i] = matrizA[i][j]"""

print('\nMatriz transposta: At')
for i in range(ordem):
    print(matrizT[i])