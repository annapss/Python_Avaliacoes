'''
Grupo: Anna Paula Siqueira, Maria Laura Soares, Luanda Rodrigues e Ariane Arantes - 2BINFO

Questão 1
Faça um programa que leia uma data no formato dd – mm – aaaa. 
E em seguida escreva qual será o próximo dia, mês e ano. 
Obs.: Verifique todas as possibilidades. Lembre-se que existem anos bissextos. 
Não permita que o usuário digite uma data inválida.
'''
dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')
invalida = 0
if(len(dia) != 2 or len(mes) != 2 or len(ano) != 4): #Checa se a quantidade de caracteres está certa
    print("Data inválida")
else:
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    if(mes < 1 or mes > 12): #Checa se o mês existe
        print("Data inválida")
    else:           
        if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12): #31 dias
            if(dia == 31 and mes == 12): #31 de dezembro
                dia = 1
                mes = 1
                ano += 1
            else:
                if(dia <= 31 and dia >= 1):
                    if(dia == 31):
                        dia = 1
                        mes += 1
                    else:
                        dia += 1
                else:
                    invalida = 1
                    print("Data inválida")
        elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
            if(dia <= 30 and dia >= 1): #30 dias
                if(dia == 30):
                    dia = 1
                    mes += 1            
                else:
                    dia += 1
            else:
                invalida = 1
                print("Data inválida")
        else: 
            if((ano % 100 == 0 and ano % 400 == 0) or (ano % 100 != 0 and ano % 4 == 0)):
                if(dia <= 29 and dia >= 1):
                    if(dia == 29):
                        dia = 1
                        mes = 3
                    else:
                        dia += 1 
                else:
                    invalida = 1
                    print("Data inválida") #fevereiro quando o ano não é bissexto
            else:
                if(dia <= 28 and dia >= 1):
                    if(dia == 28):
                        dia = 1
                        mes = 3
                    else:
                        dia += 1
                else:
                    invalida = 1
                    print("Data inválida")
        if(invalida == 0):
            dia = str(dia)
            mes = str(mes)
            ano = str(ano)
            if(len(dia) == 1):
                print(end = f'0{dia} - ')
            else:
                print(end = f'{dia} - ')
            if(len(mes) == 1):
                print(end = f'0{mes} - ')
            else:
                print(end = f'{mes} - ')
            print(ano)