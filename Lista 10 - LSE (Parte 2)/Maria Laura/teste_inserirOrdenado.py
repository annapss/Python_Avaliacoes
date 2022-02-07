    def inserirOrdenado(self, valor, i=0, inicio=0):
        if (i == 0):
            inicio = self.inicio
        aux = inicio
        if (aux == None) or (valor < aux.valor):  # lista vazia ou elemento será inserido no inicio da lista
            self.inserir(valor)
        else:
            maior = inicio
            if (maior.valor < valor) and (maior.prox != None):
                menor = maior
                maior = maior.prox
                inicio = maior
                self.inserirOrdenado(valor, i + 1, inicio)
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
