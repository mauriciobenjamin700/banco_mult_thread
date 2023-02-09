'''
                        precisa conter:
painel de saldo
botao para transferencia
bota para saque
botao para deposito
botao para historico
botao para extrato

'''
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class Tela_Geral(QMainWindow):
    def __init__(self):
        super().__init__()

        self.esquerda = 0
        self.topo = 0
        self.largura = 1460
        self.altura = 800
        self.titulo = 'Tela Geral'
#######################################$ titulo e saldo ###########################
        self.label_msg = QLabel(self)
        self.label_msg.setText('BEM VINDO(A)  ')
        self.label_msg.resize(600,100)
        self.label_msg.move(480,0)
        self.label_msg.setStyleSheet('QLabel {font: 40px}')

        self.label_saldo = QLabel(self)
        self.label_saldo.setText('SALDO: ')
        self.label_saldo.resize(600,200)
        self.label_saldo.move(250,100)
        self.label_saldo.setStyleSheet('QLabel {font: 40px}')

        self.label_limite = QLabel(self)
        self.label_limite.setText('LIMITE: ')
        self.label_limite.resize(600,200)
        self.label_limite.move(850,100)
        self.label_limite.setStyleSheet('QLabel {font: 40px}')

        self.label_num_conta = QLabel(self)
        self.label_num_conta.setText('CONTA DE NÚMERO: ')
        self.label_num_conta.resize(600,200)
        self.label_num_conta.move(350,580)
        self.label_num_conta.setStyleSheet('QLabel {font: 40px; color: blue}')
########################################### Fileira de cima
        self.botao_deposito = QPushButton('Depositar', self)
        self.botao_deposito.resize(200,40)
        self.botao_deposito.move(530,250)
        self.botao_deposito.setStyleSheet('QPushButton {font:30px}')

        self.botao_sacar = QPushButton('Sacar', self)
        self.botao_sacar.resize(200,40)
        self.botao_sacar.move(530,350)
        self.botao_sacar.setStyleSheet('QPushButton {font:30px}')

        self.botao_transferir = QPushButton('Transferir', self)
        self.botao_transferir.resize(200,40)
        self.botao_transferir.move(530,450)
        self.botao_transferir.setStyleSheet('QPushButton {font:30px}')

        self.botao_historico = QPushButton('Extrato', self)
        self.botao_historico.resize(200,40)
        self.botao_historico.move(530,550)
        self.botao_historico.setStyleSheet('QPushButton {font:30px}')

        
##################################### sair ########################################
        self.botao_voltar = QPushButton("Voltar", self)
        self.botao_voltar.move(1150, 30)
        self.botao_voltar.resize(100,40)

        self.Criar_Tela()

    def Criar_Tela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

if __name__ == '__main__':
    import sys
    aplicativo = QApplication(sys.argv)
    tela = Tela_Geral()
    sys.exit(aplicativo.exec_())