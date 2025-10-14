# Sistema Task Manager

Gianluca Mariano Sobreiro RA: 22.122.011-4 <br>
Guilherme Fornagiero de Carvalho RA: 22.122.016-3 <br>
Paulo Vinicius Bessa de Brito RA: 22.122.005-6 <br>
Pedro Augusto Bento Rocha RA: 22.122.028-8 

## Estrutura do Projeto

-   `task_manager/`: Contém o código-fonte principal da aplicação.
    -   `task.py`: Modelo de domínio (Task, Priority, Status).
    -   `storage.py`: Mecanismo de armazenamento de dados em memória.
    -   `repository.py`: Padrão de repositório para gerenciar a persistência de tarefas.
    -   `service.py`: Camada de lógica de negócio (Bônus).
-   `tests/`: Contém os testes automatizados.
    -   `test_task.py`: Testes unitários para a classe Task.
    -   `test_repository.py`: Testes unitários para o TaskRepository, usando mocks.
-   `requirements.txt`: Dependências do projeto.

## Instalação

Para instalar execute o  comando:
```bash
pip install -r requirements.txt
