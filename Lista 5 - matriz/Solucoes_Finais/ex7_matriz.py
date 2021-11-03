"""
Grupo: Anna Paula Siqueira, Ariane Arantes, Luando Rodrigues e Maria Laura Soares
Turma: 2BINFO

7. Faça um programa que leia uma matriz 6x3 com
números reais, calcule e mostre: (a) o maior elemento da
matriz e sua respectiva posição (linha e coluna); (b) o
menor elemento da matriz e sua respectiva posição.
"""
m = 6
n = 3
matriz = []

for i in range(m):
    linha = []
    for j in range(n):
        linha.append(float(input(f'Digite um valor para [{i+1}][{j+1}]: ')))
    matriz.append(linha)

menor = 0
maior = 0
posicaoma = [0]*2
posicaome = [0]*2

for i in range(m): #verificação maior e menor elemento e sua respectiva posição
    for j in range(n):
        if i ==0 and j == 0:
            menor = matriz[i][j]
            posicaome[0] = i+1
            posicaome[1] = j+1
            maior = matriz[i][j]
            posicaoma[0] = i+1
            posicaoma[1] = j+1
        else:
            if matriz[i][j] < menor:
                menor = matriz[i][j]
                posicaome[0] = i+1
                posicaome[1] = j+1
            elif matriz[i][j] > maior:
                maior = matriz[i][j]
                posicaoma[0] = i+1
                posicaoma[1] = j+1

print(f'\nMatriz {m}x{n}:')
for i in range(m):
    print(matriz[i])

print(f'O menor elemento dessa matriz é o {menor} que ocupa a linha [{posicaome[0]}] e coluna [{posicaome[1]}]')
print(f'O maior elemento dessa matriz é o {maior} que ocupa a linha [{posicaoma[0]}] e coluna [{posicaoma[1]}]')
