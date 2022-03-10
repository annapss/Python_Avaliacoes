"""
Grupo: Anna Paula Siqueira da Silva
       Maria Laura Barbosa Soares
       Luanda Rodrigues da Silva
       Ariane Arantes dos Santos
Turma: 2BINFO 
"""
n = int(input("Digite um número: "))
i = 1
a = 2
e = n - 1
while(i <= n):
    print(end=" "*e)
    print(end="*"*a)
    print(" "*e)
    i += 1
    e -= 1
    a += 2
#print(a, e)
a -= 4
e += 2
i = 1
#print(a)
while(i <= n):
    print(end = " "*e)
    print(end = "*"*a)
    print(" "*e)
    e += 1
    a -= 2
    i += 1
