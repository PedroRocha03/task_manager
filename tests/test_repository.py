from datetime import datetime
from task_manager.task import Task, Priority
from task_manager.repository import TaskRepository

def test_save_deve_atribuir_id_e_chamar_storage_add(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    task = Task(None, "Teste", "Desc", Priority.BAIXA, datetime.now())
    
    resultado = repo.save(task)
    
    assert resultado.id == 1
    mock_storage.add.assert_called_once_with(1, task)

def test_find_by_id_deve_chamar_storage_get(mocker):
    mock_storage = mocker.Mock()
    mock_storage.get.return_value = "Tarefa Encontrada"
    repo = TaskRepository(mock_storage)
    
    resultado = repo.find_by_id(123)
    
    mock_storage.get.assert_called_once_with(123)
    assert resultado == "Tarefa Encontrada"

def test_find_all_deve_chamar_storage_get_all(mocker):
    mock_storage = mocker.Mock()
    mock_storage.get_all.return_value = ["Tarefa 1", "Tarefa 2"]
    repo = TaskRepository(mock_storage)
    
    resultado = repo.find_all()
    
    mock_storage.get_all.assert_called_once()
    assert resultado == ["Tarefa 1", "Tarefa 2"]

def test_delete_deve_chamar_storage_delete(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    
    repo.delete(1)
    
    mock_storage.delete.assert_called_once_with(1)