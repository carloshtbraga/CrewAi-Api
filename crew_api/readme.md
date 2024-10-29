<p align="center">
  <img src="https://learn.crewai.com/_next/static/media/crew_only.cd8cdc40.png" alt="Crew Only" width="300" />
</p>

# API Crew AI

Esta é uma API desenvolvida para gerenciar agentes, tarefas e equipes usando a biblioteca Crew AI. A API permite a criação, leitura, atualização e execução de "crews", que são compostas por agentes e suas respectivas tarefas.

## Índice

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Endpoints](#endpoints)
  - [Agentes](#agentes)
  - [Tarefas](#tarefas)
  - [Equipes](#equipes)
- [Modelos](#modelos)
  - [Agent](#agent)
  - [Task](#task)
  - [Crew](#crew)
- [Como Executar](#como-executar)


## Tecnologias Utilizadas

- Django
- Django REST Framework
- Crew AI

## Endpoints

### Agentes

- **Listar Agentes**
  - `GET /agents/`
  
- **Criar Agente**
  - `POST /agents/`
  - **Body**: JSON com os campos necessários para criar um agente.

- **Obter Detalhes de um Agente**
  - `GET /agents/{id}/`

- **Atualizar Agente**
  - `PUT /agents/{id}/`
  - **Body**: JSON com os campos que deseja atualizar.

- **Deletar Agente**
  - `DELETE /agents/{id}/`

### Tarefas

- **Listar Tarefas**
  - `GET /tasks/`
  
- **Criar Tarefa**
  - `POST /tasks/`
  - **Body**: JSON com os campos necessários para criar uma tarefa.

- **Obter Detalhes de uma Tarefa**
  - `GET /tasks/{id}/`

- **Atualizar Tarefa**
  - `PUT /tasks/{id}/`
  - **Body**: JSON com os campos que deseja atualizar.

- **Deletar Tarefa**
  - `DELETE /tasks/{id}/`

### Equipes

- **Listar Equipes**
  - `GET /crews/`
  
- **Criar Equipe**
  - `POST /crews/`
  - **Body**: JSON com os campos necessários para criar uma equipe.

- **Obter Detalhes de uma Equipe**
  - `GET /crews/{id}/`

- **Atualizar Equipe**
  - `PUT /crews/{id}/`
  - **Body**: JSON com os campos que deseja atualizar.

- **Deletar Equipe**
  - `DELETE /crews/{id}/`

- **Executar Kickoff da Equipe**
  - `POST /crews/{id}/execute_kickoff/`
  - **Descrição**: Executa o kickoff da equipe, utilizando os agentes e tarefas associados a ela.
  - **Resposta**: Retorna o resultado da execução.

## Modelos

### Agent

- `name`: Nome do agente.
- `role`: Papel do agente.
- `goal`: Objetivo do agente.
- `verbose`: Define se o agente será detalhado nas respostas.
- `memory`: Se o agente tem ou não memória persistente.
- `backstory`: História de fundo do agente.
- `llm_model_name`: Nome do modelo de linguagem.
- `llm_temperature`: Temperatura do modelo de linguagem.
- `llm_verbose`: Modo detalhado para o modelo de linguagem.
- `allow_delegation`: Define se o agente pode delegar tarefas a outros agentes.
- `created_at`: Data de criação.

### Task

- `agent`: Agente responsável pela tarefa (chave estrangeira).
- `name`: Nome da tarefa.
- `description`: Descrição da tarefa.
- `expected_output`: Formato esperado do output da tarefa.
- `async_execution`: Define se a execução da tarefa é assíncrona.
- `output_file`: Nome do arquivo de saída para o output da tarefa.
- `created_at`: Data de criação.

### Crew

- `agents`: Agentes que compõem a equipe (muitos para muitos).
- `tasks`: Tarefas atribuídas à equipe (muitos para muitos).
- `process`: Tipo de processo da equipe (sequential ou hierarchical).
- `created_at`: Data de criação.

## Como Executar

1. **Clone o repositório**:
   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-repositorio>

2. **Crie ambiente virtual e ative**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate  # Para Windows

3. **Instale as dependências, faça as migrações e inicie o servidor**:
   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-repositorio>
   python manage.py migrate
   python manage.py runserver

