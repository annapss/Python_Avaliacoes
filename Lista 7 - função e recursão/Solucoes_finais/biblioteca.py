def percurso(n, vetor, i=0):
    if(i == n):
        return False
    else:
        vetor[i] = int(input("Digite um número: "))
        return percurso(n, i + 1)