from conta import Conta
class Banco():
    
    __slots__ = ['_contas']

    def __init__(self) -> None:
        self._contas = {}


    def adicionar_conta(self, conta, login):
        try:
            if login not in self._contas.keys():
                if isinstance(conta, Conta):
                    self._contas[login] = conta
                    return (True,'Cadastro Realizado com sucesso!')
                else:
                    return (False, 'Falha ao realizar o cadastro!')
            else:
                return (False, 'Já existe uma conta associada a este login')
       
        except:
            return (False, 'Erro 404')

    def buscar_conta(self, login):
        try:
            if login in self._contas.keys():
                return (True,self._contas[login])
            else:
                return (False, None)
        except:
            return (False, None)

    def mostrar_conta(self, login):
        try:
            if login in self._contas.keys():
                return (self._contas[login].__str__())
        except:
            return False

  
    def remover_conta(self, login, senha):
        try:
            if login in self._contas.keys():
                if self._contas[login].get_senha == senha:
                    del self._contas[login]
                    return True
                else:
                    return False
            else:
                return False

        except:
            return False

