"""
Grupo: Maria Laura Soares, Anna Paula Siqueira, Ariane Arantes e Luanda Rodrigues
Turma: 2BINFO

Faça um programa para conjugar verbos regulares (terminados em ar, er e ir), no presente, pretérito perfeito e 
no futuro do presente. O usuário deve entrar com o verbo no infinitivo pessoal (ex.: amar, beber, partir, etc.). 
O programa deve verificar se o verbo está no infinitivo, se não estiver deve mandar a mensagem: 
“O verbo deve estar no infinitivo”, e pedir para o usuário entrar novamente com o verbo. 
Seu programa deve ler o verbo, mostrar as conjugações nas 3 pessoas do singular e nas 3 pessoas do plural, 
incluindo os pronomes pessoais (eu, tu, ele, nós, vós, eles). O programa deve terminar quando for digitado a 
palavra “FIM”. 
"""
verbo = ''
acabou = 0
while(acabou == 0):
    verbo = input("Digite um verbo: ")
    verbo.lower()
    final = verbo[len(verbo) - 2:len(verbo)]
    if(final == 'ar' or final == 'er' or final == 'ir'):
        for i in range(0,7):
            if(i == 0):
                print("Presente", end='\t')
                print("Pretérito perfeito", end='\t')
                print("Futuro do presente")
            elif(i == 1): #eu
                print(verbo[0:len(verbo) - 2] + 'o', end='\t')
                if(final == 'ar'): #preterito perfeito
                    print(verbo[0:len(verbo) - 2] + 'ei',end='\t')
                else:
                    print(verbo[0:len(verbo) - 2] + 'i',end='\t')
                print(verbo + 'ei')
            elif(i == 2): #tu
                if(final == 'ar'):
                    print(verbo[0:len(verbo) - 2] + 'as',end='\t')
                    print(verbo[0:len(verbo) - 2] + 'aste',end='\t')
                else:
                    print(verbo[0:len(verbo) - 2] + 'es', end='\t')
                    print(verbo[0:len(verbo) - 1] + 'ste',end='\t')
                print(verbo + 'ás')
            elif(i == 3): #ele
                if(final == 'ar'):
                    print(verbo[0:len(verbo) - 2] + 'a',end='\t')
                    print(verbo[0:len(verbo) - 2] + 'ou', end='\t')
                else:
                    print(verbo[0:len(verbo) - 2] + 'e', end='\t')
                    print(verbo[0:len(verbo) - 1] + 'u',end='\t')
                print(verbo + 'á')                    
            elif(i == 4): #nós
                if(final == 'ar'):
                    print((verbo[0:len(verbo) - 1] + 'mos\t')*2, end='')
                else:
                    print((verbo[0:len(verbo) - 1] + 'mos\t')*2, end='')
                print(verbo + 'emos')
            elif(i == 5): #vós
                if(final == 'ar'):
                    print(verbo[0:len(verbo) - 2] + 'ais', end='\t')
                    print(verbo[0:len(verbo) - 2] + 'astes', end='\t')
                else:
                    if(final == 'er'):
                        print(verbo[0:len(verbo) - 1] + 'is', end='\t')
                    else:
                        print(verbo[0:len(verbo) - 1] + 's', end='\t')
                    print(verbo[0:len(verbo) - 1] + 'stes', end='\t')
                print(verbo + 'eis')
            else: #eles
                if(final == 'ar'):
                    print(verbo[0:len(verbo) - 2] + 'am', end='\t')
                else:
                    print(verbo[0:len(verbo) - 2] + 'em', end='\t')
                print(verbo + 'am', end='\t')
                print(verbo + 'ão')
    else:
        if(verbo != 'FIM'):
            print('O verbo deve estar no infinitivo')
        else:
            acabou = 1