import unittest
from todo import TodoList, Task
import uuid

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.td = TodoList()

    def test_add_task_success(self):
        task = self.td.add_task("Comprar leite", "Ir ao mercado comprar leite")
        self.assertIsNotNone(task.id)
        self.assertEqual(task.name, "Comprar leite")
        self.assertEqual(task.description, "Ir ao mercado comprar leite")
        self.assertEqual(task.status, "pending")

    def test_add_task_empty_name_raises(self):
        with self.assertRaises(ValueError):
            self.td.add_task("", "descricao qualquer")

    def test_mark_task_completed(self):
        task = self.td.add_task("Tarefa", "desc")
        changed = self.td.mark_task_completed(task.id)
        self.assertTrue(changed)
        self.assertEqual(self.td.get_task(task.id).status, "completed")

    def test_mark_task_completed_again_no_change(self):
        task = self.td.add_task("Tarefa2", "desc")
        self.td.mark_task_completed(task.id)
        changed = self.td.mark_task_completed(task.id)  
        self.assertFalse(changed)
        self.assertEqual(self.td.get_task(task.id).status, "completed")

    def test_mark_task_in_progress(self):
        task = self.td.add_task("Tarefa3", "desc")
        changed = self.td.mark_task_in_progress(task.id)
        self.assertTrue(changed)
        self.assertEqual(self.td.get_task(task.id).status, "in_progress")

    def test_mark_in_progress_on_completed_returns_false(self):
        task = self.td.add_task("Tarefa4", "desc")
        self.td.mark_task_completed(task.id)
        changed = self.td.mark_task_in_progress(task.id)
        self.assertFalse(changed)
        self.assertEqual(self.td.get_task(task.id).status, "completed")

    def test_edit_task_success(self):
        task = self.td.add_task("Velho nome", "Velha desc")
        self.td.edit_task(task.id, "Novo nome", "Nova desc")
        updated = self.td.get_task(task.id)
        self.assertEqual(updated.name, "Novo nome")
        self.assertEqual(updated.description, "Nova desc")

    def test_edit_nonexistent_task_raises(self):
        fake_id = str(uuid.uuid4())
        with self.assertRaises(KeyError):
            self.td.edit_task(fake_id, "x", "y")

    def test_delete_task_success(self):
        task = self.td.add_task("Remover", "desc")
        self.td.delete_task(task.id)
        with self.assertRaises(KeyError):
            self.td.get_task(task.id)

    def test_delete_nonexistent_task_raises(self):
        fake_id = str(uuid.uuid4())
        with self.assertRaises(KeyError):
            self.td.delete_task(fake_id)


if __name__ == "__main__":
    unittest.main()
