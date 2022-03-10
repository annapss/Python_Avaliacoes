"""
Grupo: Anna Paula Siqueira da Silva, Ariane Arantes dos Santos, Maria Laura Barbosa Soares e Luanda Rodrigues da Silva
Turma: 2BINFO

Faça um programa que preencha um vetor com vários valores inteiros lidos do teclado. 
A condição de parada será o usuário digitar FIM. 
Em seguida, informe o número de ocorrências de cada elemento do vetor. 
"""
acabou = 0
vetor = []
while (acabou == 0):
    a = input("Digite um numero: ")
    if(a == 'FIM'):
        acabou = 1
    else:
        vetor.append(int(a))
jaFoi = []
plural = ''
for i in range(len(vetor)):
    if(vetor[i] not in jaFoi):
        jaFoi.append(vetor[i])
        if(vetor.count(vetor[i]) != 1):
            plural = 'vezes'
        else:
            plural = 'vez'
        print(f'O número {vetor[i]} apareceu {vetor.count(vetor[i])} {plural} no vetor')