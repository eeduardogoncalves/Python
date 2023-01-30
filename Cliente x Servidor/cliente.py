import socket

HOST = '192.168.0.11'  # Endereço IP do servidor
PORT = 4444  # Porta utilizada pelo servidor

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    command = input('> ')  # Lê os comandos do usuário
    s.send(command.encode())  # Envia os comandos para o servidor
    if command == 'exit':
        s.close()
        break
    output = s.recv(1024).decode()  # Recebe a saída do comando
    print(output)
