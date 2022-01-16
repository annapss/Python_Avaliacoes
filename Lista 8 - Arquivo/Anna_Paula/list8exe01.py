"""
Grupo: Anna Paula Siqueira da Silva, Maria Laura Barbosa Soares, Luanda Rodrigues da Silva e Ariane Arantes dos Santos
Turma: 2BINFO

A faculdade de informática de uma universidade possui 2 arquivos referentes aos dados dos candidatos que fizeram 
vestibular. O primeiro possui o número de inscrição, o nome do candidato e a renda familiar; o segundo possui a 
classificação do candidato, sua matrícula e suas notas nas provas objetivas e discursivas. O primeiro arquivo está 
ordenado por número de inscrição e o segundo arquivo está ordenado por classificação. Foi instituído o sistema de 
cotas e essa universidade agora precisa destinar 25% de suas vagas aos melhores classificados com renda inferior ou 
igual a R$1000,00. Faça um programa que gere dois arquivos de saída, o primeiro contendo os nome, classificação 
inicial e classificação final, dos candidatos com renda inferior ou igual a R$1000,00, em ordem de inscrição e o 
segundo arquivo contendo os nome, inscrição e classificação inicial dos candidatos que estavam classificados e que
perderam a vaga após a instituição do sistema de cotas. 
"""
import random
def nomeAleatorio(nLetras): #Nomes dos candidatos
    vogais = ['a', 'e', 'i', 'o', 'u']
    consoantes = ['b', 'c', 'd' , 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']
    nome = ''
    for i in range(nLetras): #v + c + v + c - xoxo
        if(i % 2 == 0):
            nome += vogais[random.randint(0, len(vogais) - 1)]
        else:
            nome += consoantes[random.randint(0, len(consoantes) - 1)]
    return nome
def escreveArq1(nomeArquivo, nCandidatos): #Arquivo 1 pronto! :)
    arquivo = open(nomeArquivo, 'w')
    arquivo.write("Inscricao,Nome,Renda\n")
    for i in range(1, nCandidatos + 1):
        arquivo.write("0"*(5 - len(str(i))) + str(i) + ',' + nomeAleatorio(random.randint(4, 10)) + ',R$' + str(random.randint(50000, 500000) / 100) + '\n')
    arquivo.close()

def defineNotas(notas, nCandidatos): #Definindo as notas dos canditados e colocando em um vetor
    objetivas = [-1] #Valor na posicao 0 em cada vetor
    discursivas = [-1]
    medias = [-1]
    for i in range(1,nCandidatos + 1):
        objetivas.append(random.randint(0, 1000) /100)
        discursivas.append(random.randint(0, 1000) /100)
        medias.append((objetivas[i] + discursivas[i]) / 2) #Talvez tenha arrendondar para 2 casas decimais
    notas.append(objetivas)
    notas.append(discursivas)
    notas.append(medias)
    return notas
 
 #Função de empate ainda não está pronta :(

def empate(maior, matriz): #Retorna o número de inscrição de quem irá ficar na maior posição
    inscricao = matriz[2].index(maior)
    maiorDiscursiva = matriz[1][inscricao]
    copiaMedias = [-1]
    for i in range(len(matriz[2])):
        copiaMedias.append(matriz[2][i])
    while(copiaMedias.count(maior) != 0):
        i = matriz[2].index(maior)
        if(matriz[1][i] > maiorDiscursiva):
            maiorDiscursiva = matriz[1][i]
            inscricao = i
        copiaMedias[i] = -1
    return inscricao

def defineClassificacao(matriz, nCandidatos, nomeArquivo): #Faz a classificação e já escreve no arquivo 2
    arquivo = open(nomeArquivo, 'w')
    arquivo.write("Classificacao,Inscricao,Objetiva,Discursiva\n")
    i = 0
    while(matriz[2].count(-1) != nCandidatos):
        i += 1
        maiorMedia = max(matriz[2])
        if(matriz[2].count(maiorMedia) != 1):
            inscricao = empate(maiorMedia, matriz)
        else:
            inscricao = matriz[2].index(maiorMedia)
        inscricao = str(inscricao)
        arquivo.write("0"*(4 - len(str(i))) + str(i) + ',' + "0"*(4 - len(inscricao)) + "," + 
        str(matriz[0][int(inscricao)]) + "," + str(matriz[0][int(inscricao)]) + '\n')
        matriz[2][int(inscricao)] = -1
    arquivo.close()    


notas = []
nVagas = random.randint(20, 100)
nCandidatos = random.randint(nVagas, 500)

escreveArq1('arqCandidatos.txt', nCandidatos)
notas = defineNotas(notas, nCandidatos)
defineClassificacao(notas, nCandidatos, 'classificacao.txt')
"""
Ideia: usando a função max() podemos achar a maior média na coluna que tem a média na matriz que tem as notas. Depois
de usar o max(), vemos quantas vezes esse valor aparece na coluna das médias usando o count(). Se ele mostrar que tem
mais de um, chamamos uma função que ainda será criada que seria chamada de empate(). Nela, saberíamos quem tem a maior
nota na prova discursiva.
Na função empate, podemos ir usando o index nesse valor para encontrar a posição desses valores e também achar a maior
nota discursiva
Depois iríamos escrever no arquivo 2.
"""