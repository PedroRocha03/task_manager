from datetime import datetime
from enum import IntEnum, Enum

class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3

class Status(Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"

class Task:
    def __init__(
        self,
        id: int | None,
        titulo: str,
        descricao: str,
        prioridade: Priority,
        prazo: datetime,
        status: Status = Status.PENDENTE,
    ):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.status = status

    def validar(self):
        if not self.titulo or len(self.titulo) < 3:
            raise ValueError("Título deve ter pelo menos 3 caracteres.")
        if self.prazo and self.prazo < datetime.now():
            raise ValueError("Prazo não pode estar no passado.")