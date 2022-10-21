import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #conexao simples socket
client.connect(("127.0.0.1",2222)) # conectar ao host e a porta
client.send(b"a") #b enviar string, metodo send enviar algo
resposta = client.recv(1024) # aqui no metodo recv, recever dados do servidor
print(resposta.decode()) #.decode decoficar a resposta text simples
