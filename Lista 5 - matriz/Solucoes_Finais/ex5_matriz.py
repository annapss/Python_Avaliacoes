
"""
Grupo: Anna Paula Siqueira, Ariane Arantes, Luando Rodrigues e Maria Laura Soares
Turma: 2BINFO

5-Faça um programa que leia a ordem de uma matriz quadrada A (até
100), posteriormente leia seus valores e escreva sua transposta AT,
onde AT[i][j] = A[j][i]
"""

ordem = int(input('Para uma matriz quadrada A, informe sua ordem:  '))

if ordem < 1 or ordem > 100:
    cont = 1
    while cont == 1:
        print('Valor inválido')
        ordem = int(input('Para uma matriz quadrada A, informe sua ordem:  '))
        cont = 0
        if ordem < 1 or ordem > 100:
            cont = 1

A = []
for i in range(ordem):
    linha = []
    for j in range(ordem):
        linha.append(int(input('Digite um valor: ')))
    A.append(linha)

print('\nMatriz original: A')
for i in range(ordem):
    print(A[i])

#formação da matriz transposta:
matriz = []
for i in range(ordem):
    linha = []
    for j in range(ordem):
        linha.append(0)
    matriz.append(linha)

for i in range(ordem):
    for j in range(ordem):
        if i == j:
            matriz[i][j] = A[i][j]
        elif i != j:
            matriz[j][i] = A[i][j]

print('\nMatriz transposta: At')
for i in range(ordem):
    print(matriz[i])




