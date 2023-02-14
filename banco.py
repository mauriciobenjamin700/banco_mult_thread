import mysql.connector
from random import randint
from datetime import datetime
#import hashlib

def data():
    """
    retorna a data e hora atual em formato de string
    """
    data = str(datetime.now())

    ano = data[0:4]
    mes = data[5:7]
    dia = data[8:10]


    data_formatada = f'{dia}/{mes}/{ano}'


    hora = data[11:16]
    
    return f'{data_formatada} as {hora}'

class Banco():

    """
    classe banco que possui uma conexão ao banco de dados, onde a mesma pode acessar e alterar os dados do mesmo.
    """

    def __init__(self) -> None:
        """
        construtor que cria dois atributos referentes ao banco de dados

        self.conexão : mysql object
            conexão entre a classe banco com o banco de dados escolhido, onde a mesma precisa dos parametros de acesso e conexão com o respectivo banco
        
        self.cursor : mysql object
            cursor mysql que permite executar comandos no banco de dados, será usado sempre que for necessário solicitar algo ao banco de dados

        """
        self.conexao = mysql.connector.connect(host='localhost',user='root',password='',database='banco_python')
        self.cursor = self.conexao.cursor()

    def buscar_cliente(self, cpf):
        """
        Realiza uma busca no banco de dados para saber se existe um cliente com cpf passado.
        caso exista retorna uma tupla onde o primeiro elemento é um boleano referente ao resultado da operação, os demais elementos da tupla são os dados do cliente
        caso não exista o cliente buscado, retorna False e uma string de aviso.

            parametros:
                cpf {string} : cpf do cliente que se deseja buscar

            retorno:
            Tuple : tupla com o resultado da busca pelo cliente
        """
        comando = (f'SELECT * FROM cliente where cpf = {cpf}')

        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        if resultado != []:
            return (True,resultado[0][0], resultado[0][1], resultado[0][2], resultado[0][3])
        else:
            return (False, 'Cliente não encontrado')

    def buscar_conta(self, numero):
        """
        Realiza uma busca no banco de dados para saber se existe uma conta referente ao número passado passado.
        caso exista retorna uma tupla onde o primeiro elemento é um boleano referente ao resultado da operação, os demais elementos da tupla são os dados da conta
        caso não exista a conta buscada, retorna False e uma string de aviso.

            parametros:
                numero {string} : numero da conta que se deseja buscar

            retorno:
            Tuple : tupla com o resultado da busca pela conta
        """
        comando = (f'SELECT * FROM conta where numero = {numero}')

        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        #print(resultado)
        if resultado != []:
            #retorno caso possuir conta
            return (True, resultado[0][0], resultado[0][1], resultado[0][2],resultado[0][3],resultado[0][4], resultado[0][5])
        else:
            #retorno caso não possuir conta
            return (False, 'Conta não encontrada')
    
    def cadastrar_cliente(self,cpf,nome,sobrenome):
        """
        Realiza o cadastro do cliente no banco de dados e retorna True caso o mesmo não possua um cadastro, caso o cliente já possuir cadastro retorna False e não cadastra

            Parametros:
                cpf {string} : cpf do cliente em formato string
                nome {string} : nome do cliente em formato string
                sobrenome {string} : sobrenome do cliente em formato string
            
            Retorno: 
                Boleano referente ao resultado da operação
        """
        busca = self.buscar_cliente(cpf)
        #testar se o cliente já possui conta
        if busca[0]:
            #se ja possuir, retorna false e não cadastra o cliente
            return False
        else:
            comando = 'INSERT INTO cliente (cpf, nome, sobrenome) values (%s,%s,%s)'
            self.cursor.execute(comando,(cpf,nome,sobrenome))
            return True
    
    def criar_conta(self, cliente_cpf, login,senha):
        """
        Realiza o cadastro de uma no banco de dados e retorna True caso a mesmo não exista, caso a conta já exista retorna False e não cadastra

            Parametros:
                cliente_cpf {string} : cpf do cliente em formato string
                login {string} : login do cliente em formato string
                senha {string} : hash da senha do cliente em formato string
            
            Retorno: 
                Boleano referente ao resultado da operação
        """
        

        busca = self.buscar_cliente(cliente_cpf)
        if busca[0] == True:
            if busca[4] == None:
                numero = randint(0,1000000000)
                numero_existente = self.buscar_conta(numero)
                while numero_existente[0] == True:
                    numero = randint(0,1000000000)
                    numero_existente = self.buscar_conta(numero)
                
                comando = 'INSERT INTO conta (numero, cliente_cpf, login, senha) values (%s,%s,%s,%s)'
                self.cursor.execute(comando,(numero,cliente_cpf, login, senha))
                comando = 'UPDATE cliente SET conta_num = %s where cpf = %s'

                self.cursor.execute(comando,(numero, cliente_cpf))

                comando = comando = 'INSERT INTO historico (transacao, historico_num_conta, data_transacao) values (%s,%s,%s)'
                self.cursor.execute(comando,(f'Data de abertura da conta: ', numero,data()))
                return True
            else:
                return False
        else:
            return False


