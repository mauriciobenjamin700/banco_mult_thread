from banco import Banco
import socket
import threading


bank = Banco()
############################# dados abaixo são padrão para criação do socket  ########################################
class usuario(threading.Thread):

    """
    Classe que representa um usuário do banco

    ...
    Atributos
    ---------
    con : objeto
        conexão da maquina que o usuário está usando 
    adress : objeto
        endereço da maquina que o usuário


    """

    def __init__(self,adress,con) -> None:

        """
        Construtor da classe necessário para criar o atributo 
        """

        threading.Thread.__init__(self)
        self.con = con
        self.adress = adress

        #print('Nova conexão:',con)

    def run(self):
        while (True):
            # variavel msg_cliente recebe alguma string enviada pelo cliente
            msg_cliente = self.con.recv(1024).decode()
            comando = msg_cliente.split(',')
            #print(comando)
            #print(f'comando[0] = {comando[0]}\ncomando[1] = {comando[1]}\ncomando[2] = {comando[2]}')
            # se o cliente mandar  a msg 'sair' a coneção será encerrada
            #encerrar
            if comando[0] == '0':
                print(f'conexão {self.con} encerrada!')
                #self.con.send('0'.encode())
                self.con.close()
                break
            #cadastrar
            elif comando[0] == '1':
                retorno_cliente = bank.cadastrar_cliente(comando[3], comando[1], comando[2])
                if retorno_cliente:
                    retorno_conta =  bank.criar_conta(comando[3], comando[4], comando[5])
                    if retorno_conta == True:
                        self.con.send('True'.encode())
                    else:
                        self.con.send('False'.encode)
                else:
                    self.con.send('False'.encode())
            # logar
            elif comando[0] == '2':
                retorno_cliente = bank.logar(comando[1], comando[2])
                if retorno_cliente[0]:
                    self.con.send(f'{retorno_cliente[0]},{retorno_cliente[1]}'.encode())
                    #print(f'logar retornou isso. {retorno_cliente[0]}, {retorno_cliente[1]}')
                else:
                    self.con.send('false'.encode())
            #buscar nome do cliene
            elif comando[0] == '-2':
                retorno = bank.buscar_cliente(comando[1])
                nome = retorno[2]
                self.con.send(nome.encode())
            
            #buscar conta
            elif comando[0] == '3':
                #print(f'buscar conta na posição 1 é {comando[1]}')
                retorno = bank.buscar_conta(comando[1])
                if retorno[0]:
                    #print('buscar conta retornou oq tem em baixo\n\n')
                    #print(f'{retorno[0]},{retorno[1]},{retorno[2]},{retorno[3]},{retorno[4]},{retorno[5]},{retorno[6]}')
                    retorno_cliente = (f'{retorno[0]},{retorno[1]},{retorno[2]},{retorno[3]},{retorno[4]},{retorno[5]},{retorno[6]}')
                    self.con.send(retorno_cliente.encode())
            #depositar
            elif comando[0] == '4':
                retorno = bank.depositar(comando[1], comando[2])
                if retorno[0]:
                    self.con.send(f'{retorno[0]},{retorno[1]}'.encode())
                else:
                    self.con.send('False'.encode())  
            #sacar
            elif comando[0] == '5':
                #valor, num conta, senha
                retorno = bank.sacar(comando[1], comando[2], comando[3])

                self.con.send(f'{retorno[0]},{retorno[1]}'.encode())

            #transferir
            elif comando[0] == '6':
                #valor,num_conta, senha, num_conta_destino
                retorno = bank.transferir(comando[1], comando[2], comando[3], comando[4])
                
                self.con.send(f'{retorno[0]},{retorno[1]}'.encode())

            #historico
            elif comando[0] == '7':
                #conta logada
                string = ''
                historico = bank.historico(comando[1])
                if historico != None:
                    for tupla in historico:
                            for transacao in tupla:
                                string += transacao
                                string += ','
                
                #print(string)
                self.con.send(string.encode())

            else:
                print('conexão encerrada!')
            #enviar = input('Digite uma mensagem para enviar ao clinete: ')
            #self.con.send(enviar.encode())
                self.con.close()
                serv_socket.close()
                print('Servidor Encerrado! ')
                

ip = '0.0.0.0'
port = 9002

addr = ((ip, port))#define a tupla de endereço
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)

while True:
    serv_socket.listen(10)

    print('aguardando conexão...\n')
    conexao, cliente = serv_socket.accept()
    newthread = usuario(cliente, conexao)
    newthread.start()
    print('Conectado\n')
    

