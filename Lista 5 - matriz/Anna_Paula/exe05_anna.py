"""
Grupo: Anna Paula Siqueira da Silva, Maria Laura Soares Barbosa, Ariane Arantes dos Santos e Luanda Rodrigues da Silva
Turma: 2BINFO

Faça um programa que leia a ordem de uma matriz quadrada A (até 100), posteriormente leia seus valores e 
escreva sua transposta AT, onde AT[i][j] = A[j][i]
"""
matriz = []
matrizT = []
tam = int(input("Digite o tamanho da matriz: "))
while(tam < 1 or tam > 100):
    print("Valor inválido")
    tam = int(input("Digite o tamanho da matriz: "))
#if(tam > 1 and tam <= 100):
print("\nDigite a ordem da matriz")
for i in range(tam):
    linha = []
    print(f"Linha {i + 1}")
    for j in range(tam):
        linha.append(int(input("Digite o número da matriz: ")))
    matriz.append(linha)
for i in range(tam):
    linha = []
    for j in range(tam):
        linha.append(matriz[j][i])
    matrizT.append(linha)
print("Matriz Transposta")
for i in range(tam):
    print(matrizT[i])
'''else:
    if(tam <= 1):
        print("O tamanho da matriz só pode ser maior que 1")
    else:
        print("O tamanho da matriz precisa ser menor ou igual a 100")'''