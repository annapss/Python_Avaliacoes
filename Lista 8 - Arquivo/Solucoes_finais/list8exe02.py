"""
Grupo: Anna Paula Siqueira da Silva, Maria Laura Barbosa Soares, Luanda Rodrigues da Silva e Ariane Arantes dos Santos
Turma: 2BINFO

Faça um programa que crie dois arquivos textos para um revendedor de automóveis. 
O primeiro chamado “arq1.txt”, contendo o código do carro e o modelo do carro, e um segundo arquivo 
chamado “arq2.txt”, contendo o código do carro, cor, preço e a quantidade disponível para a venda do modelo. 
Todos os dados serão inseridos pelo usuário. 
"""
def escreveA(nomeArquivo):
    arquivo = open(nomeArquivo, 'w')
    arquivo.write("Codigo,Modelo\n")
    codigo = ""
    while(codigo != "FIM"):
        codigo = input("Digite o código do carro: ")
        if(codigo != "FIM"):
            modelo = input("Digite o modelo: ")
            arquivo.write(codigo + "," + modelo + '\n')
            print()
    arquivo.close()

def escreveB(nomeArquivo):
    arquivo = open(nomeArquivo, 'w')
    arquivo.write("Codigo,Cor,Preco,Quantidade\n")
    codigo = ""
    while(codigo != "FIM"):
        codigo = input("Digite o código do carro: ")
        if(codigo != "FIM"):
            cor = input("Digite a cor: ")
            preco = input("Digite o preço: ")
            quant = input("Dgite a quantidade: ")
            arquivo.write(codigo + "," + cor + "," + preco + "," + quant +'\n')
            print()
    arquivo.close()

print("Arquivo 1:\n")
escreveA("arq1.txt")
print("\nArquivo 2:\n")
escreveB("arq2.txt")