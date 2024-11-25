# project_sistema_de_rede_social

Projeto de um sistema de rede social

Aqui está um README otimizado para publicar no GitHub:  

---

# Rede Social Simples  

Uma aplicação básica para simular as principais funcionalidades de uma rede social. Este projeto foi desenvolvido em Python, utilizando conceitos de orientação a objetos para gerenciar usuários, postagens e amizades.  

## 📋 Funcionalidades  

- **Cadastro de Usuários:** Crie usuários com nome, username e uma biografia personalizada.  
- **Gerenciamento de Amigos:** Adicione e remova amigos.  
- **Postagens:** Permita que os usuários criem postagens e as visualizem posteriormente.  
- **Listagem de Usuários e Postagens:** Exiba os usuários cadastrados e todas as postagens feitas.  

## 🛠️ Estrutura do Projeto  

O projeto contém três classes principais:  

1. **`Usuario`**  
   Gerencia as informações e ações relacionadas ao usuário, como a lista de amigos e postagens.  

2. **`Postagem`**  
   Representa uma postagem com o conteúdo e a data em que foi criada.  

3. **`RedeSocial`**  
   Gerencia o cadastro e busca de usuários, além de permitir interações entre eles.  

## 🚀 Como Usar  

### Clone o repositório  

```bash  
git clone https://github.com/seu-usuario/rede-social-simples.git  
cd rede-social-simples  
```  

### Execute o código  

1. Certifique-se de que você tem o Python 3.7 ou superior instalado.  
2. Execute o script:  

```bash  
python3 main.py  
```  

### Exemplo de Uso  

#### Criando Usuários  

```python  
rede = RedeSocial()  
rede.criar_usuario("João Silva", "joaosilva", "Amante de tecnologia")  
rede.criar_usuario("Maria Souza", "mariasouza", "Apaixonada por fotografia")  
```  

#### Gerenciando Amigos  

```python  
usuario = rede.buscar_usuario("joaosilva")  
usuario.adicionar_amigo("mariasouza")  
usuario.remover_amigo("mariasouza")  
```  

#### Fazendo Postagens  

```python  
usuario.fazer_postagem("Minha primeira postagem!", "26/10/2024")  
usuario.fazer_postagem("Olá, mundo!", "26/10/2024")  
```  

#### Listando Postagens  

```python  
for postagem in usuario.listar_postagens():  
    print(postagem)  
```  

## 🔧 Melhorias Futuras  

- Implementar persistência de dados com banco de dados ou arquivos.  
- Adicionar uma interface gráfica ou web.  
- Permitir curtidas, comentários e compartilhamentos em postagens.  
- Desenvolver testes unitários para as classes.  

## 🤝 Contribuições  

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias ou sugestões.  

## 📄 Licença  

Este projeto está licenciado sob a [MIT License](LICENSE).  

---  

Sinta-se à vontade para personalizar conforme suas necessidades!
