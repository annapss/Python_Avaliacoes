tam = 1000
vetor = [0] * tam
def percurso(n, i=0):
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
            print(f"\nO número {vetor[i]} aparece {vetor.count(vetor[i])} vezes")
        return contagem(tam, i + 1)
contagem(tam)