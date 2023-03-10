from PyQt5.QtWidgets import QApplication,QMainWindow, QPushButton, QLabel, QListWidget

class Tela_historico(QMainWindow):
    """
    uma classe para representar uma tela historico
        
    ...

    Attributes
    ---------
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

    label: object
        rotula algum lugar da tela onde você define um texto, movimenta a posição, redimensiona o tamanho da label e adiciona o tamanho da fonte.

    Historico: object
        é uma classe de conveniência que fornece uma visualização de lista com uma interface clássica baseada em itens para adicionar e remover itens,
        onde nela é mostrada todo histórico de uma conta desde a sua criação, saque, deposito e transferência.

    botao_voltar: object
        Um botão que é usado para realizar uma determinada ação que é a de voltar para a tela anterior, na criação desse botão ele pode ser nomeado, movimentado 
        a sua posição e redimensionado de tamanho.

    Methods
    -------
    Carregar_Janela ():
        Gera a janela Histórico
        """        
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
#########################################################################################

        self.Historico = QListWidget(self)
        self.Historico.resize(600,600)
        self.Historico.move(300,80)
        
        self.botao_voltar = QPushButton("Voltar", self)
        self.botao_voltar.move(1150, 30)
        self.botao_voltar.resize(100,40)

        self.Criar_Janela()

    def Criar_Janela(self):
        '''
        A função "Criar_Janela" cria uma janela na tela de acordo com os dados adicionado nos atributos
        esquerdo, topo, largura, altura e titulo

        parameters:
                None

        return:
                None
        '''
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
"""
if __name__ == '__main__':
    
    Em caso de teste utilizasse o " if __name__ == '__main__' "
    
    import sys
    aplicativo = QApplication(sys.argv)
    tela = Tela_historico()
    sys.exit(aplicativo.exec_())
"""