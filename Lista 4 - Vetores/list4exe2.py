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
    copiaVetorX = [0] * tamX
    compV = []
    print('Vetor V')
    for i in range(tamV):
        vetorV[i] = int(input("Digite um número: "))
    print("Vetor X")
    for i in range(tamX):
        vetorX[i] = int(input('Digite um número: '))
        copiaVetorX[i] = vetorX[i]
    for i in range(tamV):
        if(vetorV[i] in vetorX):
            compV.append(vetorV[i])
            del(vetorX[vetorX.index(vetorV[i])])
    if(compV == copiaVetorX):
        print(f'{copiaVetorX} é subvetor de {vetorV}')
    else:
        print(f'{copiaVetorX} não é subvetor de {vetorV}')