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
def escreveArq1(nomeArquivo, nCandidatos, notasCotistas, inscricoesAmpla, notas): #Arquivo 1 pronto! :)
    arquivo = open(nomeArquivo, 'w')
    arquivo.write("Inscricao,Nome,Renda\n")
    inscricaoC = [-1]
    notasC = [-1]
    discursivaC = [-1]
    for i in range(1, nCandidatos + 1):
        #Fiz esse if só para terem candidatos cotistas e não cotistas
        if(i % 2 == 0):
            renda = random.randint(100100, 500000) / 100 #não cotista
        else: 
            renda = random.randint(50000, 100000) / 100 #cotista
        if(renda <= 1000):
            inscricaoC.append(i)
            notasC.append(notas[3][i])
            discursivaC.append(notas[2][i])
        elif(renda > 1000):
            inscricoesAmpla.append(i)
        arquivo.write("0"*(5 - len(str(i))) + str(i) + ',' + nomeAleatorio(random.randint(4, 10)) + ',R$' + str(renda) + '\n')
    notasCotistas.append(inscricaoC) #0
    notasCotistas.append(notasC) #1
    notasCotistas.append(discursivaC) #2
    #inscricoesAmpla.append(inscricaoA) #0
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
def pegaNome(inscricao, nomeArquivo):
    arquivoNome = open(nomeArquivo)
    linha = arquivoNome.readline()
    while(linha != ""):
        if(inscricao in linha):
            posVirgula = linha.index(",")
            i = posVirgula + 1
            nome = ''
            while(linha[i] != ","):
                nome += linha[i]
                i += 1
            arquivoNome.close()
            return nome
        linha = arquivoNome.readline()
def pegaClassificacao(inscricao, nomeArquivo):
    arquivoClassificacao = open(nomeArquivo)
    linha = arquivoClassificacao.readline()
    while(linha != ""):
        if(inscricao in linha):
            arquivoClassificacao.close()
            return linha[0:4]
        linha = arquivoClassificacao.readline()
def defineClassificacao(matriz, nCandidatos, nomeArquivo, posicaoM, posicaoI, tipo, posicaoD = 2, posicaoO = 1): #Faz a classificação e já escreve no arquivo 2
    arquivo = open(nomeArquivo, 'w')
    if(tipo == 1):
        arquivo.write("Classificacao,Inscricao,Objetiva,Discursiva\n")
    elif(tipo == 3):
        arquivo.write("Nome,Classificacao Inicial,Classificacao Final\n")
    i = 0
    if(tipo == 2): #Faz a matriz dos cotistas de acordo com a classificacao final
        matrizCotistas = []
        nome = [-1]
        classificacaoInicial = [-1]
        classificacaoFinal = [-1]
        numeroInscricao = [-1]
    while(matriz[posicaoM].count(-1) != nCandidatos + 1):
        i += 1
        maiorMedia = max(matriz[posicaoM])
        posicaoCandidato = matriz[posicaoM].index(maiorMedia)
        if(matriz[posicaoM].count(maiorMedia) != 1):
            posicaoCandidato = empate(maiorMedia, matriz, posicaoM, posicaoD)
        else:
            posicaoCandidato = matriz[posicaoM].index(maiorMedia)
        inscricao = str(matriz[posicaoI][posicaoCandidato])
        if(tipo == 1):
            discursiva = str(matriz[posicaoD][posicaoCandidato])
            objetiva = str(matriz[posicaoO][posicaoCandidato])
            arquivo.write("0"*(4 - len(str(i))) + str(i) + ',' + "0"*(5 - len(inscricao)) + inscricao + "," + objetiva + "," + discursiva + '\n')
        elif(tipo == 2): #Faz a matriz com a classificao (não está em ordem de inscricao)
            parteInscricao = "0"*(5 - len(inscricao))
            nome.append(pegaNome(parteInscricao + inscricao, 'arqCandidatos.txt'))
            classificacaoInicial.append(pegaClassificacao(parteInscricao + inscricao, 'classificacao.txt'))
            classificacaoFinal.append(i)
            numeroInscricao.append(int(inscricao))
        elif(tipo == 3):
            nomeCandidato = str(matriz[0][posicaoCandidato])
            classInicial = str(matriz[1][posicaoCandidato])
            classFinal = str(matriz[2][posicaoCandidato])
            arquivo.write(inscricao + "," + nomeCandidato + "," + "0"*(4 - len(classInicial)) + classInicial + "," + "0"*(4 - len(classFinal)) + classFinal + "\n")
        matriz[posicaoM][posicaoCandidato] = -1
    if(tipo == 2):
        matrizCotistas.append(nome) #0
        matrizCotistas.append(classificacaoInicial) #1
        matrizCotistas.append(classificacaoFinal) #2
        matrizCotistas.append(numeroInscricao) #3
        return matrizCotistas
    arquivo.close()    

def escreveAmpla(nomeArquivo, vetor):
    arquivo = open(nomeArquivo, 'w')
    arquivo.write("Nome,Inscricao,Classificacao Inicial\n")
    for i in range(1,len(vetor)):
        inscricao = str(vetor[i])
        parteInscricao = "0"*(5 - len(inscricao))
        nome = pegaNome(parteInscricao + inscricao, 'arqCandidatos.txt')
        classificacaoInicial = pegaClassificacao(parteInscricao + inscricao, 'classificacao.txt')
        arquivo.write(nome + "," + "0"*(5 - len(inscricao)) + inscricao + "," + "0"*(4 - len(classificacaoInicial)) + classificacaoInicial + '\n')
    arquivo.close()

notas = []
notasCotistas = [] #Cotistas
inscricoesAmpla = [-1] #Ampla Concorrência
matrizCotistas = []
nVagas = random.randint(20, 100)
nCandidatos = 5 #random.randint(nVagas, 500)

notas = defineNotas(notas, nCandidatos)
escreveArq1('arqCandidatos.txt', nCandidatos, notasCotistas, inscricoesAmpla, notas)
defineClassificacao(notas, nCandidatos, 'classificacao.txt', 3, 0, 1)
matrizCotistas = defineClassificacao(notasCotistas, len(notasCotistas), 'classificacaoCotistas.txt', 1, 0, 2) #Faz a classificacao Final
defineClassificacao(matrizCotistas, len(notasCotistas), 'classificacaoCotistas.txt', 3, 3, 3) #Escreve no arquivo em ordem de inscricao
escreveAmpla("ampla.txt", inscricoesAmpla)
"""
Ideia: usando a função max() podemos achar a maior média na coluna que tem a média na matriz que tem as notas. Depois
de usar o max(), vemos quantas vezes esse valor aparece na coluna das médias usando o count(). Se ele mostrar que tem
mais de um, chamamos uma função que ainda será criada que seria chamada de empate(). Nela, saberíamos quem tem a maior
nota na prova discursiva.
Na função empate, podemos ir usando o index nesse valor para encontrar a posição desses valores e também achar a maior
nota discursiva
Depois iríamos escrever no arquivo 2.
"""