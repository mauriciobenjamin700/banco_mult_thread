from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit

class Tela_Deposito(QMainWindow):
    def __init__ (self):
        super().__init__()
        
        self.esquerda = 0
        self.topo = 0
        self.largura = 1460
        self.altura = 800
        self.titulo = "TELA DE DEPOSITO"
####################################### LABEL #######################
        self.label1 = QLabel(self)
        self.label1.setText("FAÇA O SEU DEPOSITO AQUI")
        self.label1.move(450, 10)
        self.label1.resize(600,200)
        self.label1.setStyleSheet("QLabel {font: 40px}")

        self.label_deposito = QLabel(self)
        self.label_deposito.setText("Valor do Deposito")
        self.label_deposito.move(400, 400)
        self.label_deposito.resize(100,40)
        self.label_deposito.setStyleSheet("QLabel {font: 40px}")

        

        
############################################### LINE EDIT ####################
        self.LineEdit_deposito = QLineEdit(self)
        self.LineEdit_deposito.move(700, 400)
        self.LineEdit_deposito.resize(300,40)
        self.LineEdit_deposito.setStyleSheet("QLineEdit {font: 20px}")



############################################### QPushButton ##################

        self.botao_deposito = QPushButton('Confirmar Deposito',self)
        self.botao_deposito.move(470, 600)
        self.botao_deposito.resize(400,60)
        self.botao_deposito.setStyleSheet('QPushButton {font:30px; background-color: green}')

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
    j = Tela_Deposito()
    sys.exit(aplicacao.exec_())
    