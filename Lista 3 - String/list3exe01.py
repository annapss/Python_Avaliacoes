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
termino = ''
espacos = 18
while(acabou == 0):
    verbo = input("Digite um verbo: ")
    if(verbo == 'FIM'):
        acabou = 1
    else:
        verbo = verbo.lower()
        final = verbo[len(verbo) - 2:len(verbo)]
        if(final == 'ar' or final == 'er' or final == 'ir'):
            for i in range(0,7):
                if(i == 0): #Tempos Verbais
                    print("Presente", end='\t')
                    print("Pretérito perfeito", end='\t')
                    print("Futuro do presente")
                elif(i == 1): #eu
                    termino = 'o'
                    print("Eu", end = " ")
                    print(verbo[0:len(verbo) - 2] + termino, end=" "*(espacos - len(termino))) #presente
                    if(final == 'ar'): #terminação ar
                        termino = 'ei'
                    else: # terminação er e ir
                        termino = 'i'
                    print(verbo[0:len(verbo) - 2] + termino,end=" "*(espacos - len(termino))) #pretérito perfeito
                    print(verbo + 'ei') #futuro do presente
                elif(i == 2): #tu
                    print("Tu", end=" ")
                    if(final == 'ar'): #terminação ar
                        termino = 'as'
                        print(verbo[0:len(verbo) - 2] + termino,end=" "*(espacos - len(termino))) #presente
                        termino = 'aste'
                        print(verbo[0:len(verbo) - 2] + termino,end=" "*(espacos - len(termino))) #preterito perfeito
                    else: #terminação er e ir
                        termino = 'es'
                        print(verbo[0:len(verbo) - 2] + termino, end=" "*(espacos - len(termino))) #presente
                        if(final == 'ir'):
                            termino = 'iste'
                        else:
                            termino = 'este'
                        print(verbo[0:len(verbo) - 2] + termino,end=" "*(espacos - len(termino))) #preterito perfeito
                    print(verbo + 'ás') #futuro do presente
                elif(i == 3): #ele
                    print("Ele", end = " ")
                    if(final == 'ar'): #terminação ar
                        termino = 'a'
                        print(verbo[0:len(verbo) - 2] + termino,end=" "*(espacos - len(termino) - 1)) #presente
                        termino = 'ou'
                        print(verbo[0:len(verbo) - 2] + termino, end=" "*(espacos - len(termino) - 1)) #preterito perfeito
                    else: #terminações er e ir
                        termino = 'e'
                        print(verbo[0:len(verbo) - 2] + termino, end=" "*(espacos - len(termino) - 1)) #presente
                        if(final == 'ir'):
                            termino = 'iu'
                        else:
                            termino = 'eu'
                        print(verbo[0:len(verbo) - 2] + termino,end=" "*(espacos - len(termino) - 1)) #preterito perfeito
                    print(" " + verbo + 'á') #futuro do presente               
                elif(i == 4): #nós
                    print("Nós",end=" ")
                    if(final == 'ar'): #terminação ar
                        termino = 'amos'
                        distancia = termino + " "*(espacos - len(termino) - 1)
                    elif (final == 'ir'): #terminação ir
                        termino = 'imos'
                        distancia = termino + " "*(espacos - len(termino) - 1)
                    else: #terminação er
                        termino = 'emos'
                        distancia = termino + " "*(espacos - len(termino) - 1)
                    print((verbo[0:len(verbo) - 2] + distancia)*2, end="") #preterito perfeito e presente
                    print(" " + verbo + 'emos') #futuro do presente
                elif(i == 5): #vós
                    print("Vós", end=" ")
                    if(final == 'ar'): #teminação ar
                        termino = 'ais'
                        print(verbo[0:len(verbo) - 2] + termino, end=" "*(espacos - len(termino) - 1)) #presente
                        termino = 'astes'
                        print(verbo[0:len(verbo) - 2] + termino, end=" "*(espacos - len(termino) - 1)) #preterito perfeito
                    else: #terminações er e ir
                        if(final == 'er'):
                            termino = 'eis'
                            print(verbo[0:len(verbo) - 2] + termino, end=" "*(espacos - len(termino) - 1)) #presente
                            termino = 'estes'
                            print(verbo[0:len(verbo) - 2] + termino, end=" "*(espacos - len(termino) - 1)) #preterito perfeito
                        else:
                            termino = 'is'
                            print(verbo[0:len(verbo) - 2] + termino, end=" "*(espacos - len(termino) - 1)) #presente
                            termino = 'istes'
                            print(verbo[0:len(verbo) - 2] + termino, end=" "*(espacos - len(termino) - 1)) #preterito perfeito
                    print(" " + verbo + 'eis')
                else: #eles
                    print("Eles", end=" ")
                    if(final == 'ar'): #terminação ar
                        termino = 'am'
                        print(verbo[0:len(verbo) - 2] + termino, end = " "*(espacos - len(termino) - 2)) #presente
                        termino = 'aram'
                        print(verbo[0:len(verbo) - 2] + termino, end=" "*(espacos - len(termino) - 2)) #preterito perfeito
                    else: #terminações er e ir
                        termino = 'em'
                        print(verbo[0:len(verbo) - 2] + termino, end=" "*(espacos - len(termino) - 2)) #presente
                        if(final == 'er'):
                            termino = 'eram'
                        else:
                            termino = 'iram'
                        print(verbo[0:len(verbo) - 2] + termino, end=" "*(espacos - len(termino) - 2)) #preterito perfeito
                    print("  " + verbo + 'ão') #futuro do presente
            print()
        else:
            print('O verbo deve estar no infinitivo')