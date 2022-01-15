"""
Grupo: Anna Paula Siqueira da Silva, Maria Laura Barbosa Soares, Luanda Rodrigues da Silva e Ariane Arantes dos Santos
Turma: 2BINFO

A faculdade de informática de uma universidade possui 2 arquivos referentes aos dados dos candidatos que fizeram 
vestibular. O primeiro possui o número de inscrição, o nome do candidato e a renda familiar; o segundo possui a 
classificação do candidato, sua matrícula e suas notas nas provas objetivas e discursivas. O primeiro arquivo está 
ordenado por número de inscrição e o segundo arquivo está ordenado por classificação. Foi instituído o sistema de cotas
e essa universidade agora precisa destinar 25% de suas vagas aos melhores classificados com renda inferior ou igual 
a R$1000,00. Faça um programa que gere dois arquivos de saída, o primeiro contendo os nome, classificação inicial e 
classificação final, dos candidatos com renda inferior ou igual a R$1000,00, em ordem de inscrição e o segundo arquivo
contendo os nome, inscrição e classificação inicial dos candidatos que estavam classificados e que perderam a vaga 
após a instituição do sistema de cotas.
Obs.: Crie o primeiro arquivo mostrado abaixo de forma aleatória. Para criação do segundo arquivo, gere notas aleatórias
para as provas objetivas e discursivas de cada candidato existente no primeiro arquivo e em seguida ordene a 
classificação com relação às notas. O critério de ordenação será a média da objetiva com a discursiva. 
Se houver empates, o desempate será dado pela maior nota discursiva. 

"""

import random

def inscriçõesaleatorias(qtdnumeros):
    for i in range(qtdnumeros):
        print(random.randit(0,10))

inscriçõesaleatorias(10)

