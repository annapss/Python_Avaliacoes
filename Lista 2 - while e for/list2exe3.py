"""
Grupo: Anna Paula Siqueira da Silva
       Maria Laura Barbosa Soares
       Luanda Rodrigues da Silva
       Ariane Arantes dos Santos
Turma: 2BINFO 
"""
n = int(input("Digite um número: "))
i = 1
e = n * 2 - i * 2
while(i <= n):
    a = "*"*i
    print(end = a)
    print(end = " "*e)
    print(a)
    i += 1
    e -= 2
e = 2
i = n - 1
while(i >= 1):
    a = "*"*i
    print(end = a)
    print(end = " "*e)
    print(a)
    i -= 1
    e += 2