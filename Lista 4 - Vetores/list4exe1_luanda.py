'''
Grupo: Anna Paula SIqueira da Silva, Ariane Arantes dos Santos, Luanda Rodrigues da Silva e Maria Laura Barbosa Soares.
Turma: 2BINFO
Faça um programa que preencha um vetor com vários valores inteiros lidos do teclado. A condição de parada será o usuário digitar FIM. 
Em seguida, informe o número de ocorrências de cada elemento do vetor. Ex.: Vet = [1, -100, 1, 30, 12, 1, 12, 12, 12, 90] 
Seu programa deverá retornar: 
O número -100 apareceu 1 vez no vetor 
O número 1 apareceu 3 vezes no vetor 
O número 12 apareceu 4 vezes no vetor
O número 30 apareceu 1 vez no vetor 
O número 90 apareceu 1 vez no vetor 
Obs.: Cada ocorrência do número no vetor, só deve aparecer uma vez na resposta, ou seja, não é para o seu programa informar 3 vezes que 
o número 1 apareceu no vetor, e nem para informar que o número 12 apareceu 4 vezes no vetor. 
'''
vetor = []
fim = 0
while(fim == 0):
    l1 = input("Digite um número: ")
    if(l1 == 'FIM'):
      fim = 1
    else:
      vetor.append(l1)


repetiçoes = vetor[i].count(vetor[i])

x = l1

for x in l1:
  if (l1.count(x) > 1): #se o elemento aparecer mais de uma vez
    print(repetiçoes)
    
