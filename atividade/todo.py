class Task:
    def __init__(self, name, description):
        if not name or not name.strip():
            raise ValueError("O nome da tarefa não pode ser vazio.")
        self.name = name.strip()
        self.description = description.strip() if description else ""
        self.status = "pending"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description):
        task = Task(name, description)
        self.tasks.append(task)
        return task
