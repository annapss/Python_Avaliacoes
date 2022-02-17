"""
Grupo: Anna Paula Siqueira da Silva, Maria Laura Barbosa Soares, Luanda Rodrigues da Silva e 
Ariane Arantes dos Santos

Turma: 2BINFO

1. Criar LSEC, LDEC, LSED, LDED, LSECD e LDECD na ordem em que os elementos foram digitados
2. Criar LSEC, LDEC, LSED, LDED, LSECD e LDECD na ordem inversa em que os elementos foram digitados
3. Inserir elemento mantendo a lista ordenada (se a lista existir, supor que a mesma está em ordem 
crescente de valor). LSEC, LDEC, LSED, LDED, LSECD e LDECD.
4. Criar LSEC, LDEC, LSED, LDED, LSECD e LDECD em ordem crescente de valor
5. Remover um elemento de uma LSEC, LDEC, LSED, LDED, LSECD e LDECD.
6. Apagar a lista da mémoria LSEC, LDEC, LSED, LDED, LSECD e LDECD.
"""

class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
    
class ListaDuplaDescritor:
    def __init__(self, quant = 0):
        self.inicio = None
        self.fim = None
        self.quant = quant

    def mostrar(self):
        aux = self.inicio
        if(aux == None):
            print("Lista Vazia!\n")
        else:
            while(aux != None):
                print(aux.valor, end = " ")
                aux = aux.prox

    def inserirFim(self, valor):
        item = No(valor)
        if(self.inicio == None): #Lista vazia
            self.inicio = item
            self.fim = item
        else:
            self.fim.prox = item
            self.fim = item
        self.quant += 1

    def CriarOrdemDigitada(self):
        valor = int(input("Digite o valor que será inserido: "))
        while(valor >= 0):
            self.inserirFim(valor)
            valor = int(input("Digite o valor que será inserido: "))
    
    def inserirInicio(self, valor):
        item = No(valor)
        if(self.inicio == None): #Lista vazia
            self.inicio = item
            self.fim = item
        else:
            item.prox = self.inicio
            self.inicio = item
        self.quant += 1

    def CriarInversa(self):
        valor = int(input("Digite o valor que será inserido: "))
        while(valor >= 0):
            self.inserirInicio(valor)
            valor = int(input("Digite o valor que será inserido: "))

    def inserirOrdenado(self, valor):
        if(self.inicio == None or (valor < self.inicio.valor)):
            self.inserirInicio(valor)
        else:
            if(valor > self.fim.valor):
                self.inserirFim(valor)
            else:
                maior = self.inicio
                while(maior.valor < valor and maior.prox != None):
                    menor = maior
                    maior = maior.prox
                if(valor < maior.valor):
                    menor.prox = No(valor)
                    menor.prox.prox = maior
        self.quant += 1
    
    def CriarCrescente(self):
        valor = int(input("Digite o valor que será inserido: "))
        while(valor >= 0):
            self.inserirOrdenado(valor)
            valor = int(input("Digite o valor que será inserido: "))

lista = ListaDuplaDescritor()
lista.CriarCrescente()
lista.mostrar()
"""lista.inserirOrdenado(9)
lista.inserirOrdenado(3)
lista.inserirOrdenado(10)
lista.inserirOrdenado(6)
lista.mostrar()
lista.inserirFim(9)
lista.mostrar()
print()
lista.inserirFim(6)
lista.mostrar()
print()
lista.inserirFim(3)
lista.mostrar()"""