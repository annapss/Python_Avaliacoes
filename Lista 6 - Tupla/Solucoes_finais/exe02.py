"""
Grupo: Anna Paula Siqueira da Silva, Luanda Rodrigues da Silva, Maria Laura Barbosa Soares e Ariane Arantes dos Santos
Turma: 2BINFO

Crie uma tupla preenchida com os 10 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois, leia o nome de um time e imprima a sua colocação na tabela. Quando for digitado FIM, 
o programa acaba.

"""
tupla = ("atletico-mg", "palmeiras", "flamengo", "fortaleza", "bragantino", "corinthias", "internacional", "fluminense", "atletico-pr", "america-mg")
time = ""

while(time != "FIM"):
    time = input("Digite seu time: ").lower()
    if(time != "fim"):
        if(time in tupla): 
            i = 0
            achei = 0
            while(i < len(tupla) and achei == 0):
                if(tupla[i] == time):
                    posicao = i
                    achei = 1
                i += 1
            print(f"Seu time está na {posicao + 1}° posição")
        else:
            print("Seu time não está entre os 10 primeiros")
        print()
    else:
        time = time.upper()