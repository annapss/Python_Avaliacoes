"""
Grupo: Anna Paula Siqueira da Silva, Maria Laura Barbosa Soares, Luanda Rodrigues da Silva e Ariane Arantes dos Santos
Turma: 2BINFO
Resolução 2 e 1
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
        while(valor>=0):
            self.inserir(valor)
            valor = int(input('Entre com um valor: '))

    def mostrar(self):
        aux= self.inicio
        print('\nConteúdoda Lista Simplesmente Encadeada:')
        if(aux==None):
            print('Lista Vazia!!')
        else:
            while(aux!= None):
                print(aux.valor, end=' ')
                aux= aux.prox
    
    def tamanho(self):
        aux = self.inicio
        cont = 0
        while(aux!= None):
            cont+= 1
            aux= aux.prox
        return cont

    def maior(self):
        aux= self.inicio
        if(aux!=None):
            maior = aux.valor
            while(aux!= None):
                if(aux.valor>maior):
                    maior = aux.valor
                    aux= aux.prox
                else:
                    maior = None
                return maior

    def menor(self):
        aux = self.inicio
        if (aux != None):
            menor = aux.valor
            while (aux != None):
                if (aux.valor < menor):
                    menor = aux.valor
                aux = aux.prox
        else:
            menor = None
        return menor

    def media(self):
            aux = self.inicio
            if (aux == None):
                return None
            else:
                media = 0
                while (aux != None):
                    media += aux.valor
                    aux = aux.prox
                media /= self.tamanho()
                return media
    
    def fimLista(self):
        # Vai retornar o endereço do último elemento da lista
        aux = self.inicio
        if (aux == None):
            return None
        else:
            while (aux.prox != None):
                aux = aux.prox
        return aux

    def inserirFim(self, valor):
        aux = self.inicio
        if (aux == None):
            self.inserir(valor)
        else:
            aux = self.fimLista()
            aux.prox = No(valor)

