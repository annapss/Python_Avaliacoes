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
def decrescente(i=tam - 1):
    if(i == -1):
        return False
    else:
        print(f"{vetor[i]}", end=" ")
        return decrescente(i - 1)
decrescente()
