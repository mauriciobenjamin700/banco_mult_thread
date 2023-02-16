from tela_inicial import Tela_Inicial
from tela_cadastro import Tela_Cadastro
from tela_login import Tela_Login
from tela_geral import Tela_Geral
from tela_deposito import Tela_Deposito
from tela_saque import Tela_Saque
from tela_transferencia import Tela_Transferencia
from tela_historico import Tela_historico
from PyQt5.QtWidgets import QApplication, QMessageBox
import hashlib
import socket


class main():
    """
    Classe que gerencia todas as telas necessárias para a aplicação

    ...

    Attributes
    ---------
    tela_inicial : class
        tela inicial
    tela_cadastro : class
        tela cadastro
    tela_login : class
        tela login
    tela_geral : class
        tela geral
    tela_deposito : class
        tela de deposito
    tela_saque : class
        tela de saque
    tela_transferencia : class
        tela de transferencia
    tela_historico : class
        tela de histórico
    cliente_socket : object
        socket do cliente
    login_atual : str
        número da conta do cliente

    Methods
    -------
    tela_0():
        abre a tela e fecha as demais
    tela_1():
        abre a tela e fecha as demais
    tela_2():
        abre a tela e fecha as demais
    tela_3():
        abre a tela e fecha as demais
    tela_4():
        abre a tela e fecha as demais
    tela_5():
        abre a tela e fecha as demais
    tela_6():
        abre a tela e fecha as demais
    tela_7():
        abre a tela e fecha as demais
    sair():
        fecha a conexão do cliente
    fuc_cadastro():
        manda os dados do cadastro para o servidor 
    func_login():
        manda os dados de login para o servidor
    func_depositar():
        manda os dados de deposito para o servidor
    func_sacar():
        manda os dados de saque para o servidor
    func_transferencia():
        manda os dados de transferencia para o servidor
    

    """
    def __init__(self):
   
        self.tela_inicial = Tela_Inicial()   

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.close()
        self.tela_login = Tela_Login()
        self.tela_login.close()
        self.tela_geral = Tela_Geral()
        self.tela_geral.close()
        self.tela_deposito = Tela_Deposito()
        self.tela_deposito.close()
        self.tela_saque = Tela_Saque()
        self.tela_saque.close()
        self.tela_transferencia = Tela_Transferencia()
        self.tela_transferencia.close()
        self.tela_historico = Tela_historico()
        self.tela_historico.close()



        ip = 'localhost'
        port = 9002

        addr = ((ip, port))
        self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente_socket.connect(addr)

        self.login_atual = ''

        #tela inicial
        self.tela_inicial.botao_cadastro.clicked.connect(self.tela_1)
        self.tela_inicial.botao_login.clicked.connect(self.tela_2)
        self.tela_inicial.botao_sair.clicked.connect(self.botao_sair)


    def tela_0(self):
        """
        Realiza o ato de abrir a tela inicial e fechar as demais telas que não estão sendo usadas.

        parameters:
            None

        return: 
           None
        """
        self.tela_cadastro.close()
        self.tela_login.close()
        self.tela_geral.close()
        self.tela_inicial.show()


    def tela_1(self):
        """
        Realiza o ato de abrir a tela de cadastro e fechar as demais telas que não estão sendo usadas.

        parameters:
            None

        return: 
           None
        """
        self.tela_cadastro.show()
        self.tela_inicial.hide()
        
        self.tela_cadastro.botao1.clicked.connect(self.func_cadastro)
        self.tela_cadastro.botao2.clicked.connect(self.tela_0)
    
    def tela_2(self):
        """
        Realiza o ato de abrir a tela de login e fechar as demais telas que não estão sendo usadas.

        parameters:
            None

        return: 
           None
        """
        self.tela_login.show()
        self.tela_inicial.close()

        self.tela_login.botao_login.clicked.connect(self.func_login)
        self.tela_login.botao_voltar.clicked.connect(self.tela_0)
    
    
    def tela_3(self):
        """
        Realiza o ato de abrir a tela geral e fechar as demais telas que não estão sendo usadas.

        parameters:
            None

        return: 
           None
        """
        self.tela_geral.show()
        self.tela_login.close()
        self.tela_deposito.close()
        self.tela_saque.close()
        self.tela_transferencia.close()
        self.tela_historico.close()
  
        self.tela_deposito.LineEdit_deposito.setText('')
        
        self.tela_saque.LineEdit_sacar.setText('')
        self.tela_saque.LineEdit_senha.setText('')
    
        self.tela_transferencia.LineEdit_sacar.setText('')
        self.tela_transferencia.LineEdit_senha.setText('')
        self.tela_transferencia.LineEdit_login_recebedor.setText('')


        self.cliente_socket.send(f'3,{self.login_atual}'.encode())
        retorno = self.cliente_socket.recv(1024).decode()
        conta = retorno.split(',')

        self.cliente_socket.send(f'-2,{conta[2]}'.encode())
        nome = self.cliente_socket.recv(1024).decode()

        self.tela_geral.label_msg.setText(f'BEM VINDO(A): {nome}')
        self.tela_geral.label_saldo.setText(f'Saldo Atual: {(conta[3])} R$')
        self.tela_geral.label_limite.setText(f'Limite Atual: {(conta[4])} R$')
        self.tela_geral.label_num_conta.setText(f'CONTA DE NÚMERO {conta[1]}')

    
        self.tela_geral.botao_deposito.clicked.connect(self.tela_4)
        self.tela_geral.botao_sacar.clicked.connect(self.tela_5)
        self.tela_geral.botao_transferir.clicked.connect(self.tela_6)

        self.tela_geral.botao_historico.clicked.connect(self.tela_7)

        self.tela_geral.botao_voltar.clicked.connect(self.tela_0)
    
    def tela_4(self):
        """
        Realiza o ato de abrir a tela deposito e fechar as demais telas que não estão sendo usadas.

        parameters:
            None

        return: 
           None
        """
        self.tela_deposito.show()
        self.tela_geral.hide()

        self.tela_deposito.botao_voltar.clicked.connect(self.tela_3)
        self.tela_deposito.botao_deposito.clicked.connect(self.func_depositar)
    
    def tela_5(self):
        """
        Realiza o ato de abrir a tela de saque e fechar as demais telas que não estão sendo usadas.

        parameters:
            None

        return: 
           None
        """
        self.tela_saque.show()
        self.tela_geral.hide()

        self.tela_saque.botao_saque.clicked.connect(self.func_saque)
        self.tela_saque.botao_voltar.clicked.connect(self.tela_3)

    def tela_6(self):
        """
        Realiza o ato de abrir a tela de transferenia e fechar as demais telas que não estão sendo usadas.

        parameters:
            None

        return: 
           None
        """
        self.tela_transferencia.show()
        self.tela_geral.hide()

        self.tela_transferencia.botao_confirmar_transferencia.clicked.connect(self.func_transferencia)
        self.tela_transferencia.botao_voltar.clicked.connect(self.tela_3)
    
    def tela_7(self):
        """
        Realiza o ato de abrir a tela de histórico e fechar as demais telas que não estão sendo usadas.

        parameters:
            None

        return: 
           None
        """
        self.tela_historico.show()
        self.tela_geral.hide()

        self.cliente_socket.send(f'7,{self.login_atual}'.encode())
        retorno = self.cliente_socket.recv(1024).decode()
        lista_string = retorno.split(',')
   
        
        self.tela_historico.Historico.clear()
        for string in lista_string:

            self.tela_historico.Historico.addItem(string)

        self.tela_historico.botao_voltar.clicked.connect(self.tela_3)
    

    
    def botao_sair(self):
        """
        Realiza o ato de enviar o aviso de encerramento de conexão para o servidor e fechar as telas da aplicação.

        parameters:
            None

        return: 
           None
        """
        self.cliente_socket.send('0'.encode())
        self.tela_inicial.close()
    


 
    def func_cadastro(self):
        """
        Realiza o ato de coletar as informações necessárias para realizar o cadastro e enviar as mesmas para o servidor, receber o retorno de servidor e exibir na tela o resultado.

        parameters:
            None

        return: 
           None
        """
   
        nome = str(self.tela_cadastro.LineEdit_nome.text().upper())
        sobrenome = str(self.tela_cadastro.LineEdit_sobrenome.text().upper())
        cpf = str(self.tela_cadastro.LineEdit_CPF.text())
        login = str(self.tela_cadastro.LineEdit_login.text())
        senha = str(self.tela_cadastro.LineEdit_senha.text())

        if not(nome == '' or sobrenome == '' or cpf == '' or login == '' or senha == ''):

                
            hash_object = hashlib.md5(senha.encode())
            senha = hash_object.hexdigest()
               
            self.cliente_socket.send(f'1,{nome},{sobrenome},{cpf},{login},{senha}'.encode())
            retorno = self.cliente_socket.recv(1024).decode()

            if retorno == 'True':

    
                QMessageBox.information(None, 'Tela_Cadastro', 'Cadastro Realizado com sucesso')
                self.tela_cadastro.LineEdit_nome.setText('')
                self.tela_cadastro.LineEdit_sobrenome.setText('')
                self.tela_cadastro.LineEdit_CPF.setText('')
                self.tela_cadastro.LineEdit_login.setText('')
                self.tela_cadastro.LineEdit_senha.setText('')

                
            else:
                QMessageBox.warning(None, 'Tela_Cadastro', 'Falha ao realizar o cadastro')
    

    def func_login(self):
        """
        Realiza o ato de coletar as informações necessárias para realizar o login e enviar as mesmas para o servidor, receber o retorno de servidor e exibir na tela o resultado.

        parameters:
            None

        return: 
           None
        """
        
        
        login = self.tela_login.LineEdit_login.text()
        senha = self.tela_login.LineEdit_senha.text()

        if not (login == '' or senha == ''):

            hash_object = hashlib.md5(senha.encode())
            senha = hash_object.hexdigest()
        
            self.cliente_socket.send(f'2,{login},{senha}'.encode())
            retorno =  self.cliente_socket.recv(1024).decode()

            retorno = retorno.split(',')

            if retorno[0] == 'True':            
                   
                self.tela_login.LineEdit_login.setText('')
                self.tela_login.LineEdit_senha.setText('')

                self.login_atual = retorno[1]
                self.tela_3()

            else:
              QMessageBox.warning(None, 'Tela_Login','Login e/ou senha incorretos!')
        

    def func_depositar(self):
        """
        Realiza o ato de coletar as informações necessárias para realizar o deposito  e enviar as mesmas para o servidor, receber o retorno de servidor e exibir na tela o resultado.

        parameters:
            None

        return: 
           None
        """
    
        valor = self.tela_deposito.LineEdit_deposito.text()
        if not (valor == ''):
            try:
                valor = float(valor)
            except:
                pass

            if type(valor) == float:
                

                self.cliente_socket.send(f'4,{valor},{self.login_atual}'.encode())
                retorno = self.cliente_socket.recv(1024).decode()
                retorno = retorno.split(',')
                if retorno[0] == 'True':
                    QMessageBox.information(None, 'Tela_Deposito',retorno[1])
                    self.tela_deposito.LineEdit_deposito.setText('')
                else:
                    QMessageBox.information(None, 'Tela_Deposito',retorno[1])
            else:
                QMessageBox.warning(None, 'Tela_Deposito','Digite um valor númerico')  

             
       
    def func_saque(self):
        """
        Realiza o ato de coletar as informações necessárias para realizar o saque e enviar as mesmas para o servidor, receber o retorno de servidor e exibir na tela o resultado.

        parameters:
            None

        return: 
           None
        """

        valor = self.tela_saque.LineEdit_sacar.text()
        senha = self.tela_saque.LineEdit_senha.text()
        if not (valor == '' or senha == ''):
            try:
                valor = float(valor)
            except:
                pass

            if type(valor) == float:

                hash_object = hashlib.md5(senha.encode())
                senha = hash_object.hexdigest()

                self.cliente_socket.send(f'5,{valor},{self.login_atual},{senha}'.encode())
                retorno = self.cliente_socket.recv(1024).decode()

                retorno = retorno.split(',')
                try:
                    if retorno[0] == 'True':

                        QMessageBox.information(None, 'Tela_Saque',retorno[1])
                        self.tela_saque.LineEdit_sacar.setText('')
                        self.tela_saque.LineEdit_senha.setText('')

                    else:
                        QMessageBox.information(None, 'Tela_Saque',retorno[1])
                except:
                    pass
    def func_transferencia(self):
        """
        Realiza o ato de coletar as informações necessárias para reazar a transferencia e enviar as mesmas para o servidor, receber o retorno de servidor e exibir na tela o resultado.

        parameters:
            None

        return: 
           None
        """
        valor = self.tela_transferencia.LineEdit_sacar.text()
        senha = self.tela_transferencia.LineEdit_senha.text()
        login_recebedor = self.tela_transferencia.LineEdit_login_recebedor.text()
        if not (valor == '' or senha == '' or login_recebedor == ''):
            try:
                valor = float(valor)
            except:
                pass

            if type(valor) == float:

                hash_object = hashlib.md5(senha.encode())
                senha = hash_object.hexdigest()

                valor = str(valor)

                self.cliente_socket.send(f'6,{valor},{self.login_atual},{senha}, {login_recebedor}'.encode())
                retorno = self.cliente_socket.recv(1024).decode()

                retorno = retorno.split(',')
                try:
                    if retorno[0] == 'True':
                        QMessageBox.information(None, 'Tela_Transferencia','Operação realizada com sucesso!')
                        self.tela_transferencia.LineEdit_sacar.setText('')
                        self.tela_transferencia.LineEdit_senha.setText('')
                        self.tela_transferencia.LineEdit_login_recebedor.setText('')
                    else:
                        QMessageBox.information(None, 'Tela_Transferencia','Falha ao realizar operação')
                except:
                    pass  
            else:
                QMessageBox.information(None, 'Tela_Transferencia', 'Preencha todos os campos corretamente!')  

        


if __name__ == '__main__':
    import sys
    aplicativo = QApplication(sys.argv)
    tela = main()
    sys.exit(aplicativo.exec_())


