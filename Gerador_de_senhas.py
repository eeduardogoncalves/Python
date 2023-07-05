import random

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-!@#$%^&*()_+=[]{};':|,.<>/?"
while True:
    try:
        length = int(input("Tamanho da Senha: "))
        qty = int(input("Quantidade de Senhas: "))
    except ValueError:
        print("Entrada inválida!")
    else:
        for _ in range(qty):
            passwd = ""
            for _ in range(length):
                passchar = random.choice(char)
                passwd += passchar
            print("Senha gerada:", passwd)
        break





import random  # Importa o módulo random para gerar senhas aleatórias

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-!@#$%^&*()_+=[]{};':|,.<>/?"
# Define uma string chamada 'char' que contém todos os caracteres que podem ser usados para gerar senhas

while True:  # Loop infinito, executa continuamente até ser interrompido
    try:
        length = int(input("Tamanho da Senha: "))
        # Solicita ao usuário o tamanho da senha e converte a entrada em um número inteiro
        qty = int(input("Quantidade de Senhas: "))
        # Solicita ao usuário a quantidade de senhas e converte a entrada em um número inteiro
    except ValueError:
        print("Entrada inválida!")
        # Se ocorrer um ValueError durante a conversão, imprime uma mensagem de erro informando que a entrada é inválida
    else:
        for _ in range(qty):  # Loop que executa 'qty' vezes
            passwd = ""  # Inicializa a variável 'passwd' como uma string vazia
            for _ in range(length):  # Loop que executa 'length' vezes
                passchar = random.choice(char)
                # Seleciona aleatoriamente um caractere da string 'char' e armazena em 'passchar'
                passwd += passchar
                # Concatena o caractere selecionado à variável 'passwd'
            print("Senha gerada:", passwd)  # Imprime a senha gerada
        break
        # Encerra o loop infinito e termina a execução do programa
