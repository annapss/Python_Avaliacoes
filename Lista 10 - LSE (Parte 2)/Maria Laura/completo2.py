"""
Grupo: Anna Paula Siqueira da Silva, Maria Laura Barbosa Soares, Luanda Rodrigues da Silva e Ariane Arantes dos Santos
Turma: 2BINFO
"""
class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.size = 0 #Atributo par ao tamanho

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
            print('\nConteúdo da Lista Simplesmente Encadeada:')
        if (aux == None and i == 0):
            print('Lista vazia')
        if (aux != None):
            print(aux.valor, end=' ')
            aux = aux.prox
            inicio = aux
            self.mostrar(i + 1, inicio)
        else:
            return 0

    def tamanho(self, i=0, inicio=0):
        if(i == 0):
            inicio = self.inicio
        aux = inicio
        if (aux == None):
            #print(f"O tamanho da lista é {self.size}")
            return self.size
        else:
            aux = aux.prox
            inicio = aux
            self.size += 1
            self.tamanho(i + 1, inicio)
    
    def maior(self, i = 0, inicio = 0, more = 0):
        if(i == 0):
            inicio = self.inicio
        aux = inicio
        if (aux != None):
            if(i == 0):
                more = aux.valor
            if (aux.valor > more):
                more = aux.valor
            aux = aux.prox
            inicio = aux
            self.maior(i + 1, inicio, more)
        else:
            if(i != 0):
                print(f'O maior valor é {more}')
                return more
            else:
                print("Lista vazia")
                return None
    
    def menor(self, i = 0, inicio = 0, less = 0):
        if(i == 0):
            inicio = self.inicio
        aux = inicio
        if (aux != None):
            if(i == 0):
                less = aux.valor
            if (aux.valor < less):
                less = aux.valor
            aux = aux.prox
            inicio = aux
            self.menor(i + 1, inicio, less)
        else:
            if(i != 0):
                print(f'O menor valor é {less}')
                return less
            else: 
                print("Lista vazia")
                return None

    def media(self, i = 0, inicio = 0, avg = 0):
        if(i == 0):
            inicio = self.inicio
        aux = inicio
        if (aux == None):
            if(i != 0):
                avg = avg / self.size
                print(f'A média é {avg:.2f}')
                return avg
            else:
                print("Lista vazia")
                return None
        else:
            avg += aux.valor
            aux = aux.prox
            inicio = aux
            return self.media(i + 1, inicio, avg)
    
    def fimLista(self, i = 0, inicio = 0):
            # Vai retornar o endereço do último elemento da lista
            if(i == 0):
                inicio = self.inicio
            aux = inicio
            if (aux == None and i == 0):
                return None
            else:
                if(aux.prox != None):
                    aux = aux.prox
                    inicio = aux
                    return self.fimLista(i + 1, inicio)
                else:
                    return aux

    def inserirFim(self, valor):
        aux = self.inicio
        if (aux == None):
            self.inserir(valor)
        else:
            aux = self.fimLista()
            aux.prox = No(valor)    
    def inserirOrdenado(self, valor, menor=0, i=0, inicio=0):
        if (i == 0):
            inicio = self.inicio
        aux = inicio
        if ((aux == None) or (valor < aux.valor)) and i == 0:  # lista vazia ou elemento será inserido no inicio da lista
            self.inserir(valor)
        else:
            maior = inicio
            if (maior.valor < valor) and (maior.prox != None):
                menor = maior
                maior = maior.prox
                inicio = maior
                self.inserirOrdenado(valor, menor, i + 1, inicio)
            else:
                if (valor > maior.valor):  # inserir no fim da lista
                    aux = maior
                    self.inserirFim(valor)
                else:  # inserir no meio da lista
                    menor.prox = No(valor)
                    menor.prox.prox = maior


    def criarLSEOrdenada(self):
        valor = int(input('Entre com um valor: '))
        if (valor >= 0):
            self.inserirOrdenado(valor)
            self.criarLSEOrdenada()
        else:
            return 0
    def removerElemento(self, valor, menor=0, i=0, inicio = 0):
        if (i == 0):
            self.tamanho()
            inicio = self.inicio
        aux = self.inicio
        if (self.size == 0):
            print('Lista Vazia')
        else:
            if (self.size == 1):  # lista só tem 1 valor
                if (valor != aux.valor):
                    print('Valor não existe na lista')
                else:
                    self.inicio = self.inicio.prox
                    aux.prox = None
            else:
                if (valor == aux.valor):
                    self.inicio = self.inicio.prox
                    aux.prox = None
                else:
                    maior = inicio
                    if (maior.valor != valor) and (maior.prox != None):
                        menor = maior
                        maior = maior.prox
                        inicio = maior
                        self.removerElemento(valor, menor, i + 1, inicio)
                    else:
                        if (valor != maior.valor):
                            print('Valor não existe na lista')
                        else:
                            if (maior.prox == None):  # elemento a ser retirado está no fim da LSE
                                menor.prox = None
                            else:
                                menor.prox = maior.prox
                                maior.prox = None

    def criarLSEOrdemDigitada(self):
        valor = int(input('Entre com um valor: '))
        if (valor >= 0):
            self.inserirFim(valor)
            self.criarLSEOrdemDigitada()
        else:
            return 0

    def ordenarLSE(self):

    def apagarLSE(self):
        


lista = ListaEncadeada()
lista.criarLSEOrdemDigitada()
lista.mostrar()
"""lista.inserirOrdenado(12)
lista.inserirOrdenado(9)
lista.inserirOrdenado(3)
lista.inserirOrdenado(6)
lista.inserirOrdenado(20)
lista.criarLSEOrdenada()
lista.mostrar()
lista.removerElemento(6)
lista.mostrar()
lista.removerElemento(20)
lista.mostrar()"""
#lista.inserirOrdenado(6)
#lista.mostrar()