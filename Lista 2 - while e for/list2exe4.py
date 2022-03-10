"""
Grupo: Anna Paula Siqueira da Silva
       Maria Laura Barbosa Soares
       Luanda Rodrigues da Silva
       Ariane Arantes dos Santos
Turma: 2BINFO 
"""
num = int(input('Digite um número: '))
a = 0
b = 1
i=0
#fibonacci
while i<=num:
    if(i == 0):
        c = 1
    else:
        c = a+b
        a = b
        b = c
    i +=1
i = num
while(i >= 0):
    if(i != 0):
        cont = b - 1
        conta = b
        while(cont >= 1):
            conta = conta *(b - cont)
            cont -= 1
        print(conta*"*")
    else:
        print("*")
    aux = a
    a = b - a
    b = aux
    i -= 1