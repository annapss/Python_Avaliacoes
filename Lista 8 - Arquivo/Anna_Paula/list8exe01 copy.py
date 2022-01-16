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
def escreveArq1(nomeArquivo, nCandidatos, notasCotistas, notasNcotistas, notas): #Arquivo 1 pronto! :)
    arquivo = open(nomeArquivo, 'w')
    arquivo.write("Inscricao,Nome,Renda\n")
    inscricaoC = []
    notasC = []
    notasA = []
    inscricaoA = []
    for i in range(1, nCandidatos + 1):
        renda = random.randint(50000, 500000) / 100
        if(renda <= 1000):
            inscricaoC.append(i)
            notasC.append(notas[2][i])
        elif(renda > 1000):
            inscricaoA.append(i)
            notasA.append(notas[2][i])
        notasCotistas.append(inscricaoC) #0
        notasCotistas.append(notasC) #1
        notasNcotistas.append(inscricaoA) #0
        notasNcotistas.append(notasA) #1
        arquivo.write("0"*(5 - len(str(i))) + str(i) + ',' + nomeAleatorio(random.randint(4, 10)) + ',R$' + str(random.randint(50000, 500000) / 100) + '\n')
    arquivo.close()

def defineNotas(notas, nCandidatos): #Definindo as notas dos canditados e colocando em um vetor
    objetivas = [-1] #Valor na posicao 0 em cada vetor
    discursivas = [-1]
    medias = [-1]
    inscricao = [-1]
    for i in range(1,nCandidatos + 1):
        objetivas.append(random.randint(0, 1000) /100)
        discursivas.append(random.randint(0, 1000) /100)
        inscricao.append(i)
        notaFinal = (objetivas[i] + discursivas[i]) / 2
        medias.append(round(notaFinal,2)) #Talvez tenha arrendondar para 2 casas decimais
    notas.append(inscricao) #0 
    notas.append(objetivas) #1
    notas.append(discursivas) #2
    notas.append(medias) #3
    return notas
 
 #Função de empate ainda não está pronta :(

def empate(maior, matriz, mediaP, discursivaP): #Retorna o número de inscrição de quem irá ficar na maior posição
    posicao = matriz[mediaP].index(maior)
    maiorDiscursiva = matriz[discursivaP][posicao]
    copiaMedias = []
    for i in range(len(matriz[mediaP])): 
        copiaMedias.append(matriz[mediaP][i]) 
    while(copiaMedias.count(maior) != 0):
        i = copiaMedias.index(maior)
        if(matriz[discursivaP][i] > maiorDiscursiva):
            maiorDiscursiva = matriz[discursivaP][i]
            posicao = matriz[discursivaP].index(maiorDiscursiva)
        copiaMedias[i] = -1
    copiaMedias.clear()
    return posicao

def defineClassificacao(matriz, nCandidatos, nomeArquivo, posicaoM, posicaoI, posicaoD = 2, posicaoO = 1): #Faz a classificação e já escreve no arquivo 2
    arquivo = open(nomeArquivo, 'w')
    arquivo.write("Classificacao,Inscricao,Objetiva,Discursiva\n")
    i = 0
    while(matriz[posicaoM].count(-1) != nCandidatos + 1):
        i += 1
        maiorMedia = max(matriz[posicaoM])
        posicaoCandidato = matriz[posicaoM].index(maiorMedia)
        if(matriz[posicaoM].count(maiorMedia) != 1):
            posicaoCandidato = empate(maiorMedia, matriz, posicaoM, posicaoD)
        else:
            posicaoCandidato = matriz[posicaoM].index(maiorMedia)
        inscricao = str(matriz[posicaoI][posicaoCandidato])
        discursiva = str(matriz[posicaoD][posicaoCandidato])
        objetiva = str(matriz[posicaoO][posicaoCandidato])
        arquivo.write("0"*(4 - len(str(i))) + str(i) + ',' + "0"*(4 - len(inscricao)) + inscricao + "," + objetiva + "," + discursiva + '\n')
        matriz[posicaoM][posicaoCandidato] = -1
    arquivo.close()    


notas = []
notasCotistas = [] #Cotistas
notasNcotistas = [] #Ampla Concorrência
nVagas = random.randint(20, 100)
nCandidatos = random.randint(nVagas, 500)

notas = defineNotas(notas, nCandidatos)
escreveArq1('arqCandidatos.txt', nCandidatos, notasCotistas, notasNcotistas, notas)
defineClassificacao(notas, nCandidatos, 'classificacao.txt', 3, 0)
#defineClassificacao(notasCotistas, len(notasCotistas), 'classificacaoCotistas', 1, 0, 2)
"""
Ideia: usando a função max() podemos achar a maior média na coluna que tem a média na matriz que tem as notas. Depois
de usar o max(), vemos quantas vezes esse valor aparece na coluna das médias usando o count(). Se ele mostrar que tem
mais de um, chamamos uma função que ainda será criada que seria chamada de empate(). Nela, saberíamos quem tem a maior
nota na prova discursiva.
Na função empate, podemos ir usando o index nesse valor para encontrar a posição desses valores e também achar a maior
nota discursiva
Depois iríamos escrever no arquivo 2.
"""