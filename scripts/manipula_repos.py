import base64
import requests
from env import access_token

class ManipulaRepositorios:

    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = access_token
        self.headers = {'Authorization':"Bearer " + self.access_token,
                        'X-GitHub-Api-Version': '2022-11-28'}
        
    def cria_repo(self, nome_repo, desc_repo):
        data = {
            "name": nome_repo,
            "description": desc_repo,
            "private": False
        }
        response = requests.post(f"{self.api_base_url}/user/repos", json=data, headers=self.headers)

        print(f'status_code criação do repositório: {response.status_code}')

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo, comment):

        with open(caminho_arquivo, "rb") as file:
            file_content = file.read()

        encoded_content = base64.b64encode(file_content)

        url = f"{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}"
        data = {
            "message": comment,
            "content": encoded_content.decode("utf-8")
        }

        response = requests.put(url, json=data, headers=self.headers)
        print(f'status_code upload do arquivo: {response.status_code}')

    
novo_repo = ManipulaRepositorios('uDanielBispo')

nome_repo = 'linguagens-repositorios-empresas'
novo_repo.cria_repo(nome_repo, "Repositório criado automaticamente via script python de outro repositório com o nome de 'learning-requests-python'")

novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'processed_files/linguagens_amzn.csv', 'Arquivo de dados das linguagens usadas no github da amazon')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'processed_files/linguagens_netflix.csv', 'Arquivo de dados das linguagens usadas no github da Netflix')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'processed_files/linguagens_spotify.csv', 'Arquivo de dados das linguagens usadas no github do Spotify')
novo_repo.add_arquivo(nome_repo, 'linguagens_apple.csv', 'processed_files/linguagens_apple.csv', 'Arquivo de dados das linguagens usadas no github do apple')