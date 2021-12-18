"""
Grupo: Maria Laura Barbosa Soares, Anna Paula Siqueira da Silva, Luanda Rodrigues da Silva e Ariane Arantes dos Santos
Turma: 2BINFO

Faça um programa, utilizando recursão, que leia um vetor de 100 números inteiros, e em seguida os ordene em 
ordem decrescente de valor. (Não utilize estrutura de repetição, sob pena de anular a questão).
"""
tam = 5
vetor = [0] * tam
def percurso(n, i=0):
    if(i == n):
        return False
    else:
        vetor[i] = int(input("Digite um número: "))
        return percurso(tam, i + 1)
percurso(tam) 
vetor = sorted(vetor)
def decrescente(i = tam - 1):
    if(i == -1):
        return False
    else:
        print(f"{vetor[i]}", end=" ")
        return decrescente(i - 1)
decrescente()
