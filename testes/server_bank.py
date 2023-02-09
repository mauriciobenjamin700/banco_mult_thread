import socket
#ip usada para outra pessoa se conectar a minha maquina de forma local
#ip = '0.0.0.0'
############################# dados abaixo são padrão para criação do socket  ########################################
ip = 'localhost'
port = 9000

addr = ((ip, port))#define a tupla de endereço
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(10)
############################################## aguardando o cliente se conectar ######################################
print('aguardando conexão...\n')
con, cliente = serv_socket.accept()
#######################################################################################

################################################# após o cliente se conectar, será executado o seguinte laço
while (True):
    try:
        # variavel msg_cliente recebe alguma string enviada pelo cliente
        msg_cliente = con.recv(1024)
        print('mensagem recebida:' + msg_cliente.decode())
        # se o cliente mandar  a msg 'sair' a coneção será encerrada
        if msg_cliente.decode() == 'sair':
            print('conexão encerrada!')
            con.send('sair'.encode())
            serv_socket.close()
            break
        enviar = input('Digite uma mensagem para enviar ao clinete: ')
        con.send(enviar.encode())
    except:
        serv_socket.close()