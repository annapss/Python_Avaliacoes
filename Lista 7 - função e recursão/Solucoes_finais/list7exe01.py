"""
Grupo: Maria Laura Barbosa Soares, Anna Paula Siqueira da Silva, Luanda Rodrigues da Silva e Ariane Arantes dos Santos
Turma: 2BINFO

Faça  um  programa,  utilizando  recursão,  que  leia  dois  números  binários,  com  qualquer quantidade de bits,
e em seguida efetue a soma desses dois números binários. Obs.: Não é para converter os números para decimais e 
realizar a operação de soma.  Todas as operações devem ser realizadas com números binários.  
(Não utilize estrutura de repetição, sob pena de anular a questão). 
"""
digitosA = []
digitosB = []
resposta = []
nA = input('Digite o primeiro numero: ')
nB = input("Digite o segundo número: ")
tamA = len(nA)
tamB = len(nB)
nA = int(nA)
nB = int(nB)
def bin(n, vetor):  #função para separar cada dígito do número binario e colocá-los em uma lista
    if n < 1:
        return False
    else:
        vetor.append(n%10)
        bin(n//10, vetor)

def soma(n, i=0, resto=0):  #função para somar digíto por digíto dos dois números binários
    if(i == n):
        return False
    else:
        if(digitosA[i] + digitosB[i] + resto == 0):
            resposta[i] = 0
            resto = 0
        elif(digitosA[i] + digitosB[i] + resto == 1):
            resposta[i] = 1
            resto = 0
        elif(digitosA[i] + digitosB[i] + resto == 2):
            if(i == n - 1):
                resposta[i] = 10
                resto = 0
            else:
                resposta[i] = 0
                resto = 1
        else:
            if(i == n - 1):
                resposta[i] = 11
                resto = 0
            else: 
                resposta[i] = 1
                resto = 1
        return soma(n, i + 1, resto)

def percurso(i):  #função para printar o resultado
    if(i == -1):
        return False
    else:
        print(f"{resposta[i]}", end="")
        return percurso(i - 1)

def repete(n, vetor, i = 0):  #função para igualar o tamanho das listas que guardam separadamente os dígitos de cada número binário
    if i == n:
        return False
    else:
        vetor.append(0)
        repete(n, vetor, i + 1)
bin(nA, digitosA)
bin(nB, digitosB)
if(tamA != tamB):
    if(tamA < tamB):
        repete(tamB - tamA, digitosA)
    else:
        repete(tamA - tamB, digitosB)
resposta = [0] * len(digitosA)
soma(len(digitosA))
percurso(len(resposta) - 1)