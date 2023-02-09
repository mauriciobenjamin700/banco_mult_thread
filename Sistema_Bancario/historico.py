from dataFormatada import data, hora
class Historico():

    __slots__ = ['data_abertura', 'transacoes']
    
    def __init__(self):

        self.data_abertura = (data(),hora())
        self.transacoes = []
        

    def adicionar_transacao(self, t):
        try:
            self.transacoes.append(t)
            return True
        except:
            return False

    def imprimir(self):
        return (self.data_abertura, self.transacoes)
        
    def dados_transacoes(self):
        return self.transacoes