from PyQt5.QtWidgets import QApplication,QMainWindow, QPushButton, QLabel, QListWidget

class Tela_historico(QMainWindow):
    def __init__(self):
        super().__init__()

        self.esquerda = 0
        self.topo = 0
        self.largura = 1460
        self.altura = 800
        self.titulo = 'Histórico'

        self.label = QLabel(self)
        self.label.setText('HISTÓRICO DA CONTA ')
        self.label.resize(450,100)
        self.label.move(400,0)
        self.label.setStyleSheet('QLabel {font: 40px}')

        self.Historico = QListWidget(self)
        self.Historico.resize(600,600)
        self.Historico.move(300,80)
        #self.Historico.addItem('Olá Mundo')
        

        self.botao_voltar = QPushButton("Voltar", self)
        self.botao_voltar.move(1150, 30)
        self.botao_voltar.resize(100,40)

        self.Criar_Janela()

    def Criar_Janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

if __name__ == '__main__':
    import sys
    aplicativo = QApplication(sys.argv)
    tela = Tela_historico()
    sys.exit(aplicativo.exec_())