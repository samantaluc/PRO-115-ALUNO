#instalar as bibliotecas usando pip install no terminal. Para a biblioteca da 7 e 8, usar pip install watchdog


# Defina as pastas de origem (Downloads) e destino (onde os arquivos serão organizados)
from_dir = "C:/Users/???/Downloads"
to_dir = "C:/Users/???/Desktop/download_files"

# Define um dicionário que mapeia categorias de arquivos às extensões correspondentes
dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],  # Categorias de imagens
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],  # Categorias de vídeos
    "Document_Files": ['.ppt', '.xls', '.xlsx', '.csv', '.pdf', '.txt'],  # Categorias de documentos
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']  # Categorias de programas de instalação
}

# Classe Gerenciadora de Eventos
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Obtém o nome do arquivo e sua extensão
        name, extension = os.path.splitext(event.src_path)

        time.sleep(1)

        # Itera sobre as categorias definidas em dir_tree
        for key, value in dir_tree.items():
            time.sleep(1)

            if extension in value:
                # Obtém o nome do arquivo
                file_name = os.path.basename(event.src_path)

                print("Foi feito o download de ..." + file_name)

                # Monta os caminhos para a pasta de origem e de destino
                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                # Verifica se a pasta de destino já existe
                
                    
                    # Verifica se o arquivo já existe na categoria de destino
                    
                        
                        # Renomeia o arquivo com um número aleatório
                       
                        # Move o arquivo renomeado para a pasta de destino
                        
                    else:
                        print("Movendo " + file_name + "....")
                        # Move o arquivo para a pasta de destino
                        shutil.move(path1, path3)
                        time.sleep(1)
                else:
                    print("Criando novo destino...")
                    # Cria a pasta de destino se ela não existe
                    os.makedirs(path2)
                    print("Movendo " + file_name + "....")
                    # Move o arquivo para a pasta de destino
                    shutil.move(path1, path3)
                    time.sleep(1)

# Inicialize a Classe Gerenciadora de Eventos

# Inicialize o Observer

# Agende o Observer para monitorar a pasta de origem (Downloads)

# Inicie o Observer em um loop

    # Interrompe o Observer quando o usuário pressiona Ctrl+C
    
