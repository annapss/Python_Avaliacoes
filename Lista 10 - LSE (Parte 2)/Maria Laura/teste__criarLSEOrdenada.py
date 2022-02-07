    def criarLSEOrdenada(self):
        valor = int(input('Entre com um valor: '))
        if (valor >= 0):
            self.inserirOrdenado(valor)
            self.criarLSEOrdenada()
        else:
            return 0
    
