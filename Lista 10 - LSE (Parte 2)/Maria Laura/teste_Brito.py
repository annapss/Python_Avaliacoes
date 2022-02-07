def inserirOrdenado(self, valor):
    aux = self.inicio
    if (aux==None) or (valor < aux.valor): #lista vazia ou elemento será inserido no inicio da lista
            self.inserir(valor)
    else:
        maior = self.inicio
        while (maior.valor < valor) and (maior.prox != None):
            menor = maior
            maior = maior.prox
        else:
            if(valor>maior.valor): #inserir no fim da lista
                aux = maior
                self.inserirFim(valor)
            else: #inserir no meio da lista
                menor.prox = No(valor)
                menor.prox.prox = maior


def criarLSEOrdemDigitada(self):
    valor = int(input('Entre com um valor: '))
    while(valor>=0):
        self.inserirFim(valor)
        valor = int(input('Entre com um valor: ‘))




def removerElemento(self, valor):
    aux = self.inicio
    if (self.tamanho()==0):
        print('Lista Vazia')
    else:
        if (self.tamanho() == 1): #lista só tem 1 valor
            if(valor!=aux.valor):
                print('Valor não existe na lista')
            else:
                self.inicio = self.inicio.prox
                aux.prox = None
        else:
            if (valor == aux.valor):
                self.inicio = self.inicio.prox
                aux.prox = None
            else:
                maior = self.inicio
                while (maior.valor != valor) and (maior.prox != None):
                    menor = maior
                    maior = maior.prox

                if (valor != maior.valor):
                    print('Valor não existe na lista')
                else:
                    if (maior.prox == None):  # elemento a ser retirado está no fim da LSE
                        menor.prox = None
                    else:
                        menor.prox = maior.prox
                        maior.prox = None

def criarLSEOrdenada(self):
  valor = int(input('Entre com um valor: '))
  while(valor>=0):
    self.inserirOrdenado(valor)
    valor = int(input('Entre com um valor: '))
