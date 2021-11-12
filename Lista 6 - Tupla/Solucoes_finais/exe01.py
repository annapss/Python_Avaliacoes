"""
Grupo: Anna Paula Siqueira, Maria Laura Barbosa, Luanda Rodrigues e Ariane Arantes
Turma: 2BINFO

Crie um jogo para duas pessoas. Uma delas irá digitar diversos números. Em seguida a outra pessoa terá 10 tentativas para
adivinhar pelo menos 5 números que estejam na lista de números que o sue adversário digitou anteriormente. Se dentro de
suas 10 tentativas, o segundo jogador acertar 5 números, ele ganha. Caso contrário, o primeiro jogador ganha.
"""
print("É a vez do jogador 1!")
tam = int(input("Digite a quantidade de números que você irá digitar: "))
tupla = ()
for i in range(tam):
    x = int(input(f"Digite o {i + 1}° número: "))
    tupla += (x,)
    print()
print("\nÉ a sua vez jogador 2!")
i = 1
pontos = 0
while(i <= 10 and pontos != 5):
    print(f"Tentativa {i}")
    x = int(input("Digite a sua suposição: "))
    if(x in tupla):
        pontos += 1
    i += 1
    print()
if(pontos == 5):
    print("Parabéns jogador 2! Você ganhou!")
else:
    print("Parabéns jogador 1! Você ganhou!")