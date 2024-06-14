1. Documentação da Arquitetura do Sistema
1.1. Visão Geral da Arquitetura
O sistema Ticket2Help é uma aplicação de gerenciamento de tickets que permite aos usuários criar e visualizar tickets de hardware e software. O sistema é construído utilizando Python, com conexão a um banco de dados MySQL para armazenamento de dados. A arquitetura é dividida em várias camadas, incluindo a camada de controle, modelo e visualização.

1.2. Componentes Principais
Controllers: Contêm a lógica de negócio e são responsáveis por manipular as interações entre o usuário e o banco de dados.

TicketController: Gerencia a criação, atualização e consulta de tickets.
UserController: Gerencia operações relacionadas a usuários, como login e registro.
Models: Representam as entidades do sistema e são responsáveis por mapear os dados do banco de dados.

Ticket: Classe mãe para todos os tipos de tickets.
HardwareTicket: Herda de Ticket e adiciona atributos específicos de hardware.
SoftwareTicket: Herda de Ticket e adiciona atributos específicos de software.
Views: Gerenciam a interface do usuário e interações.

TicketView: Gerencia o menu e interações relacionadas a tickets.
UserView: Gerencia o menu e interações relacionadas a usuários.
Utils: Contêm utilitários e configurações gerais, como conexão ao banco de dados.

db: Classe para gerenciar a conexão ao banco de dados.
1.3. Diagrama de Arquitetura
plaintext
Copiar código
+-------------------+
|    User View      |
|                   |
| - User View       |
| - Main View       |
| - TechnicianView  |
+---------+---------+
          |
          |
+---------v---------+
|   Ticket View     |
|                   |
| - Ticket menu     |
| - Interactions    |
+---------+---------+
          |
          |
+---------v--------------+
|   Controllers          |
|                        |
| - TicketController     |
| - UserController       |
| - MainController       |
| - StatsController      |
| - TechnicianController |
+---------+--------------+
          |
          |
+---------v---------+
|     Models        |
|                   |
| - Ticket          |
| - HardwareTicket  |
| - SoftwareTicket  |
| - Users           |
+---------+---------+
          |
          |
+---------v---------+
|     Database      |
|                   |
| - db              |
+-------------------+
1.4. Fluxo de Dados
Criação de Ticket:

O usuário seleciona a opção de criar um ticket na TicketView.
TicketView chama o método create_ticket no TicketController.
TicketController insere o ticket no banco de dados e retorna o resultado para TicketView.
Visualização de Tickets:

O usuário seleciona a opção de visualizar tickets na TicketView.
TicketView chama o método get_tickets_by_state no TicketController.
TicketController consulta o banco de dados e retorna os tickets para TicketView.
TicketView exibe os tickets ao usuário.
2. README.md
markdown
Copiar código
# Ticket2Help

## Visão Geral

Ticket2Help é uma aplicação de gerenciamento de tickets que permite aos usuários criar e visualizar tickets de hardware e software. A aplicação é desenvolvida em Python e utiliza um banco de dados MySQL para armazenamento de dados.

## Estrutura do Projeto

- **Controllers**: Contêm a lógica de negócio.
  - `TicketController.py`
  - `UserController.py`
  - `MainController.py`
  - `StatsController.py`
  - `TechnicianController.py`

- **Models**: Representam as entidades do sistema.
  - `Ticket.py`
  - `Users.py`
  - `HardwareTicket.py`
  - `SoftwareTicket.py`
- **Views**: Gerenciam a interface do usuário.
  - `TechnicianView.py`
  - `MainView.py`
  - `UserView.py`
- **Utils**: Utilitários e configurações.
  - `db.py`
  - `Constants.py`
- **Testes**: Testes.
  - `HardwareTicketTest.py`

## Instalação

### Pré-requisitos

- Python 3.x
- MySQL

### Passos

1. Clone o repositório:

   ```bash
   git clone https://github.com/leo70097/projeto_p4
   cd projeto_p4
Crie um ambiente virtual e ative-o:

bash
Copiar código
python -m venv p4_venv
source p4_venv/bin/activate  # Linux/MacOS
p4_venv\Scripts\activate     # Windows
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Configure o banco de dados MySQL:

Crie um banco de dados chamado ticket2help.
Atualize as configurações de conexão em Utils/db.py.
Execute a aplicação:

bash
Copiar código
python main.py

Uso
Registrar: Permite registrar um novo usuário.
Login: Permite fazer login com um usuário existente.
Criar Ticket: Permite criar um ticket de hardware ou software.
Ver Tickets: Permite visualizar tickets de acordo com o estado (por atender ou resolvido).
