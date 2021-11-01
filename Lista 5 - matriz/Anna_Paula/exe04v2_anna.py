"""
Grupo: Anna Paula Siqueira da Silva, Maria Laura Soares Barbosa, Ariane Arantes dos Santos e Luanda Rodrigues da Silva
Turma: 2BINFO

Faça um programa que leia uma matriz 3x3 de inteiros e retorne a linha de maior soma. 
Imprima na tela a matriz, a linha de maior soma e a soma. 
Com a função sum()
"""
tam = 3
matriz = []
maior = 0
l = 0
for i in range(tam):
    linha = []
    print(f"Linha {i + 1}")
    for j in range(tam):
        linha.append(int(input("Digite um número: ")))
    matriz.append(linha)
for i in range(tam):
    if(sum(matriz[i]) >= maior):
        maior = sum(matriz[i])
        l = i + 1
for i in range(tam):
    print(matriz[i])
print(f"A linha de maior soma é a linha {l + 1} e a soma é {maior}")