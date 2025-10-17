import unittest
from todo import TodoList

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.td = TodoList()

    def test_add_task_success(self):
        task = self.td.add_task("Comprar pão", "Ir à padaria")
        self.assertEqual(task.name, "Comprar pão")
        self.assertEqual(task.description, "Ir à padaria")
        self.assertEqual(task.status, "pending")

    def test_add_task_empty_name_raises(self):
        with self.assertRaises(ValueError):
            self.td.add_task("", "Descrição qualquer")

if __name__ == "__main__":
    unittest.main()
