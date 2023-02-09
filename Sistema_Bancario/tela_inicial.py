from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class Tela_Inicial(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.esquerda = 0
        self.topo = 0
        self.largura = 1460
        self.altura = 800
        self.titulo = 'TELA INICIAL'

        ###################################### BOTÕES ###################################
        self.label1 = QLabel(self)
        self.label1.setText("REALIZE SEU CADASTRO OU SEU LOGIN")
        self.label1.move(320,0)
        self.label1.resize(1000,100)
        self.label1.setStyleSheet("QLabel {font: 40px}")

        self.botao_cadastro = QPushButton('Cadastro',self)
        self.botao_cadastro.resize(320,170)
        self.botao_cadastro.move(500,200)
        self.botao_cadastro.setStyleSheet('QPushButton {font: 60px}')

        self.botao_login = QPushButton('Login',self)
        self.botao_login.resize(320,170)
        self.botao_login.move(500,440)
        self.botao_login.setStyleSheet('QPushButton {font: 60px}')

        self.botao_sair = QPushButton('Sair',self)
        self.botao_sair.resize(100,40)
        self.botao_sair.move(1150,20)
        self.botao_sair.setStyleSheet('QPushButton {font: 40px;}')


        self.Criar_Janela()

    def Criar_Janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()


if __name__ == '__main__':
    import sys
    aplicativo = QApplication(sys.argv)
    tela = Tela_Inicial()
    sys.exit(aplicativo.exec_())