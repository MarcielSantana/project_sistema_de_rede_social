from datetime import datetime


class Usuario:
    def __init__(self, nome: str, username: str, bio: str):
        self.nome = nome
        self.username = username
        self.bio = bio
        self.amigos = []
        self.postagens = []

    def adicionar_amigo(self, username):
        if username not in self.amigos:
            self.amigos.append(username)
            return 'amigo adicionado com sucesso'
        return 'amigo já está na lista'

    def remover_amigo(self, username):
        if username in self.amigos:
            self.amigos.remove(username)
            return 'amigo removido com sucesso'
        return 'amigo não encontrado'

    def fazer_postagem(self, conteudo, data):
        data_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        nova_postagem = Postagem(conteudo, data_atual)
        self.postagens.append(nova_postagem)
        return 'postagem feita com sucesso'

    def listar_postagens(self):
        return [post.info() for post in self.postagens]


class Postagem:
    def __init__(self, conteudo: str, data: str):
        self.conteudo = conteudo
        self.data = data

    def info(self):
        return f'{self.conteudo} e postado em {self.data}'


class RedeSocial():
    def __init__(self):
        self.usuarios = {}

    def criar_usuario(self, nome: str, username: str, bio: str):
        if username in self.usuarios:
            return 'Erro: usuário já cadastrado'
        novo_usuario = Usuario(nome, username, bio)
        self.usuarios[username] = novo_usuario
        return 'Usuário cadastrado com sucesso'

    def buscar_usuario(self, username):
        return self.usuarios.get(username, 'Usuário não encontrado')

    def listar_usuario(self):
        print("Usuários cadastrados:")
        for username in self.usuarios:
            print(f"- {username}")


# Criando a rede social
rede = RedeSocial()

# Adicionando usuários
rede.criar_usuario("João Silva", "joaosilva", "Amante de tecnologia")
rede.criar_usuario("Maria Souza", "mariasouza", "Apaixonada por fotografia")

# Buscando um usuário
usuario = rede.buscar_usuario("joaosilva")
if isinstance(usuario, Usuario):
    # Fazendo uma postagem
    usuario.fazer_postagem("Minha primeira postagem!", 26/10/2024)
    usuario.fazer_postagem("Olá, mundo!", 26/10/2024)

    # Listando as postagens
    for postagem in usuario.listar_postagens():
        print(postagem)
