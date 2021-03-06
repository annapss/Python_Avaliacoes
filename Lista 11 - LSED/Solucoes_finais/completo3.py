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

    def remover(self, valor):
        aux = self.inicio
        if(self.quant == 0):
            print("Lista vazia")
        else:
            if(self.quant == 1):
                if(valor != aux.valor):
                    print("Esse valor não está na lista")
                else:
                    self.inicio = None
                    self.fim = None
                    self.quant -= 1
            else:
                if(valor == aux.valor):
                    self.inicio = self.inicio.prox
                    aux.prox = None
                else:
                    maior = self.inicio
                    while((maior.valor != valor) and (maior.prox != None)):
                        menor = maior
                        maior = maior.prox
                    if(valor != maior.valor):
                        print("Esse valor não está na lista")
                    else:
                        if(maior.prox == None):
                            menor.prox = None
                            self.fim = menor
                        else:
                            menor.prox = maior.prox
                            maior.prox = None
                        self.quant -= 1
    
    def apagarLSED(self):
        aux = self.inicio
        while(aux != None):
            valor = aux.valor
            aux = aux.prox
            self.remover(valor)
            self.quant -= 1


lista = ListaDuplaDescritor()
lista.CriarOrdemDigitada()
lista.mostrar()
print()
lista.apagarLSED()
lista.mostrar()
lista.CriarInversa()
lista.mostrar()
print()
lista.apagarLSED()
lista.mostrar()
lista.CriarCrescente()
lista.mostrar()