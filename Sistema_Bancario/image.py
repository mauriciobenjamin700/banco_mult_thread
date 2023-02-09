from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit
from PyQt5 import QtGui

class Tela_Login(QMainWindow):
    def __init__ (self):
        super().__init__()
        
        self.esquerda = 0
        self.topo = 0
        self.largura = 1460
        self.altura = 800
        self.titulo = "TELA DE LOGIN"
####################################### LABEL #######################
        self.label1 = QLabel(self)
        self.label1.setText("FAÇA O LOGIN")
        self.label1.move(540, 0)
        self.label1.resize(400,200)
        self.label1.setStyleSheet("QLabel {font: 40px}")

        self.label_login = QLabel(self)
        self.label_login.setText("Login")
        self.label_login.move(400, 280)
        self.label_login.resize(200,60)
        self.label_login.setStyleSheet("QLabel {font: 40px}")

        self.label_senha = QLabel(self)
        self.label_senha.setText("Senha")
        self.label_senha.move(400, 386)
        self.label_senha.resize(200,60)
        self.label_senha.setStyleSheet("QLabel {font: 40px}")

        
############################################### LINE EDIT ####################
        self.LineEdit_login = QLineEdit(self)
        self.LineEdit_login.move(700, 300)
        self.LineEdit_login.resize(300,40)
        self.LineEdit_login.setStyleSheet("QLineEdit {font: 20px; color: blue}")
        self.LineEdit_login.setPlaceholderText("Digite seu login aqui!")


        self.LineEdit_senha = QLineEdit(self)
        self.LineEdit_senha.move(700, 400)
        self.LineEdit_senha.resize(300,40)
        self.LineEdit_senha.setStyleSheet("QLineEdit {font: 20px; color: blue}")
        self.LineEdit_senha.setPlaceholderText("Digite sua senha aqui!")
        self.LineEdit_senha.setEchoMode(QLineEdit.Password)

############################################### QPushButton ##################

        self.botao_login = QPushButton('Fazer Login',self)
        self.botao_login.move(470, 600)
        self.botao_login.resize(400,60)
        self.botao_login.setStyleSheet('QPushButton {font: 30px; background-color: green}')

        self.botao_voltar = QPushButton("Voltar", self)
        self.botao_voltar.move(1150, 30)
        self.botao_voltar.resize(100,40)

        self.Carregar_Janela()



    def Carregar_Janela (self):

        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        
        self.setWindowTitle(self.titulo)
        
        self.show()

if __name__ == '__main__':
    import sys
    aplicacao =  QApplication(sys.argv)
    j = Tela_Login()
    sys.exit(aplicacao.exec_())