from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit

class Tela_Transferencia(QMainWindow):
    def __init__ (self):
        super().__init__()
        """
        uma classe para representar uma tela transferencia
        --------
        Atributos:
        --------
        esquerda: int
        define a posição da "tela transferencia" no lado esquerdo da tela de visualização 
        topo: int
        define a posição da "tela transferencia" no topo da tela de vizualisação
        largura: int
        define a largura da "tela transferencia" na tela de visualização
        altura: int
        define a altura da "tela transferencia" na tela de visualização.
        titulo: str
        define o titulo da "tela transferencia" na tela de visualização.
        """
        self.esquerda = 0
        self.topo = 0
        self.largura = 1460
        self.altura = 800
        self.titulo = "TELA DE TRANSFERENCIA"
####################################### LABEL #######################
        '''
        --------
        Atributos:
        --------
        label1: rotula algum lugar da tela onde você define um texto, movimenta a posição, redimensiona o tamanho da label e adiciona o tamanho da fonte.
        label_valor: rotula algum lugar da tela onde você define um texto, movimenta a posição desse texto, redimensiona o tamanho da label e adiciona o tamanho da fonte.
        label_senha: rotula algum lugar da tela onde você define um texto, movimenta a posição desse texto, redimensiona o tamanho da label e adiciona o tamanho da fonte.
        label_login_recebedor: rotula algum lugar da tela onde você define um texto, movimenta a posição desse texto, redimensiona o tamanho da label e adiciona o tamanho da fonte.
        '''
        self.label1 = QLabel(self)
        self.label1.setText("FAÇA SUA TRANSFERENCIA AQUI")
        self.label1.move(350, 10)
        self.label1.resize(600,200)
        self.label1.setStyleSheet("QLabel {font: 40px}")

        self.label_valor = QLabel(self)
        self.label_valor.setText("Valor a ser transferido:")
        self.label_valor.move(300, 300)
        self.label_valor.resize(100,40)
        self.label_valor.setStyleSheet("QLabel {font: 40px}")

        self.label_senha = QLabel(self)
        self.label_senha.setText("Senha")
        self.label_senha.move(300, 400)
        self.label_senha.resize(150,40)
        self.label_senha.setStyleSheet("QLabel {font: 40px}")

        self.label_login_recebedor = QLabel(self)
        self.label_login_recebedor.setText("Nº Conta do Recebedor")
        self.label_login_recebedor.move(300, 500)
        self.label_login_recebedor.resize(450,50)
        self.label_login_recebedor.setStyleSheet("QLabel {font: 40px}")

############################################### LINE EDIT ####################
        '''
        --------
        Atributos:
        --------
        LineEdit_sacar: É uma caixa de texto onde o usuario pode adicionar o valor que deseja sacar.
        LineEdit_senha: É uma caixa de texto onde o usuario pode adicionar a senha de login que criou para poder realizar o saque.
        LineEdit_login_recebedor: É uma caixa de texto onde o usuario pode adicionar o login de destino que receberá a transferência.

        '''
        self.LineEdit_sacar = QLineEdit(self)
        self.LineEdit_sacar.move(600, 300)
        self.LineEdit_sacar.resize(300,40)
        self.LineEdit_sacar.setStyleSheet('QLineEdit {font: 30px}')

        self.LineEdit_senha = QLineEdit(self)
        self.LineEdit_senha.move(600, 400)
        self.LineEdit_senha.resize(300,40)
        self.LineEdit_senha.setEchoMode(QLineEdit.Password)
        self.LineEdit_senha.setStyleSheet('QLineEdit {font: 30px}')

        self.LineEdit_login_recebedor = QLineEdit(self)
        self.LineEdit_login_recebedor.move(750, 505)
        self.LineEdit_login_recebedor.resize(300,40)
        self.LineEdit_login_recebedor.setStyleSheet('QLineEdit {font: 30px}')

############################################### QPushButton ##################
        '''
        --------
        Atributos:
        --------
        botao_confirmar_transferencia: Um botão que é usado para realizar uma determinada ação que é a de executar a transferência, na criação desse botão ele pode ser nomeado, movimentado 
        a sua posição e redimensionado de tamanho.
        botao_voltar: Um botão que é usado para realizar uma determinada ação que é a de voltar para a tela anterior, na criação desse botão ele pode ser nomeado, movimentado 
        a sua posição e redimensionado de tamanho.
        '''
        self.botao_confirmar_transferencia = QPushButton('Confirmar Transferencia',self)
        self.botao_confirmar_transferencia.move(500, 620)
        self.botao_confirmar_transferencia.resize(400,60)
        self.botao_confirmar_transferencia.setStyleSheet('QPushButton {font:30px; background-color: green}')

        self.botao_voltar = QPushButton("Voltar", self)
        self.botao_voltar.move(1150, 30)
        self.botao_voltar.resize(100,40)

        self.Carregar_Janela()



    def Carregar_Janela (self):
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
    aplicacao =  QApplication(sys.argv)
    j = Tela_Transferencia()
    sys.exit(aplicacao.exec_())
    