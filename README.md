# task-manager-backend

Este é um repositório para uma API de gerenciamento de tarefas desenvolvida com Django e Django REST Framework.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/Franciscovj/task-manager-backend.git
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # No Windows
    source .venv/bin/activate  # No macOS/Linux
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Faça as migrações:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Inicie o servidor:
    ```bash
    python manage.py runserver
    ```


 ```sh
Exemplo de Requisição
Aqui está um exemplo de uma requisição GET para obter as tarefas:

Requisição

GET /api/tasks/ HTTP/1.1
Host: localhost:8000
Accept: application/json

Resposta
HTTP/1.1 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "title": "estudar djangorestframework",
        "description": "melhorando as habilidades como backend",
        "completed": false,
        "created_at": "2024-07-25T14:11:49.752910Z",
        "updated_at": "2024-07-25T14:12:00.374853Z",
        "due_date": "2024-07-25T14:11:41Z",
        "priority": "H"
    }
]
 ```
