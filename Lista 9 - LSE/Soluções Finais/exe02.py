"""
class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir(self, valor):
        aux = No(valor)
        aux.prox = self.inicio
        self.inicio = aux

    def criarLSEInversa(self):
        valor = int(input('Entre com um valor: '))
        if (valor <= 0):
            return 0
        else:
            self.inserir(valor)
            self.criarLSEInversa()

    def mostrar(self):
        aux = self.inicio
        print("\nConteúdo da Lista Simplesmente Encadeada:")
        if (self.prox == None):
            print('Lista vazia')
        else:
            while(aux!= None):
                print(aux.valor, end=' ')
                aux= aux.prox
"""
class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir(self, valor):
        aux = No(valor)
        aux.prox = self.inicio
        self.inicio = aux

    def criarLSEInversa(self):
        valor = int(input('Entre com um valor: '))
        if (valor <= 0):
            return 0
        else:
            self.inserir(valor)
            self.criarLSEInversa()

    def mostrar(self, i=0, inicio=0):
        if(i == 0):
            inicio = self.inicio
        aux = inicio
        if(i == 0):
            print('\nConteúdoda Lista Simplesmente Encadeada:')
        if (aux == None and i == 0):
            print('Lista vazia')
        if (aux != None):
            print(aux.valor, end=' ')
            aux = aux.prox
            inicio = aux
            self.mostrar(i + 1, inicio)
        else:
            return 0

lista = ListaEncadeada()
lista.criarLSEInversa()
lista.mostrar()