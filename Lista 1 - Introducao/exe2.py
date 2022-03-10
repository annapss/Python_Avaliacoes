'''
Grupo: Anna Paula Siqueira, Maria Laura Soares, Luanda Rodrigues e Ariane Arantes - 2BINFO

Questão 2
Um marciano chegou a uma floresta e se escondeu atrás de uma das 100 árvores quando viu um caçador. 
O caçador só tinha cinco balas em sua espingarda. Cada vez que ele atirava, e não acertava, é claro,
o marciano dizia: estou mais à direita ou mais à esquerda. Se o caçador não conseguir acertar o marciano, 
ele será levado para marte. Implemente esse jogo para dois jogadores, 
onde um escolhe a árvore em que o marciano irá se esconder, 
e o outro tenta acertar. 
Obs.: Não permita, em hipótese alguma, que seja escolhida uma árvore fora do intervalo entre 1 e 100. 
'''
marciano = int(input('Marciano, escolha a sua árvore: '))
if(marciano <= 1 or marciano >= 100):
    print('Esta árvore é inválida')
else:
    cacador = int(input('Cacador, escolha a sua aposta: ')) # 1 chute
    if(cacador <= 1 or cacador >= 100):
        print('Esta árvore é inválida')
    else:
        if(cacador == marciano):
            print("Parabéns caçador! Você acertou")
        else:
            if(cacador > marciano):
                print("O marciano está mais para a esquerda")
            else:
                print("O marciano está mais a direita")
            cacador = int(input('Cacador, outra aposta: ')) # 2 chute
            if(cacador <= 1 or cacador >= 100):
                print('Esta árvore é inválida')
            else:
                if(cacador == marciano):
                    print("Parabéns caçador! Você acertou")
                else:
                    if(cacador > marciano):
                        print("O marciano está mais para a esquerda")
                    else:
                        print("O marciano está mais a direita")
                    cacador = int(input('Caçador, digite outra aposta: '))
                    if(cacador <= 1 or cacador >= 100): # 3 chute
                        print('Esta árvore é inválida')
                    else:
                        if(cacador == marciano):
                            print("Parabéns caçador! Você acertou")
                        else:
                            if(cacador > marciano):
                                print("O marciano está mais para a esquerda")
                            else:
                                print("O marciano está mais a direita")
                            cacador = int(input('Caçador, digite outra aposta: '))
                            if(cacador <= 1 or cacador >= 100): # 4 chute
                                print('Esta árvore é inválida')
                            else:
                                if(cacador == marciano):
                                    print("Parabéns caçador! Você acertou")
                                else:
                                    if(cacador > marciano):
                                        print("O marciano está mais para a esquerda")
                                    else:
                                        print("O marciano está mais a direita")
                                    cacador = int(input('Caçador, digite outra aposta: '))
                                    if(cacador <= 1 or cacador >= 100): # 5 chute
                                        print('Esta árvore é inválida')
                                    else:
                                        if(cacador == marciano):
                                            print("Parabéns caçador! Você acertou")
                                        else:
                                            print("Caçador errou e acabou com todas as balas!")
                                            print("O Marciano ganhou e foi para Marte!")