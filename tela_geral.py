from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class Tela_Geral(QMainWindow):
    """
    uma classe para representar uma tela geral
    
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

    label_msg: object
        rotula algum lugar da tela onde você define um texto, movimenta a posição, redimensiona o tamanho da label e adiciona o tamanho da fonte.
    label_saldo: object
        rotula algum lugar da tela onde você define um texto, movimenta a posição desse texto, redimensiona o tamanho da label e adiciona o tamanho da fonte.
    label_limite: object
        rotula algum lugar da tela onde você define um texto, movimenta a posição desse texto, redimensiona o tamanho da label e adiciona o tamanho da fonte.
    label_num_conta: object
        rotula algum lugar da tela onde você define um texto, movimenta a posição desse texto, redimensiona o tamanho da label e adiciona o tamanho da fonte.

    botao_deposito: object
        Um botão que é usado para realizar uma determinada ação que é a de ir para a tela de deposito, na criação desse botão ele pode ser nomeado, movimentado 
                a sua posição e redimensionado de tamanho.
    botao_sacar: object
        Um botão que é usado para realizar uma determinada ação que é a de ir para a tela de saque, na criação desse botão ele pode ser nomeado, movimentado 
        a sua posição e redimensionado de tamanho.
    botao_transferir: object
        Um botão que é usado para realizar uma determinada ação que é a de ir para a tela de transferência, na criação desse botão ele pode ser nomeado, movimentado 
        a sua posição e redimensionado de tamanho.
    botao_historico: object
        Um botão que é usado para realizar uma determinada ação que é a de ir para a tela de histórico, na criação desse botão ele pode ser nomeado, movimentado 
        a sua posição e redimensionado de tamanho.

    botao_voltar: object
        Um botão que é usado para realizar uma determinada ação que é a de voltar para a tela anterior, na criação desse botão ele pode ser nomeado, movimentado 
        a sua posição e redimensionado de tamanho.

    Methods
    -------
    Carregar_Janela ():
        Gera a janela geral
    """
    def __init__(self):
        super().__init__()

        self.esquerda = 0
        self.topo = 0
        self.largura = 1460
        self.altura = 800
        self.titulo = 'Tela Geral'


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


        self.botao_voltar = QPushButton("Voltar", self)
        self.botao_voltar.move(1150, 30)
        self.botao_voltar.resize(100,40)

        self.Criar_Tela()

    def Criar_Tela(self):
        '''
        A função "Criar_Tela" cria uma janela na tela de acordo com os dados adicionado nos atributos
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
    tela = Tela_Geral()
    sys.exit(aplicativo.exec_())
"""