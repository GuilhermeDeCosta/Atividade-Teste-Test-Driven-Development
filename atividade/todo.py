import uuid
from typing import Dict, List, Optional

class Task:
    def __init__(self, name: str, description: str):
        if not name or not name.strip():
            raise ValueError("Nome da tarefa não pode ser vazio.")
        self.id = str(uuid.uuid4())
        self.name = name.strip()
        self.description = description.strip() if description is not None else ""
        self.status = "pending"

    def mark_completed(self) -> bool:
        if self.status == "completed":
            return False
        self.status = "completed"
        return True

    def mark_in_progress(self) -> bool:
        if self.status == "completed":
            return False
        if self.status == "in_progress":
            return False
        self.status = "in_progress"
        return True

    def edit(self, new_name: Optional[str], new_description: Optional[str]) -> None:
        if new_name is not None:
            if not new_name.strip():
                raise ValueError("Nome da tarefa não pode ser vazio.")
            self.name = new_name.strip()
        if new_description is not None:
            self.description = new_description.strip()

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "status": self.status
        }


class TodoList:
    def __init__(self):
        self._tasks: Dict[str, Task] = {}

    def add_task(self, name: str, description: str) -> Task:
        task = Task(name, description)
        self._tasks[task.id] = task
        return task

    def get_task(self, task_id: str) -> Task:
        try:
            return self._tasks[task_id]
        except KeyError:
            raise KeyError(f"Tarefa com id {task_id} não encontrada.")

    def edit_task(self, task_id: str, new_name: Optional[str], new_description: Optional[str]) -> None:
        task = self.get_task(task_id)
        task.edit(new_name, new_description)

    def delete_task(self, task_id: str) -> None:
        if task_id not in self._tasks:
            raise KeyError(f"Tarefa com id {task_id} não encontrada.")
        del self._tasks[task_id]

    def mark_task_completed(self, task_id: str) -> bool:
        task = self.get_task(task_id)
        return task.mark_completed()

    def mark_task_in_progress(self, task_id: str) -> bool:
        task = self.get_task(task_id)
        return task.mark_in_progress()

    def list_tasks(self) -> List[Dict]:
        return [t.to_dict() for t in self._tasks.values()]
