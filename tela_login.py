from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit

class Tela_Login(QMainWindow):
    """
    uma classe para representar uma tela login
        
    ...

    Attributes
    ----------
    esquerda: int
        define a posição da "tela login" no lado esquerdo da tela de visualização 
    topo: int
        define a posição da "tela login" no topo da tela de vizualisação
    largura: int
        define a largura da "tela login" na tela de visualização
    altura: int
        define a altura da "tela login" na tela de visualização.
    titulo: str
        define o titulo da "tela login" na tela de visualização.

    label1: object
        rotula algum lugar da tela onde você define um texto, movimenta a posição, redimensiona o tamanho da label e adiciona o tamanho da fonte.
    label_login: object
        rotula algum lugar da tela onde você define um texto, movimenta a posição desse texto, redimensiona o tamanho da label e adiciona o tamanho da fonte.
    label_senha: object
        rotula algum lugar da tela onde você define um texto, movimenta a posição desse texto, redimensiona o tamanho da label e adiciona o tamanho da fonte.

    LineEdit_login: object
        É uma caixa de texto onde o usuario pode adicionar o usuário de login que criou para poder logar na conta.
    LineEdit_senha: object
        É uma caixa de texto onde o usuario pode adicionar a senha de login que criou para poder logar na conta.

    botao_login: object
        Um botão que é usado para realizar uma determinada ação que é a de logar e ir para a tela da conta, na criação desse botão ele pode ser nomeado, movimentado 
        a sua posição e redimensionado de tamanho.
    botao_voltar: object
        Um botão que é usado para realizar uma determinada ação que é a de voltar para a tela anterior, na criação desse botão ele pode ser nomeado, movimentado 
        a sua posição e redimensionado de tamanho.
    Methods
    -------
    Carregar_Janela ():
        Gera a janela login
        """
    def __init__ (self):
       
        super().__init__()
        
        self.esquerda = 0
        self.topo = 0
        self.largura = 1460
        self.altura = 800
        self.titulo = "TELA DE LOGIN"


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
        '''
        A função "Criar_Janela" cria uma janela na tela de acordo com os dados adicionado nos atributos
        esquerdo, topo, largura, altura e titulo

        parameters:
            None
        return
            None
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
    j = Tela_Login()
    sys.exit(aplicacao.exec_())
    