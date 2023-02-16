from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class Tela_Inicial(QMainWindow):
    def __init__(self):
        """
        uma classe para representar uma tela inicial
        
        ...

        Attributes:
        --------
        esquerda: int
                define a posição da "tela geral" no lado esquerdo da tela de visualização 
        topo: int
                define a posição da "tela geral" no topo da tela de vizualisação
        largura: int
                define a largura da "tela geral" na tela de visualização
        altura: int
                define a altura da "tela geral" na tela de visualização.
        titulo: str
                define o titulo da "tela geral" na tela de visualização.
        """
        super().__init__()
        
        self.esquerda = 0
        self.topo = 0
        self.largura = 1460
        self.altura = 800
        self.titulo = 'TELA INICIAL'

        #########################################################################
        '''
        
        Attributes:
        --------
        label1: object
            rotula algum lugar da tela onde você define um texto, movimenta a posição, redimensiona o tamanho da label e adiciona o tamanho da fonte.
        '''
        self.label1 = QLabel(self)
        self.label1.setText("REALIZE SEU CADASTRO OU SEU LOGIN")
        self.label1.move(320,0)
        self.label1.resize(1000,100)
        self.label1.setStyleSheet("QLabel {font: 40px}")

#################################################################################
        '''
        
        Attributes:
        --------
        botao_cadastro: object
            Um botão que é usado para realizar uma determinada ação que é a de ir para a tela de realizar um cadastro, na criação desse botão ele pode ser nomeado, movimentado 
            a sua posição e redimensionado de tamanho.
        botao_login: object
            Um botão que é usado para realizar uma determinada ação que é a de ir para a tela de realizar um login na conta, na criação desse botão ele pode ser nomeado, movimentado 
            a sua posição e redimensionado de tamanho.
        botao_sair: object
            Um botão que é usado para realizar uma determinada ação que é a de sair da tela inicial e fechar o programa, na criação desse botão ele pode ser nomeado, movimentado 
            a sua posição e redimensionado de tamanho.
        '''
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
        '''
        A função "Criar_Janela" cria uma janela na tela de acordo com os dados adicionado nos atributos
        esquerdo, topo, largura, altura e titulo
        '''
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()


if __name__ == '__main__':
    """
    Em caso de teste utilizasse o " if __name__ == '__main__' "
    """
    import sys
    aplicativo = QApplication(sys.argv)
    tela = Tela_Inicial()
    sys.exit(aplicativo.exec_())