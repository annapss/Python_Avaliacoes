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
            print(f"O tamanho da lista é {self.size}")
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
    
lista = ListaEncadeada()
lista.criarLSEInversa()
lista.mostrar()
print()
lista.tamanho()
lista.maior()
lista.menor()
lista.media()
valor = int(input("\nDigite um valor para ser inserido no fim da lista: "))
lista.inserirFim(valor)
lista.mostrar()