########################################################## CADASTRO E BUSCA DE CONTAS/CLIENTES ##############################
########################################################### OPERAÇÕES BANCÁRIOS E HISTÓRICO #################################
    def depositar(self, valor, num_conta):
        """
        Realiza o ato de "depositar" do banco, onde recebe um valor e um número de conta e esse valor sera creditado na conta.

            parâmetros:
                valor {string} : valor a ser depositado em formato de string
                num_conta {string} : número da conta em string onde será créditado o depósito 
            Retorno: 
                Boleano referente ao resultado da operação e uma string justificado o motivo do boleano
        """
        valor = float(valor)
        if valor > 0:
            comando = f'SELECT saldo FROM conta WHERE numero = {num_conta}'
            self.cursor.execute(comando)
            #fetchone faz uma tupla contendo um unico valor na posição zero
            #ao usar o [0] é possivel anular a tupla e ter um valor normal, nesse caso um float
            saldo_atual = self.cursor.fetchone()[0]
            saldo_atual += valor

            comando = f'UPDATE conta SET saldo = {saldo_atual} WHERE numero = {num_conta}'
            self.cursor.execute(comando)    

            comando = 'INSERT INTO historico (transacao, historico_num_conta, data_transacao) values (%s,%s,%s)'
            self.cursor.execute(comando,(f'Deposito realizado no valor de {valor} R$', num_conta,data()))
            return (True, 'Deposito Realizado com sucesso!')  
        else:
            return (False, 'Falha ao realizar o deposito, valor invalido!')

    def sacar(self, valor, num_conta, senha):
        """
        Realiza o ato de "sacar" do banco, onde recebe um valor e um número de conta e esse valor sera retirado da conta.

            parâmetros:
                valor {string} : valor a ser depositado em formato de string
                num_conta {string} : número da conta em string onde será retirado o valor para saque
                senha {string} : hash da senha em formato de string para garatir uma segurança da conta durante a operação 
            Retorno: 
                Boleano referente ao resultado da operação e uma string justificado o motivo do boleano
        """

        valor = float(valor)


        if valor > 0:
            comando = f'SELECT saldo, limite, senha FROM conta WHERE numero = {num_conta}'
            self.cursor.execute(comando)
            #fetchone faz uma tupla contendo um unico valor na posição zero
            #ao usar o [0] é possivel anular a tupla e ter um valor normal, nesse caso um float
            retorno = self.cursor.fetchone()
            saldo_conta = retorno[0]
            limite_conta = retorno[1]
            senha_conta = retorno[2]
            
            if senha == senha_conta :
                if valor <= (saldo_conta + limite_conta):

                    saldo_conta -= valor

                    comando = f'UPDATE conta SET saldo = {saldo_conta} WHERE numero = {num_conta}'
                    self.cursor.execute(comando)
                    comando = 'INSERT INTO historico (transacao, historico_num_conta, data_transacao) values (%s,%s,%s)'
                    self.cursor.execute(comando,(f'Saque realizado no valor de {valor} R$', num_conta,data()))

                    return (True, 'Operação Realizada com Sucesso')  
                else:
                    return (False, 'Saldo Insuficiente')
            else:
                return (False, 'Senha incorreta')
        
            
        else:
            return (False, 'Valor Invalido')



    def transferir(self, valor,num_conta, senha, num_conta_destino):
        """
        Realiza o ato de "transferir" do banco, onde recebe um valor e um número de conta, onde essa conta tera seu saldo subtraido pelo valor passado e esse mesmo valor será creditado na conta destino que foi passada.

        parâmetros:
            valor {string} : valor a ser depositado em formato de string
            num_conta {string} : número da conta em string onde será retirado o valor para transferencia
            senha {string} : hash da senha em formato de string para garatir uma segurança da conta durante a operação
            num_conta_destino {string} : número da conta que será creditado o valor transferido pela conta do usuário 
        Retorno: 
                Boleano referente ao resultado da operação e uma string justificado o motivo do boleano
        """


        valor = float(valor)
        if valor > 0:
            comando = f'SELECT saldo, limite, senha FROM conta WHERE numero = {num_conta}'
            self.cursor.execute(comando)
            #fetchone faz uma tupla contendo um unico valor na posição zero
            #ao usar o [0] é possivel anular a tupla e ter um valor normal, nesse caso um float
            retorno = self.cursor.fetchone()
            saldo_conta = retorno[0]
            limite_conta = retorno[1]
            senha_conta = retorno[2]

            destino = self.buscar_conta(num_conta_destino)
            
            if senha == senha_conta and destino[0]:
                if valor <= (saldo_conta + limite_conta):

                    saldo_conta -= valor
                    
                    #atualizando conta primaria
                    comando = f'UPDATE conta SET saldo = {saldo_conta} WHERE numero = {num_conta}'
                    self.cursor.execute(comando)
                    comando = 'INSERT INTO historico (transacao, historico_num_conta, data_transacao) values (%s,%s,%s)'
                    self.cursor.execute(comando,(f'Transferencia realizada no valor de {valor} R$ para conta {num_conta_destino}', num_conta,data()))

                    #atualizando conta destino
                    comando = f'UPDATE conta SET saldo = {destino[3]+valor} WHERE numero = {num_conta_destino}'
                    self.cursor.execute(comando)
                    comando = 'INSERT INTO historico (transacao, historico_num_conta, data_transacao) values (%s,%s,%s)'
                    self.cursor.execute(comando,(f'Transferencia recebida no valor de {valor} R$ da conta {num_conta}', num_conta_destino,data()))

                    return (True, 'Operação Realizada com Sucesso')  
                else:
                    return (False, 'Saldo Insuficiente')
            else:
                return (False, 'Senha incorreta e/ou conta destino invalida!')
        
            
        else:
            return (False, 'Valor Invalido')



    def historico(self, num_conta):
        """
        Realiza o ato de "buscar histórico" do banco, onde recebe um número de conta, busca todas as transações referentes a conta e retorna as mesmas.

        parâmetros:
            num_conta {string} : número da conta em string onde será retirado o valor para saque

        Retorno: 
           uma lista de tuplas, onde cada tupla é uma transação
        """
        comando = f'SELECT transacao, data_transacao FROM historico WHERE historico_num_conta = {num_conta}'
        self.cursor.execute(comando)
        retorno = self.cursor.fetchall()
        if retorno == []:
            return None
        else:
            return retorno

    def logar(self, login, senha):

        #hash_object = hashlib.md5(senha.encode())
        #senha = hash_object.hexdigest()

        comando = 'SELECT * FROM conta;'
        self.cursor.execute(comando)
        contas = self.cursor.fetchall()
        conta_correta = ''
        for tupla in contas:
            if tupla[4] == login and tupla[5] == senha:
                conta_correta = tupla[0]
                break
            else:
                pass
        if conta_correta != '':
            return (True,conta_correta)
        else:
            return (False, 'Conta não Encontrada')

    def sair(self):
        self.conexao.commit()
        self.conexao.close()

if __name__ == '__main__':
    '''b = Banco()
    if b.logar('mauriciorocha70', 'mr14148099')[0]:
        print('achei')
    '''
    #b.sair()
    #print(b.buscar_cliente('001'))
    #print(b.buscar_conta('14'))


    #print(b.cadastrar_cliente('123', 'Pedro', 'Vital'))

    #print(b.criar_conta('123', 'pedro123','123'))
    #b.cancelar_conta('222', '123')
    #print(b.buscar_cliente('083'))

    #print(b.depositar(10, '403784779'))

    #b.conexao.commit()
    #b.conexao.close()

    #retorno =  b.sacar(10,'314564974', 'mr14148099')
    #if retorno[0]:
    #    print(retorno[1])
    #else:
    #    print(retorno[1])

""""    
    retorno = b.historico('403784779')
    if retorno != None:
        for tupla in retorno:
            print('\n','-'*40)
            for iten in tupla:
                print(iten, end=' ')
    else:
        print('Sem dados do historico')
"""  
"""
    retorno =  b.transferir(2, '314564974', 'mr14148099', '403784779')
    if retorno[0]:
        print(retorno[1])
    else:
        print(retorno[1])
"""
    