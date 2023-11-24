## FastAPI template

Simple backend template with FastAPI, PostgreSQL, SQLAlchemy and Alembic

### Contents.
1. [Project Structure.](https://github.com/nuriatimerkaeva/FastAPI_template#1-project-structure)
2. [How to copy a project.](https://github.com/nuriatimerkaeva/FastAPI_template#2-how-to-copy-a-project)
3. [Env-file.](https://github.com/nuriatimerkaeva/FastAPI_template#3-how-to-copy-a-project)
4. [Run a project.](https://github.com/nuriatimerkaeva/FastAPI_template#4-run-project)

### 1. Project Structure.
```
fastapi_project/
├── src/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── dependencies.py
│   │   │   └── user_router.py
│   │   ├── __init__.py
│   │   └── router.py
│   ├── common/
│   │   ├── dto/
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   ├── interfaces/
│   │   │   ├── repository.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── abstract_repository.py
│   │   │   │   └── base_repo.py
│   │   │   ├── __init__.py
│   │   │   └── uow.py
│   │   ├── middlewares/
│   │   │   ├── __init__.py
│   │   │   └── process_time.py
│   │   ├── templates/
│   │   │   ├── __init__.py
│   │   │   ├── confirm_password.html
│   │   │   └── new_account.html
│   │   ├── __init__.py
│   │   ├── model_converters.py
│   │   └── typess.py
│   └── core/
│   │   ├── __init__.py
│   │   └── settingss.py
│   └── services/
│   │   ├── database/
│   │   │   ├── migrations/ # default alembic folder
│   │   │   ├── models/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── base.py
│   │   │   │   └── user.py
│   │   │   ├── repositories/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── base.py
│   │   │   │   ├── crud.py
│   │   │   │   └── user_repo.py
│   │   │   ├── __init__.py
│   │   │   └── session.py
│   │   ├── security/
│   │   │   ├── __init__.py
│   │   │   ├── jwt.py
│   │   │   └── security.py
│   │   └── __init__.py
│   ├── __init__.py
│   └── __main__.py
├── .dockerignore
├── .env_axample
├── .flake8
├── .gitignore
├── .pylintrc
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── mypy.ini
├── README.md
└── requirements.txt
```

### 2. How to copy a project.
```
git clone https://github.com/nuriatimerkaeva/FastAPI_template.git
```

### 3. Env-file.

```
Rename .env_example to .env and set your values.

DB_URL = postgresql+asyncpg:///{}
DB_USER = username
DB_PASSWORD = password
DB_HOST = host
DB_PORT  = port
DB_NAME  = dbname
```

### 4. Run a project

```
Go to your working directory and enter the command:
    ```bash
    docker compose up

The aplication is available at:

http://localhost:8001.

The documentation is available at:

http://localhost:8001/docs.
```
