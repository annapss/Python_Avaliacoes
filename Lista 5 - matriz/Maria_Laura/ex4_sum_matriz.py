
"""
Grupo: Anna Paula Siqueira, Ariane Arantes, Luando Rodrigues e Maria Laura Soares
Turma: 2BINFO

4. Faça um programa que leia uma matriz 3x3 de inteiros e retorne a
linha de maior soma. Imprima na tela a matriz, a linha de maior
soma e a soma. Obs.: Em Python existe uma função sum() que efetua
a soma dos elementos de uma lista. Faça a questão de duas
maneiras: utilizando e não utilizando a função sum()

Com o SUM:
"""

matriz = []
tam = 3
maior = 0
mlinha = 0

for i in range(tam):
    linha = []
    for j in range(tam):
        linha.append(int(input(f'Digite um valor para [{i+1}] [{j+1}]: ')))

    matriz.append(linha)

for i in range(tam): #soma da linha
    if i == 0:
        maior = sum(matriz[0])
    else:
        if sum(matriz[i]) > maior:
            maior = sum(matriz[i])
            mlinha = i

for i in range(tam):
    print(matriz[i])

print(f'A linha de maior soma é a {mlinha+1} onde seus elementos somam {maior} ')
