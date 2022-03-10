'''
Grupo: Anna Paula Siqueira, Maria Laura Soares, Luanda Rodigues e Ariane Arantes - 2BINFO

Questão 3
Faça um programa que recebe um número inteiro no intervalo de 1 até 1 milhão e o escreva na tela por extenso. 
'''
numero = input("Digite um número: ")
nAlgarismos = len(numero)
numero = int(numero)
unidade = -1
dezena = -1
centena = -1
milharU = -1
milharD = -1
milharC = -1
zeros = 0
if(nAlgarismos > 7):
    print("Esse número é inválido")
else:
    if(nAlgarismos == 7):
        print("um milhão")
    elif(nAlgarismos == 1 and numero == 0):
        print('zero')
    else: #Aqui a gente pega cada algarismo separadamente
        if(nAlgarismos >= 1):
            unidade = (numero // 1) % 10
            if(nAlgarismos >= 2):
                dezena = (numero // 10) % 10
                if(nAlgarismos >= 3):
                    centena = (numero // 100) % 10
                    if(nAlgarismos >= 4):
                        milharU = (numero // 1000) % 10
                        if(nAlgarismos >= 5):
                            milharD = (numero // 10000) % 10
                            if(nAlgarismos == 6):
                                milharC = numero // 100000
        if(milharC != -1): #Se tiver um número na casa da centena de milhar, imprimimos de acordo com o número
            if(milharC == 1): #Caso específico para milharC = 1
                if(milharD == 0):
                    print(end = "cem")
                else:
                    print(end = "cento")
            elif(milharC == 2):
                print(end = "duzentos")
            elif(milharC == 3):
                print(end = "trezentos")
            elif(milharC == 4):
                print(end = "quatrocentos")
            elif(milharC == 5):
                print(end = "quinhentos")
            elif(milharC == 6):
                print(end = "seiscentos:")
            elif(milharC == 7):
                print(end = "setecentos")
            elif(milharC == 8):
                print(end = "oitocentos")
            elif(milharC == 9):
                print(end = "novecentos")
        if(milharD != -1): #Se tiver um número na casa da dezena de milhar, imprimimos de acordo com o número
            if(nAlgarismos != 5 and milharD != 0):
                    print(end = " e ")
            if(milharD == 1): # milharD = 1 é um caso específico já que a escrita é um pouco diferente
                if(milharU == 1):
                    print(end = "onze")
                elif(milharU == 2):
                    print(end = "doze")
                elif(milharU == 3):
                    print(end = "treze")
                elif(milharU == 4):
                    print(end = "quatorze")
                elif(milharU == 5):
                    print(end = "quinze")
                elif(milharU == 6):
                    print(end = "dezesseis")
                elif(milharU == 7):
                    print(end = "dezesete")
                elif(milharU == 8):
                    print(end = "dezoito")
                elif(milharU == 0):
                    print(end = "dez")
                else:
                    print(end = "dezenove")
            elif(milharD == 2):
                print(end = "vinte")
            elif(milharD == 3):
                print(end = "trinta")
            elif(milharD == 4):
                print(end = "quarenta")
            elif(milharD == 5):
                print(end = "cinquenta")
            elif(milharD == 6):
                print(end = "sessenta")
            elif(milharD == 7):
                print(end = "setenta")
            elif(milharD == 8):
                print(end = "oitenta")
            elif(milharD == 9):
                print(end = "noventa")
        if(milharU != -1): #Se tiver um número na casa da unidade de milhar, imprimimos de acordo com o número
            if(milharD != 1):
                if(nAlgarismos != 4 and milharU != 0):
                    print(end = " e ")
                if(milharU == 1):
                    if(nAlgarismos != 4):
                        print(end = "um")
                elif(milharU == 2):
                    print(end = "dois")
                elif(milharU == 3):
                    print(end = "três")
                elif(milharU == 4):
                    print(end = "quatro")
                elif(milharU == 5):
                    print(end = "cinco")
                elif(milharU == 6):
                    print(end = "seis")
                elif(milharU == 7):
                    print(end = "sete")
                elif(milharU == 8):
                    print(end = "oito")
                elif(milharU == 9):
                    print(end = "nove")
        if(nAlgarismos > 3):
            if(numero >= 2000):
                print(end = " ")
            print(end = "mil")
        if(centena != -1): #Se tiver um número na casa da centena, imprimimos de acordo com o número
            if(numero >= 1100):
                print(end = " ")
            if(nAlgarismos == 4 and dezena == 0 and unidade == 0):
                print(end = "e ")
            if(centena == 1): #Caso específico para centena = 1
                if(dezena == 0 and unidade == 0): #numero = 100
                    print(end = "cem")
                else: #numero != 100
                    print(end = "cento")
            elif(centena == 2):
                print(end = "duzentos")
            elif(centena == 3):
                print(end = "trezentos")
            elif(centena == 4):
                print(end = "quatrocentos")
            elif(centena == 5):
                print(end = "quinhentos")
            elif(centena == 6):
                print(end = "seiscentos")
            elif(centena == 7):
                print(end = "setecentos")
            elif(centena == 8):
                print(end = "oitocentos")
            elif(centena == 9):
                print(end = "novecentos")
        if(dezena != -1): #Se tiver um número na casa da dezena, imprimimos de acordo com o número
            if(nAlgarismos != 2 and dezena != 0):
                    print(end = " e ")
            if(dezena == 1): #caso específico para dezena = 1 porque a escrita é um pouco diferente 
                if(unidade == 1):
                    print(end = "onze")
                elif(unidade == 2):
                    print(end = "doze")
                elif(unidade == 3):
                    print(end = "treze")
                elif(unidade == 4):
                    print(end = "quatorze")
                elif(unidade == 5):
                    print(end = "quinze")
                elif(unidade == 6):
                    print(end = "dezesseis")
                elif(unidade == 7):
                    print(end = "dezesete")
                elif(unidade == 8):
                    print(end = "dezoito")
                elif(unidade == 0):
                    print(end = "dez")
                else:
                    print(end = "dezenove")
            elif(dezena == 2):
                print(end = "vinte")
            elif(dezena == 3):
                print(end = "trinta")
            elif(dezena == 4):
                print(end = "quarenta")
            elif(dezena == 5):
                print(end = "cinquenta")
            elif(dezena == 6):
                print(end = "sessenta")
            elif(dezena == 7):
                print(end = "setenta")
            elif(dezena == 8):
                print(end = "oitenta")
            elif(dezena == 9):
                print(end = "noventa")
        if(unidade != -1): #Se tiver um número na casa da unidade, imprimimos de acordo com o número
            if(dezena != 1):
                if(nAlgarismos != 1 and unidade != 0):
                    print(end = " e ")
                if(unidade == 1):
                    print(end = "um")
                elif(unidade == 2):
                    print(end = "dois")
                elif(unidade == 3):
                    print(end = "três")
                elif(unidade == 4):
                    print(end = "quatro")
                elif(unidade == 5):
                    print(end = "cinco")
                elif(unidade == 6):
                    print(end = "seis")
                elif(unidade == 7):
                    print(end = "sete")
                elif(unidade == 8):
                    print(end = "oito")
                elif(unidade == 9):
                    print(end = "nove")   