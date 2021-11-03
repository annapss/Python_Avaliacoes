
"""
Grupo: Anna Paula Siqueira, Ariane Arantes, Luando Rodrigues e Maria Laura Soares
Turma: 2BINFO

5-Faça um programa que leia a ordem de uma matriz quadrada A (até
100), posteriormente leia seus valores e escreva sua transposta AT,
onde AT[i][j] = A[j][i]
"""

ordem = int(input('Para uma matriz quadrada A, informe sua ordem:  '))

while(ordem < 1 or ordem > 100):
    print("Valor invalido")
    ordem = int(input('Para uma matriz quadrada A, informe sua ordem:  '))

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
        matrizT[i][j] = matrizA[j][i]

print('\nMatriz transposta: At')
for i in range(ordem):
    print(matrizT[i])