import socket

host = "127.0.0.1" #variavel com nome host
port = [80,20,21,22,23,53,110,123,156,143
,161,179,1723,1863,3128,3389,25,443,135,
1434,139,9929,445,3306,8080,31337,5000] # Variavel com nome port passando as portas


for portas in port:  #Jogar a variavel port para dentro de portas

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket simples
	client.settimeout(0.3) #obj settimeout , tempo da conexao em ms
	code = client.connect_ex((host, portas)) # codigo de resposta 0 = ok 
	if code == 0:
		print(" Porta ",portas, "--> OPEN");

# desative o firewall , ports se comunica via Three-way Handshake
