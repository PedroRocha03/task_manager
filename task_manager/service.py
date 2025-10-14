from datetime import datetime
from task_manager.task import Task, Priority, Status
from task_manager.repository import TaskRepository

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def criar_tarefa(
        self, titulo: str, descricao: str, prioridade: Priority, prazo: datetime
    ) -> Task:
        nova_tarefa = Task(
            id=None,
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade,
            prazo=prazo,
        )
        nova_tarefa.validar()
        return self.repository.save(nova_tarefa)

    def listar_todas(self) -> list[Task]:
        return self.repository.find_all()

    def atualizar_status(self, id: int, status: Status) -> Task | None:
        tarefa = self.repository.find_by_id(id)
        if tarefa:
            tarefa.status = status
            self.repository.save(tarefa)
            return tarefa
        return None