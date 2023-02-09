from historico import Historico
from dataFormatada import data,hora
from cliente import Cliente
class Conta:

    __slots__ = ['_numero', '_cliente', 'saldo', '_historico', '_limite', '_login', '_senha']
    _total_contas = 0

    def __init__(self, numero, cliente, login, senha, limite = 400):
        self._numero = numero
        self._cliente = cliente
        self.saldo = 0
        self._historico = Historico()
        self._limite = limite
        self._login = login
        self._senha = senha
        
        Conta._total_contas += 1

    @staticmethod
    def get_total_contas():
        return Conta._total_contas

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, n):
        self._numero = n

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, c):
        self._cliente = c
   

    @property
    def get_limite(self):
        return self._limite
    
    @get_limite.setter
    def set_limite(self, l):
        self._limite = l
    
    @property
    def get_historico(self):
        return self._historico

    @get_historico.setter
    def set_historico(self,s):
        return 'Erro ao adicionar, adicione usando a função adicionar do histórico'  

    @property
    def get_login(self):
        return self._login
    @get_login.setter
    def set_login(self, new_login):
        self._login = new_login
    
    @property
    def get_senha(self):
        return self._senha
    
    @get_senha.setter
    def set_senha(self, nova_senha):
        self._senha = nova_senha


    def depositar(self, valor):
        try:
            if valor > 0:
                self.saldo += valor
                self._historico.adicionar_transacao(f'Deposito no valor de {valor} R$ realizada no dia {data()} as {hora()}')

                return (True,'Deposito Realizado com Sucesso!')
            else:
                return (False, 'Saldo Invalido')
        except:
                return (False,'Ocorreu um erro inesperado!')
    def sacar(self, valor, senha):
        try:
            if valor > 0 and self._senha == senha:
                if (self.saldo + self._limite) >= valor: 
                    self.saldo -= valor
                    self._historico.adicionar_transacao(f'Saque no valor de {valor} R$ realizada no dia {data()} as {hora()}')
                    return (True, 'Saque Realizado com Sucesso!')
                else:
                    return (False, 'Saldo Insuficiente')
            else:
                return (False, 'Falha ao realizar o saque!\nsenha invalida ou valor invalido!')
        except:
            return (False, 'Ocorreu um erro inesperado')

    def transferir(self, destino, valor, senha):
        try:
            if ((self.saldo + self.get_limite) >= valor and valor > 0) and isinstance(destino, Conta) and self._senha == senha:
                self.saldo -= valor
                destino.saldo += valor
                
                self._historico.adicionar_transacao(f'Transferencia no valor de {valor} R$ para conta {destino.numero} realizada no dia {data()} as {hora()}')
                destino._historico.adicionar_transacao(f'Recebimento de Transferenia da conta {self.numero} no valor de {valor}R$ realizada no dia {data()} as {hora()}')
                return (True,'Transferencia Realizada com Sucesso!')
            else:
                return False, ('Falha ao Realizar a transferencia!\nConfira os dados informados!')
        except:
            return False, ('Ocorreu um erro inesperado')

    def extrato(self):
        print(f"Numero: {self.numero}\nTitular: {self.cliente.nome} {self.cliente.sobrenome}\nSaldo: {self.saldo}")
        self._historico.transacoes.append(f"Tirou extrato - saldo de {self.saldo} R$")

    def __str__(self) -> str:
        return f'Número da conta: {self._numero}\n\
Cliente: {self._cliente.nome} {self._cliente.sobrenome}\n\
CPF: {self._cliente.cpf}\n\
Saldo: {self.saldo}\n'

if __name__ == '__main__':
    cli = Cliente('Mauricio', 'Benjamin', '083')
    c = Conta('1', cli, '083', '083')

    retorno = c.depositar(50)
    if retorno[0]:
        print(retorno[1])
    else:
        print(retorno[1])