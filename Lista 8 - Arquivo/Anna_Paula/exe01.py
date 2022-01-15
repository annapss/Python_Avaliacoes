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
    for i in range(nLetras):
        if(i % 2 == 0):
            nome += random.randint(0, len(vogais) - 1)
        else:
            nome += random.randint(0, len(consoantes) - 1)
    return nome
def escreveArq1(nomeArquivo, nCandidatos): #Arquivo 1 pronto! :)
    arquivo = open(nomeArquivo, 'w')
    arquivo.write("Inscricao,Nome,Renda")
    for i in range(1, nCandidatos + 1):
        arquivo.write("0"*(4 - len(str(i))) + str(i) + ',' + nomeAleatorio(random.randint(4, 10)) + ',R$' + str(random.randint(50000, 500000) / 100))
    arquivo.close()

def defineNotas(notas, nCandidatos): #Definindo as notas dos canditados e colocando em um vetor
    objetivas = [''] #Valor na posicao 0 em cada vetor
    discursivas = ['']
    medias = ['']
    for i in range(1,nCandidatos + 1):
        objetivas.append(str(random.randint(0, 1000) /100))
        discursivas.append(str(random.randint(0, 1000) /100))
        medias.append((str(objetivas[i] + discursivas[i]) / 2)) #Talvez tenha arrendondar para 2 casas decimais
    notas.append(objetivas)
    notas.append(discursivas)
    notas.append(medias)
