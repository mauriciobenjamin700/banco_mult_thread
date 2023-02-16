from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit

class Tela_Cadastro(QMainWindow):
    """
    uma classe para representar uma tela de cadastro
    
    ...

    Attributes:
    --------
    esquerda: int
     define a posição da "tela cadastro" no lado esquerdo da tela de visualização 
     topo: int
     define a posição da "tela cadastro" no topo da tela de vizualisação
     largura: int
     define a largura da "tela cadastro" na tela de visualização.
     altura: int
     define a altura da "tela cadastro" na tela de visualização.
     titulo: str
     define o titulo da "tela cadastro" na tela de visualização.
    """
    def __init__ (self):
        super().__init__()
###################################### Estrutura da janela ###################################
        self.esquerda = 0
        self.topo = 0
        self.largura = 1460
        self.altura = 800
        self.titulo = "TELA DE CADASTRO"

####################################### LABEL ###############################################
        '''
        
        Attributes:
        --------
        label1: object
        rotula algum lugar da tela, onde você define um texto, movimenta a posição desse texto, redimensiona o tamanho da label e adiciona o tamanho da fonte.
        label_nome: object
        rotula algum lugar da tela, onde você define um texto, movimenta a posição desse texto, redimensiona o tamanho da label e adiciona o tamanho da fonte.
        label_sobrenome: object
        rotula algum lugar da tela, onde você define um texto, movimenta a posição desse texto, redimensiona o tamanho da label e adiciona o tamanho da fonte.
        label_cpf: object
        rotula algum lugar da tela, onde você define um texto, movimenta a posição desse texto, redimensiona o tamanho da label e adiciona o tamanho da fonte.
        label_login: object
        rotula algum lugar da tela, onde você define um texto, movimenta a posição desse texto, redimensiona o tamanho da label e adiciona o tamanho da fonte.
        label_senha: object
        rotula algum lugar da tela, onde você define um texto, movimenta a posição desse texto, redimensiona o tamanho da label e adiciona o tamanho da fonte.
        '''
        self.label1 = QLabel(self)
        self.label1.setText("CADASTRE-SE AGORA")
        self.label1.move(540,0)
        self.label1.resize(400,100)
        self.label1.setStyleSheet("QLabel {font: 30px}")

        self.label_nome = QLabel(self)
        self.label_nome.setText("Nome")
        self.label_nome.move(400, 150)
        self.label_nome.resize(100,40)
        self.label_nome.setStyleSheet("QLabel {font: 30px}")

        self.label_sobrenome = QLabel(self)
        self.label_sobrenome.setText("Sobrenome")
        self.label_sobrenome.move(400, 250)
        self.label_sobrenome.resize(200,40)
        self.label_sobrenome.setStyleSheet("QLabel {font: 30px}")

        self.label_CPF = QLabel(self)
        self.label_CPF.setText("CPF")
        self.label_CPF.move(400, 350)
        self.label_CPF.resize(100,40)
        self.label_CPF.setStyleSheet("QLabel {font: 30px}")

        self.label_login = QLabel(self)
        self.label_login.setText("Login")
        self.label_login.move(400, 450)
        self.label_login.resize(100,40)
        self.label_login.setStyleSheet("QLabel {font: 30px}")

        self.label_senha = QLabel(self)
        self.label_senha.setText("Senha")
        self.label_senha.move(400, 550)
        self.label_senha.resize(100,40)
        self.label_senha.setStyleSheet("QLabel {font: 30px}")


       
############################################### LINE EDIT ###############################
        '''
        
        Attributes:
        --------
        LineEdit_nome: object
        É uma caixa de texto onde o usuario pode adicionar o seu nome.
        LineEdit_sobrenome: object
        É uma caixa de texto onde o usuario pode adicionar o seu sobrenome.
        LineEdit_cpf: object
        É uma caixa de texto onde o usuario pode adicionar o seu cpf.
        LineEdit_login: object
        É uma caixa de texto onde o usuario pode adicionar o seu usuário de login.
        LineEdit_senha: object
        É uma caixa de texto onde o usuario pode adicionar a sua senha de login.
        '''
        self.LineEdit_nome = QLineEdit(self)
        self.LineEdit_nome.move(700, 150)
        self.LineEdit_nome.resize(300,40)
        self.LineEdit_nome.setStyleSheet("QLineEdit {font: 20px}")
        self.LineEdit_nome.setPlaceholderText("Digite seu primeiro nome aqui!")


        self.LineEdit_sobrenome = QLineEdit(self)
        self.LineEdit_sobrenome.move(700, 250)
        self.LineEdit_sobrenome.resize(300,40)
        self.LineEdit_sobrenome.setStyleSheet("QLineEdit {font: 20px}")
        self.LineEdit_sobrenome.setPlaceholderText("Digite seu sobrenome aqui!")

        self.LineEdit_CPF = QLineEdit(self)
        self.LineEdit_CPF.move(700, 350)
        self.LineEdit_CPF.resize(300,40)
        self.LineEdit_CPF.setStyleSheet("QLineEdit {font: 20px}")
        self.LineEdit_CPF.setPlaceholderText("Digite seu CPF aqui!")

        self.LineEdit_login = QLineEdit(self)
        self.LineEdit_login.move(700, 450)
        self.LineEdit_login.resize(300,40)
        self.LineEdit_login.setStyleSheet("QLineEdit {font: 20px}")
        self.LineEdit_login.setPlaceholderText("Digite seu Login aqui!")

        self.LineEdit_senha = QLineEdit(self)
        self.LineEdit_senha.move(700, 550)
        self.LineEdit_senha.resize(300,40)
        self.LineEdit_senha.setStyleSheet("QLineEdit {font: 20px}")
        self.LineEdit_senha.setPlaceholderText("Digite sua senha aqui!")


        
###################################### BOTÕES ###########################################3
        '''
        
        Attributes:
        --------
        botao1: object
        Um botão que é usado para realizar uma determinada ação que é a de cadastrar, onde ele pode ser nomeado, movimentado 
        a sua posição e redimensionado de tamanho.
        botao2: object
        Um botão que é usado para realizar uma determinada ação que é a de voltar para a tela anterior, onde ele pode ser nomeado, movimentado 
        a sua posição e redimensionado de tamanho.
        '''
        self.botao1 = QPushButton("CADASTRAR", self)
        self.botao1.move(700,650)
        self.botao1.resize(200,40)
        self.botao1.setStyleSheet("QPushButton {font: 30px; background-color: green}")

        self.botao2 = QPushButton("Voltar", self)
        self.botao2.move(1150, 30)
        self.botao2.resize(100,40)

############################## criando a janela ############################
        self.Carregar_Janela()

    def Carregar_Janela (self):
        """
        A função "Carrega_Janela" cria uma janela na tela de acordo com os dados adicionado nos atributos
        esquerdo, topo, largura, altura e titulo
        """

        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        
        self.setWindowTitle(self.titulo)
        
        self.show()

if __name__ == '__main__':
    """
    Em caso de teste utilizasse o " if __name__ == '__main__' "
    """
    import sys
    aplicacao =  QApplication(sys.argv)
    j = Tela_Cadastro()
    sys.exit(aplicacao.exec_())