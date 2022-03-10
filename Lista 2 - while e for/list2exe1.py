"""
Grupo: Anna Paula Siqueira da Silva
       Maria Laura Barbosa Soares
       Luanda Rodrigues da Silva
       Ariane Arantes dos Santos
Turma: 2BINFO 
"""
n = int(input("Digite um número: "))
i = 1
while(i <= n):
    print("*"*i)
    i += 1
i = n - 1
while(i >= 1):
    print(i*"*")
    i -= 1