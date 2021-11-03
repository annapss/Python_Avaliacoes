"""
Grupo: Anna Paula Siqueira, Ariane Arantes, Luanda Rodrigues e Maria Laura Soares
Turma: 2BINFO

8. Faça um programa que lê duas notas para cada aluno de
duas turmas. Cada turma tem 3 alunos. Armazene os dados
em uma matriz M. Cada aluno deve ter três notas (as duas
digitadas e a média dessas duas). Calcule a média de cada
turma e armazene em um vetor TURMA. Informe qual
turma tem maior média, e quais alunos tiveram média
maior que a média de sua turma.

"""
turmas = 2
alunos = 3
notas = 2
matrizPrin = []
medias = [] 
mediaAlunos = []
mediasTurmas = []
for i in range(turmas):  #criação da matriz e cáculo da média de cada aluno
    aux = []
    print(f'\nTurma {i+1}')
    medias = []
    for j in range(alunos):
        print(f'Aluno {j+1}')
        linha = []
        soma = 0
        for z in range(notas):
            linha.append(float(input(f'Digite sua nota {z+1}: ')))
            soma += linha[z]
        linha.append(soma/notas) #media
        aux.append(linha)
        medias.append(soma/notas)
    mediaAlunos.append(medias)
    matrizPrin.append(aux)

for i in range(turmas):  #cálculo da média de cada turma
    mediasTurmas.append(sum(mediaAlunos[i]) / alunos)

maior = max(mediasTurmas)
grp = mediasTurmas.index(max(mediasTurmas))

print('\nMatriz M:')
for aux in matrizPrin:
    print(aux)

print(f'\nA turma {grp+1} possui a maior média com {maior:.2f}')


for i in range(turmas):
    for j in range(alunos):  #verificação de que alunos tiveram média superior a de sua turma
        if mediaAlunos[i][j] > mediasTurmas[i]:
            print(f'O aluno {i+1} da turma {j + 1} tem a média({mediaAlunos[i][j]:.2f}) como maior que a média de sua turma.')