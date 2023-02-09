import socket

#ip = '10.180.42.64' #colocar o ipv4 da maquina servidor
ip = 'localhost'
port = 9000

addr = ((ip, port))#define a tupla de endereço
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(addr)

while (True):
    try:
        #cliente_socket.send(f'0,nome,sobrenome,cpf,login,senha'.encode())
        cliente_socket.send(f'1,Teste,01,teste1,t,1'.encode())
        print ('mensagem enviada! ')
        msg_recebida = cliente_socket.recv(1024).decode()
        print('mensagem recebida: ' + msg_recebida)
        if msg_recebida == 'sair':
    
            cliente_socket.close()
            break

    except:
        cliente_socket.close()