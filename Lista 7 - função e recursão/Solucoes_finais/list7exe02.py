"""
Grupo: Maria Laura Barbosa Soares, Anna Paula Siqueira da Silva, Luanda Rodrigues da Silva e Ariane Arantes dos Santos
Turma: 2BINFO

Faça um programa, utilizando recursão, que leia um vetor de 1000 números inteiros e em seguida informe a 
quantidade de cada número que foi digitado nesse vetor. (Não utilize estrutura de repetição, 
sob pena de anular a questão).
"""
tam = 1000
vetor = [0] * tam
def percurso(n, i=0): #função para percorrer o vetor e adicionar as entradas
    if(i == n):
        return False
    else:
        vetor[i] = int(input("Digite um número: "))
        return percurso(tam, i + 1)
percurso(tam)
passei = []
def contagem(n, i=0):
    if(i == n):
        return False
    else:
        if(vetor[i] not in passei):
            passei.append(vetor[i])
            if vetor.count(vetor[i]) == 1:
                print(f"\nO número {vetor[i]} aparece {vetor.count(vetor[i])} vez")
            else:
                print(f"\nO número {vetor[i]} aparece {vetor.count(vetor[i])} vezes")
        return contagem(tam, i + 1)
contagem(tam)