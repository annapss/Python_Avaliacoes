
"""
Grupo: Anna Paula Siqueira da Silva, Maria Laura Barbosa Soares, Ariane Arantes dos Santos e Luanda Rodrigues da Silva
Turma: 2BINFO

1 Questão:
Faça um programa que preencha um vetor com vários valores inteiros lidos do teclado. A
condição de parada será o usuário digitar FIM. Em seguida, informe o número de ocorrências de
cada elemento do vetor.

Ex.:
Vet = [1, -100, 1, 30, 12, 1, 12, 12, 12, 90]
Seu programa deverá retornar:
O número -100 apareceu 1 vez no vetor
O número 1 apareceu 3 vezes no vetor
O número 12 apareceu 4 vezes no vetor
O número 30 apareceu 1 vez no vetor
O número 90 apareceu 1 vez no vetor

Obs.: Cada ocorrência do número no vetor, só deve aparecer uma vez na resposta, ou seja, não
é para o seu programa informar 3 vezes que o número 1 apareceu no vetor, e nem para informar
que o número 12 apareceu 4 vezes no vetor.

"""

vet = []
fim = 0

while not fim:
    valor = input('Digite um valor inteiro: ')
    vet.append(valor)
    if valor == 'FIM':
        fim = True

for i in range(len(vet)-1):      # passar todos os itens do vetor vet de string para inteiro
    vet[i] = int(vet[i])

occ = [0]*(len(vet)-1)           # vetor para guardar as ocorrências dos números no vetor vet sem contar com o 'FIM'

for i in range(len(occ)):
    cont = 0
    aux = 0
    if i != 0:
        for j in range(i):
            if vet[j] == vet[i]:
                aux += 1

    if aux == 0:
        for z in range(len(vet)-1):
            if vet[i] == vet[z]:
                cont += 1
        occ[i] = cont #A parte que vc tinha colocado, ta comentada lá embaixo. Ela tem que ficar aqui
    if aux != 0:
        occ[i] = -1


    #occ[i] = cont
    if occ[i] != -1:
        if occ[i] > 1:
            print(f'\nO valor {vet[i]} aparece {occ[i]} vezes no vetor')
        elif occ[i] == 1:
            print(f'\nO valor {vet[i]} aparece {occ[i]} vez no vetor')


