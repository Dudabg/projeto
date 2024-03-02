
# Teste para Desenvolvedor Python/Flask
Descrição do Projeto

- Este é um projeto simples de uma aplicação web desenvolvida em Python utilizando o framework Flask. A aplicação permite aos usuários realizar operações CRUD (Create, Read, Update, Delete) em registros de uma entidade chamada "Produto", armazenados em um banco de dados MySQL. A interface é construída com HTML/CSS para fornecer uma experiência básica e intuitiva ao usuário.

# Requisitos Técnicos

1- Backend:
   1.1 Python com Flask: Utilizado para criar a aplicação web.
   1.2 MySQL: Banco de dados utilizado para armazenar os registros dos produtos.
   1.3 Conexão segura com o banco de dados: Garantida para proteger os dados.
   1.4 Padrão de classes: Utilizado para definir e manipular entidades no backend.


2-Frontend:
  2.1 HTML/CSS: Interface simples e intuitiva para os usuários realizarem operações CRUD nos produtos.
  2.2 O código CSS está organizado em três partes, cada uma correspondendo a uma página da aplicação: produto.css, criar.css e editar.css. Cada parte contém estilos específicos para a respectiva página.


3- Controle de Versão:
  3.1 Git: Utilizado para versionar o código.


4- Gestão de projeto 
  4.1 Trello: foi utilizado a plataforma Trello para a gestao desse projeto no model kaban
  4.2 Quadros: "To do" , "Doing" , "Code review", "Testing phase", "Done".


# Estrutura do Projeto
A estrutura do projeto segue a seguinte organização:

├── app.py                   # Arquivo principal da aplicação Flask
├── models.py                # Define as classes de modelo para manipulação de entidades
├── templates/               # Diretório contendo os templates HTML
│   ├── criar.html           # Template para adicionar um novo produto
│   ├── editar.html          # Template para editar um produto existente
│   ├── index.html           # Template para visualizar todos os produtos cadastrados
├── static/                  # Diretório contendo arquivos estáticos como CSS
│   └── style.css            # Arquivo CSS para estilização da interface
├── README.md                # Documentação do projeto (este arquivo)



# Instruções de Configuração e Uso

- Configuração do Ambiente

1 Clone o repositório do projeto:
- git clone https://github.com/seu-usuario/nome-do-repositorio.git


2 Acesse o diretório do projeto:

- cd nome-do-repositorio


3 Instale as dependências do Python listadas no arquivo requirements.txt:

- pip install -r requirements.txt


4 Configuração do Banco de Dados

- Certifique-se de ter o servidor MySQL instalado e em execução em sua máquina.
- Crie um banco de dados chamado user e que tenha a tabela users(id,name,email,password) e a tabela produto(idproduto,nome,descricao,preco) .


5 Execução da Aplicação
 5.1- Execute o arquivo app.py para iniciar o servidor Flask:
     - python app.py


6 Acesse a aplicação em seu navegador web através do endereço http://localhost:5000.

7 Autenticação de Usuário
- Foi implementada autenticação de usuário para garantir a segurança dos dados e restringir o acesso às operações CRUD apenas a usuários autenticados.

8 Documentação
- A documentação incluída neste README fornece instruções claras e completas sobre como configurar e utilizar a aplicação. Qualquer dúvida ou problema, entre em contato.


8- Contribuição
Contribuições são bem-vindas! Se você deseja propor melhorias ou correções, fique à vontade para abrir uma issue ou enviar um pull request.

