"""
Grupo: Anna Paula Siqueira da Silva, Maria Laura Barbosa Soares, Ariane Arantes dos Santos e Luanda Rodrigues da Silva
Turma: 2BINFO

Um subvetor de um vetor v é o que sobra depois de alguns dos elementos de v são apagados. 
(por exemplo, 12  13  10  3   é um subvetor de 11  12  13  11  10  9  7  3  3, mas não é um 
subvetor de 11  12  10  11  13  9  7  3  3). Faça um programa que leia dois vetores de inteiros, 
um vetor ve um vetor x, e em seguida decida se o vetor x é um subvetor de v.  
Peça para o usuário entrar com os tamanhos do vetor v e do vetor x.  
Obs.:  O tamanho do vetor x não pode ser maior que o vetor v.
"""
tamV = int(input("Digite o tamanho do vetor v: "))
tamX = int(input("Digite o tamanho do vetor x: "))
if(tamX > tamV):
    print("O tamanho do vetor x não pode ser maior que o tamanho do vetor V")
else:
    vetorV = [0] * tamV
    vetorX = [0] * tamX
    print('Vetor V')
    for i in range(tamV):
        vetorV[i] = int(input("Digite um número: "))
    print("Vetor X")
    for i in range(tamX):
        vetorX[i] = int(input('Digite um número: '))
    nSubvetor = 0
    cont = 0
    j = 0
    while(vetorV.count(vetorX[0]) != 0 and nSubvetor == 0):
        if(tamX <= tamV - 1 - vetorV.index(vetorX[0])):
            i = vetorV.index(vetorX[0])
            j = 0
            while(j < tamX):
                if(vetorV[i] == vetorX[j]):
                    cont += 1
                j += 1
                i += 1
        if(cont == tamX):
            nSubvetor = 1
        else:
            del(vetorV[vetorV.index(vetorX[0])])
        count = 0
    if(nSubvetor == 0):
        print(f'{vetorX} não é subvetor de {vetorV}')
    else:
        print(f'{vetorX} é subvetor de {vetorV}')