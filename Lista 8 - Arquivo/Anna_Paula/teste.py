discursivas = [-1,5, 2, 1, 4]
vetor = [-1,8.5, 5, 5, 8.5]
print(f"Vetor: {vetor}")
maiorDiscursiva = 0
inscricao = 0
while(vetor.count(8.5) != 0):
    if(discursivas[vetor.index(8.5)] > maiorDiscursiva):
        maiorDiscursiva = discursivas[vetor.index(8.5)]
        inscricao = vetor.index(8.5)
    vetor[vetor.index(8.5)] = -1
print(vetor)
print(f"Maior discursiva: {maiorDiscursiva}")
print(f"Inscricao: {inscricao}")
#print(f"Posição do primeiro 8.5: {vetor.index(8.5)}")
#print(f"{vetor[1:4]}")
#print(f"posição do segundo 8.5: {vetor.index(8.5)}")