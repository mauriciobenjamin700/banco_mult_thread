from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit

class Tela_Deposito(QMainWindow):
    """
    uma classe para representar uma tela de deposito
    
    ...

    Attributes
    ----------
    esquerda: int
        define a posição da "tela deposito" no lado esquerdo da tela de visualização 
    topo: int
        define a posição da "tela deposito" no topo da tela de vizualisação
    largura: int
        define a largura da "tela deposito" na tela de visualização
    altura: int
        define a altura da "tela deposito" na tela de visualização.
    titulo: str
        define o titulo da "tela deposito" na tela de visualização.

    label1: object
        rotula algum lugar da tela onde você define um texto, movimenta a posição, redimensiona o tamanho da label e adiciona o tamanho da fonte.
    label_deposito: object
        rotula algum lugar da tela onde você define um texto, movimenta a posição desse texto, redimensiona o tamanho da label e adiciona o tamanho da fonte.

    LineEdit_deposito: object
        É uma caixa de texto onde o usuario pode adicionar o valor que irá depositar.

    botao_deposito: object
                Um botão que é usado para realizar uma determinada ação que é a de depositar, na criação desse botão ele pode ser nomeado, movimentado 
                a sua posição e redimensionado de tamanho.
    botao2: object
                Um botão que é usado para realizar uma determinada ação que é a de voltar para a tela anterior, na criação desse botão ele pode ser nomeado, movimentado 
                a sua posição e redimensionado de tamanho.

    Methods
    -------
    Carregar_Janela ():
        Gera a janela deposito
    
    """
    def __init__ (self):
        super().__init__()
        
        self.esquerda = 0
        self.topo = 0
        self.largura = 1460
        self.altura = 800
        self.titulo = "TELA DE DEPOSITO"

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


        self.LineEdit_deposito = QLineEdit(self)
        self.LineEdit_deposito.move(700, 400)
        self.LineEdit_deposito.resize(300,40)
        self.LineEdit_deposito.setStyleSheet("QLineEdit {font: 20px}")



        self.botao_deposito = QPushButton('Confirmar Deposito',self)
        self.botao_deposito.move(470, 600)
        self.botao_deposito.resize(400,60)
        self.botao_deposito.setStyleSheet('QPushButton {font:30px; background-color: green}')

        self.botao_voltar = QPushButton("Voltar", self)
        self.botao_voltar.move(1150, 30)
        self.botao_voltar.resize(100,40)

        self.Carregar_Janela()



    def Carregar_Janela (self):
        """
        A função "Carrega_Janela" cria uma janela na tela de acordo com os dados adicionado nos atributos
        esquerdo, topo, largura, altura e titulo

        parameters:
                None
        
        return:
                None

        """

        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        
        self.setWindowTitle(self.titulo)
        
        self.show()
"""
if __name__ == '__main__':
 
    Em caso de teste utilizasse o " if __name__ == '__main__' "
    
    import sys
    aplicacao =  QApplication(sys.argv)
    j = Tela_Deposito()
    sys.exit(aplicacao.exec_())
"""