# 💻 第三层 - 代码实现结果

生成时间: 2025-09-27 18:39:33

---

1. `src/models/task.py`
```python
# filepath: src/models/task.py
from enum import Enum

class TaskStatus(Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'

class Task:
    def __init__(self, description: str, status: TaskStatus = TaskStatus.PENDING) -> None:
        self.description = description
        self.status = status

    def mark_as_completed(self) -> None:
        self.status = TaskStatus.COMPLETED

    def __str__(self) -> str:
        return f"{self.description} - {self.status.value}"
```

2. `src/services/task_service.py`
```python
# filepath: src/services/task_service.py
from src.models import Task

class TaskService:
    def __init__(self):
        self.tasks = []

    def add_task(self, description: str) -> str:
        new_task = Task(description)
        self.tasks.append(new_task)
        return f"Task added: {new_task}"

    def delete_task(self, task_id: int) -> str:
        if 0 <= task_id < len(self.tasks):
            deleted_task = self.tasks.pop(task_id)
            return f"Task deleted: {deleted_task}"
        else:
            return "Task not found"

    def mark_task_as_completed(self, task_id: int) -> str:
        if 0 <= task_id < len(self.tasks):
            task = self.tasks[task_id]
            task.mark_as_completed()
            return f"Task marked as completed: {task}"
        else:
            return "Task not found"
```

3. `src/main.py`
```python
# filepath: src/main.py
from src.services import task_service

def main():
    task_service = task_service.TaskService()
    
    print(task_service.add_task("Buy groceries"))
    print(task_service.add_task("Finish project report"))
    
    print(task_service.mark_task_as_completed(0))
    
    print(task_service.delete_task(1))
    
    print(task_service.add_task("Read a book"))
    print(task_service.mark_task_as_completed(0))

if __name__ == "__main__":
    main()
```

4. `tests/test_models.py`
```python
# filepath: tests/test_models.py
from src.models import Task, TaskStatus

def test_task_creation():
    task = Task("Buy groceries")
    assert str(task) == "Buy groceries - pending"

def test_mark_task_as_completed():
    task = Task("Finish project report")
    task.mark_as_completed()
    assert str(task) == "Finish project report - completed"
```

5. `tests/test_services.py`
```python
# filepath: tests/test_services.py
from src.services import task_service
from src.models import Task

def test_add_task():
    task_service = task_service.TaskService()
    task = Task("Buy groceries")
    task_service.tasks.append(task)
    assert len(task_service.tasks) == 1

def test_delete_task():
    task_service = task_service.TaskService()
    task_service.tasks.append(Task("Buy groceries"))
    assert task_service.delete_task(0) == "Task deleted: Buy groceries - pending"

def test_mark_task_as_completed():
    task_service = task_service.TaskService()
    task_service.tasks.append(Task("Buy groceries"))
    task = task_service.tasks[0]
    task.mark_as_completed()
    assert str(task) == "Buy groceries - completed"
```

6. `config/settings.py`
```python
# filepath: config/settings.py
TODO_STORAGE = "memory"
TODO_USER_INTERFACE = "command_line"
```

7. `requirements.txt`
```plaintext
# filepath: requirements.txt
# No additional dependencies needed for this simple application
```
``` ```python
# filepath: src/models/task.py
from enum import Enum

class TaskStatus(Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'

class Task:
    def __init__(self, description: str, status: TaskStatus = TaskStatus.PENDING) -> None:
        self.description = description
        self.status = status

    def mark_as_completed(self) -> None:
        self.status = TaskStatus.COMPLETED

    def __str__(self) -> str:
        return f"{self.description} - {self.status.value}"
```

```python
# filepath: src/services/task_service.py
from src.models import Task

class TaskService:
    def __init__(self):
        self.tasks = []

    def add_task(self, description: str) -> str:
        new_task = Task(description)
        self.tasks.append(new_task)
        return f"Task added: {new_task}"

    def delete_task(self, task_id: int) -> str:
        if 0 <= task_id < len(self.tasks):
            deleted_task = self.tasks.pop(task_id)
            return f"Task deleted: {deleted_task}"
        else:
            return "Task not found"

    def mark_task_as_completed(self, task_id: int) -> str:
        if 0 <= task_id < len(self.tasks):
            task = self.tasks[task_id]
            task.mark_as_completed()
            return f"Task marked as completed: {task}"
        else:
            return "Task not found"
```

```python
# filepath: src/main.py
from src.services import task_service

def main():
    task_service = task_service.TaskService()
    
    print(task_service.add_task("Buy groceries"))
    print(task_service.add_task("Finish project report"))
    
    print(task_service.mark_task_as_completed(0))
    
    print(task_service.delete_task(1))
    
    print(task_service.add_task("Read a book"))
    print(task_service.mark_task_as_completed(0))

if __name__ == "__main__":
    main()
```

```python
# filepath: tests/test_models.py
from src.models import Task, TaskStatus

def test_task_creation():
    task = Task("Buy groceries")
    assert str(task) == "Buy groceries - pending"

def test_mark_task_as_completed():
    task = Task("Finish project report")
    task.mark_as_completed()
    assert str(task) == "Finish project report - completed"
```

```python
# filepath: tests/test_services.py
from src.services import task_service
from src.models import Task

def test_add_task():
    task_service = task_service.TaskService()
    task = Task("Buy groceries")
    task_service.tasks.append(task)
    assert len(task_service.tasks) == 1

def test_delete_task():
    task_service = task_service.TaskService()
    task_service.tasks.append(Task("Buy groceries"))
    assert task_service.delete_task(0) == "Task deleted: Buy groceries - pending"

def test_mark_task_as_completed():
    task_service = task_service.TaskService()
    task_service.tasks.append(Task("Buy groceries"))
    task = task_service.tasks[0]
    task.mark_as_completed()
    assert str(task) == "Buy groceries - completed"
```

```python
# filepath: config/settings.py
TODO_STORAGE = "memory"
TODO_USER_INTERFACE = "command_line"
```

```plaintext
# filepath: requirements.txt
# No additional dependencies needed for this simple application
```
```
