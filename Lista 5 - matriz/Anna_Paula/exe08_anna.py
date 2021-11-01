"""
Grupo: Anna Paula Siqueira da Silva, Maria Laura Soares Barbosa, Ariane Arantes dos Santos e Luanda Rodrigues da Silva
Turma: 2BINFO

Faça um programa que lê duas notas para cada aluno de duas turmas. Cada turma tem 3 alunos. 
Armazene os dados em uma matriz M. Cada aluno deve ter três notas (as duas digitadas e a média dessas duas). 
Calcule a média de cada turma e armazene em um vetor TURMA. Informe qual turma tem maior média, e quais alunos 
tiveram média maior que a média de sua turma.
"""
#Não testei
tam = 3
matriz = []
matrizT = []
turma = []
for i in range(2):
    matriz = []
    print(f"Turma {i + 1}")
    for j in range(tam):
        print(f"Notas do aluno {j + 1} da turma {i + 1}")
        linha = []
        for k in range(tam):
            if(k == tam - 1):
                linha.append((linha[0] + linha[1]) / 2) #media
            else:
                linha.append(float(input(f"Digite a nota {k + 1}: ")))
        matriz.append(linha)
    turma.append((matriz[0][2] + matriz[1][2] + matriz[2][2]) / 3)
    matrizT.append(matriz)
    print()
print(f"A turma que tem maior media é a turma {turma.index(max(turma)) + 1}")
print()
print("Alunos que tiveram média maior do que a média da turma")
for i in range(2):
    print(f"Turma {i + 1}")
    for j in range(tam):
        for k in range(tam - 1, tam):
            if(matrizT[i][j][k] > turma[i]):
                print(f"Aluno {j + 1}")
    print()