"""
Grupo: Anna Paula Siqueira da Silva, Maria Laura Soares Barbosa, Ariane Arantes dos Santos e Luanda Rodrigues da Silva
Turma: 2BINFO

Faça um programa que leia uma matriz 6x3 com números reais, calcule e mostre: 
(a) o maior elemento da matriz e sua respectiva posição (linha e coluna); 
(b) o menor elemento da matriz e sua respectiva posição.
"""
linhas = 6
colunas = 3
matriz = []
maior = [0] * 3
menor = [0] * 3
for i in range(linhas):
    linha = []
    print(f"Linha {i + 1}")
    for j in range(colunas):
        linha.append(float(input("Digite um número: ")))
    matriz.append(linha)
for i in range(linhas):
    for j in range(colunas):
        if(i == 0 and j == 0):
            menor[0] = matriz[i][j]
            maior[0] = matriz[i][j]
        if(matriz[i][j] < menor[0]):
            menor[0] = matriz[i][j]
            menor[1] = i
            menor[2] = j
        if(matriz[i][j] > maior[0]):
            maior[0] = matriz[i][j]
            maior[1] = i
            maior[2] = j
print(f"O maior número é {maior[0]:.2f} e está na posição {maior[1] + 1} {maior[2] + 1}")
print(f"O menor número é {menor[0]:.2f} e está na posição {menor[1] + 1} {menor[2] + 1}")