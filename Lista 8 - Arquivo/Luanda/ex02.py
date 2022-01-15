"""
Grupo: Anna Paula Siqueira da Silva, Maria Laura Barbosa Soares, Luanda Rodrigues da Silva e Ariane Arantes dos Santos
Turma: 2BINFO

Faça um programa que crie dois arquivos textos para um revendedor de automóveis. O primeiro chamado “arq1.txt”, contendo
o código do carro e o modelo do carro, e um segundo arquivo chamado “arq2.txt”, contendo o código do carro, cor, preço 
e a quantidade disponível para a venda do modelo. Todos os dados serão inseridos pelo usuário. 

"""

def escrevenumaleatorios1(nomeArquivo):
    arquivo = (open, nomeArquivo, 'w')
    arquivo.write("Codigo,Modelo""\n")
    while(codigo != "FIM"):
        codigo = input("Digite o código do carro: ")
        if(codigo != "FIM"):
            modelo = input("Digite o modelo: ")
            arquivo.write(codigo + "," + modelo + '\n')
    arquivo.close()

def escrevenumaleatorios2(nomeArquivo):
    arquivo = (open, nomeArquivo, 'w')
    arquivo.write("Codigo,Cor,Preço,Quantidade""\n")
    while(codigo != "FIM"):
        codigo = input("Digite o código do carro: ")
        if(codigo != "FIM"):
            cor = input("Digite a cor: ")
            preço = input("Digite o preço: ")
            quant = input("Dgite a quantidade: ")
            arquivo.write(codigo + "," + cor + "," + preço + "," + quant +'\n')
    arquivo.close()

escrevenumaleatorios1("arquivo1.txt")
escrevenumaleatorios2("arquivo2.txt")


