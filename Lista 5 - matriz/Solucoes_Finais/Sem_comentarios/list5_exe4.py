
"""
Grupo: Anna Paula Siqueira, Ariane Arantes, Luanda Rodrigues e Maria Laura Soares
Turma: 2BINFO

4. Faça um programa que leia uma matriz 3x3 de inteiros e retorne a
linha de maior soma. Imprima na tela a matriz, a linha de maior
soma e a soma. Obs.: Em Python existe uma função sum() que efetua
a soma dos elementos de uma lista. Faça a questão de duas
maneiras: utilizando e não utilizando a função sum()

Sem o SUM:
"""

matriz = []
vet = []
tam = 3
soma = 0

for i in range(tam):
    linha = []
    for j in range(tam):
        linha.append(int(input(f'Digite um valor para [{i+1}] [{j+1}]: ')))
        soma += linha[j]
    vet.append(soma)  #soma da linha
    matriz.append(linha)
    soma = 0
for i in range(tam):
    print(matriz[i])
print(f'A linha de maior soma é a {vet.index(max(vet)) + 1} onde seus elementos somam {max(vet)} ')

