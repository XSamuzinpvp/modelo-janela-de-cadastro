# Sistema de Login com Banco de Dados Local

Este é um sistema de login simples desenvolvido em Python, que utiliza um banco de dados local para armazenar os dados de usuários. Ele foi projetado para funcionar sem criptografia e é ideal para projetos iniciais ou aplicações locais.

## Funcionalidades

- **Entrada de Dados:** Permite que o usuário insira um nome de usuário e uma senha.
- **Validação de Usuário:** Verifica se o nome de usuário já está registrado no banco de dados local antes de criar uma nova entrada.
- **Banco de Dados Local:** Armazena os dados de login em um arquivo de texto (bancodedados.txt).

## Como Funciona

1. **Interface Gráfica:** A interface é criada utilizando a biblioteca `customtkinter`, proporcionando uma aparência moderna e escura.
2. **Validação:** Antes de salvar um novo usuário, o sistema verifica se o nome de usuário já está em uso.
3. **Armazenamento:** Os dados de login (nome de usuário e senha) são armazenados no arquivo `bancodedados.txt` no mesmo diretório do programa.

## Como Usar

1. Certifique-se de ter o Python instalado na sua máquina (versão 3.10 ou superior recomendada).
2. Instale a biblioteca `customtkinter` utilizando o comando:
   ```
   pip install customtkinter
   ```
3. Baixe ou clone este repositório.
4. Execute o arquivo principal do sistema de login:
   ```
   python login_system.py
   ```
5. Use a interface gráfica para criar um novo usuário ou verificar logins existentes.

## Autor

Este projeto foi desenvolvido por **XSamuzin\_pvp**.

- Canal do YouTube: [XSamuzin Plays](https://www.youtube.com/@XSamuzin_plays)

## Futuras Implementações

- Integração com um sistema de criptografia para maior segurança.
- Interface mais personalizada e responsiva.
- Conexão com bancos de dados externos como MySQL ou PostgreSQL.

Acompanhe as atualizações no canal do YouTube e fique por dentro das novidades!

