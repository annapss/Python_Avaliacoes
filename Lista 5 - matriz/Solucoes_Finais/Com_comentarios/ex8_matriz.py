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
medias = [] #criei um vetor medias pra colocar as medias dos alunos de cada turma
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
    mediaAlunos.append(medias) #depois adiciono em outro vetor pra fazer uma matriz
    matrizPrin.append(aux)
#cada linha de mediaAlunos representa as medias dos alunos de uma turma
#com isso, posso usar o sum()
for i in range(turmas):  #cálculo da média de cada turma
    mediasTurmas.append(sum(mediaAlunos[i]) / alunos)
    """soma += mediaAlunos[i]
    j +=1
    if j == 3:
        TURMA.append(soma/alunos)
        soma = 0
        j = 0
    """

maior = max(mediasTurmas)
grp = mediasTurmas.index(max(mediasTurmas))
#Usando o max() e o index(), não precisamos do for
"""for i in range(turmas):  #verificação de qual turma tem a maior média
    if i == 0:
        maior = TURMA[i]
    else:
        if TURMA[i] > maior:
            maior = TURMA[i]
            grp = i
"""
print('\nMatriz M:')
for aux in matrizPrin:
    print(aux)

print(f'\nA turma {grp+1} possui a maior média com {maior:.2f}')

#z = 0
for i in range(turmas):
    for j in range(alunos):  #verificação de que alunos tiveram média superior a de sua turma
    ##if i <= 2: #media dos alunos da primeira turma
        if mediaAlunos[i][j] > mediasTurmas[i]:
            print(f'O aluno {i+1} da turma 1 tem a média({mediaAlunos[i][j]:.2f}) como maior que a média de sua turma.')
    ##elif i > 2: #media dos alunos da segunda turma
        ##z +=1
        ##if mediaAlunos[i] > TURMA[1]:
            ##print(f'O aluno {z} da turma 2 tem a média({mediaAlunos[i]}) como maior que a média de sua turma.')
