from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit

class Tela_Saque(QMainWindow):
    def __init__ (self):
        super().__init__()
        
        self.esquerda = 0
        self.topo = 0
        self.largura = 1460
        self.altura = 800
        self.titulo = "TELA DE SAQUE"
####################################### LABEL #######################
        self.label1 = QLabel(self)
        self.label1.setText("FAÇA O SEU SAQUE AQUI")
        self.label1.move(350, 10)
        self.label1.resize(600,200)
        self.label1.setStyleSheet("QLabel {font: 40px}")

        self.label_saque = QLabel(self)
        self.label_saque.setText("Valor do Saque:")
        self.label_saque.move(300, 300)
        self.label_saque.resize(100,40)
        self.label_saque.setStyleSheet("QLabel {font: 40px}")

        self.label_senha = QLabel(self)
        self.label_senha.setText("Senha")
        self.label_senha.move(300, 400)
        self.label_senha.resize(150,40)
        self.label_senha.setStyleSheet("QLabel {font: 40px}")

        

        
############################################### LINE EDIT ####################
        self.LineEdit_sacar = QLineEdit(self)
        self.LineEdit_sacar.move(600, 300)
        self.LineEdit_sacar.resize(300,40)
        self.LineEdit_sacar.setStyleSheet("QLineEdit {font: 20px}")


        self.LineEdit_senha = QLineEdit(self)
        self.LineEdit_senha.move(600, 400)
        self.LineEdit_senha.resize(300,40)
        self.LineEdit_senha.setStyleSheet("QLineEdit {font: 20px}")
        self.LineEdit_senha.setEchoMode(QLineEdit.Password)

############################################### QPushButton ##################

        self.botao_saque = QPushButton('Confirmar Saque',self)
        self.botao_saque.move(400, 600)
        self.botao_saque.resize(400,60)
        self.botao_saque.setStyleSheet('QPushButton {font:30px; background-color: green}')

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
    j = Tela_Saque()
    sys.exit(aplicacao.exec_())
    