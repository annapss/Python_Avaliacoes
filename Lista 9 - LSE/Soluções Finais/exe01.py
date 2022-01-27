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
        while(valor >= 0):
            if (valor <= 0):
                return 0
            else:
                self.inserir(valor)
                valor = int(input('Entre com um valor: '))
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

lista = ListaEncadeada()
lista.criarLSEInversa()