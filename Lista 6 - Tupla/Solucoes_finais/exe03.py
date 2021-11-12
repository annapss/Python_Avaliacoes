'''
Grupo: Anna Paula Siqueira, Maria Laura Barbosa, Luanda Rodrigues e Ariane Arantes
Turma: 2BINFO

Em uma competição de salto em distância cada atleta tem direito a 3 saltos.
O resultado do atleta será determinado pela média dos 3 saltos. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas 
pelo atleta em seus saltos e depois informe o nome e a média 
dos saltos. O programa deve ser encerrado quando for digitado "FIM" o nome do atleta.

'''
tuplaMedia = ()
tuplaNome = ()
nome = ""
tam = 3

while(nome != "FIM"):
    nome = input("Digite o nome: ")
    if(nome != "FIM"):
        tuplaNome += (nome, )
        soma = 0
        for i in range(tam):
            soma += float(input(f"Digite a nota do salto {i + 1}: "))
        tuplaMedia += (soma / tam, )
        print()
for i in range(len(tuplaNome)):
    print(f"O atleta {tuplaNome[i]} teve média {tuplaMedia[i]:.2f}")
