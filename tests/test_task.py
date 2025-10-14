import pytest
from datetime import datetime, timedelta
from task_manager.task import Task, Priority

def test_task_valida_deve_ser_criada_com_sucesso():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(id=None, titulo="Estudar Python", descricao="Aprofundar em testes", prioridade=Priority.ALTA, prazo=prazo)
    
    task.validar()
    
    assert task.titulo == "Estudar Python"

def test_task_com_titulo_invalido_deve_lancar_valueerror():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(id=None, titulo="AB", descricao="Desc", prioridade=Priority.BAIXA, prazo=prazo)
    
    with pytest.raises(ValueError, match="Título deve ter pelo menos 3 caracteres."):
        task.validar()

def test_task_com_prazo_no_passado_deve_lancar_valueerror():
    prazo_passado = datetime.now() - timedelta(days=1)
    task = Task(id=None, titulo="Tarefa Vencida", descricao="Desc", prioridade=Priority.MEDIA, prazo=prazo_passado)
    
    with pytest.raises(ValueError, match="Prazo não pode estar no passado."):
        task.validar()