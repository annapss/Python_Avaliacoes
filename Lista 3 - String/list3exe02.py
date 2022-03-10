"""
Grupo: Maria Laura Soares, Anna Paula Siqueira, Ariane Arantes e Luanda Rodrigues
Turma: 2BINFO

Faça um programa que leia uma frase e uma palavra e em seguida determine o número de vezes que a palavra 
aparece na frase. 
Exemplo: Frase:  Ana e Mariana gostam de banana. 
Palavra: ana Temos que a palavra ana ocorre 4 vezes na frase. 
"""
frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")
frase = frase.lower()
palavra = palavra.lower()
inicio = 0
fim = frase.find(palavra)
cont = 0
if(fim != -1):
    while(fim != -1):
        cont += 1
        inicio = fim + 1
        fim = frase.find(palavra, inicio)
    print(f'A palavra aparece na frase {cont} vezes')
else:
    print(f'A palavra não aparece na frase')