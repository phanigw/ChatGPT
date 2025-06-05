import sqlite3

DB_NAME = 'todo.db'

class ToDoService:
    def __init__(self, db_name: str = DB_NAME):
        self.db_name = db_name

    def init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS todos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            due_date TEXT,
                            status TEXT NOT NULL
                        )''')
            conn.commit()

    def add_todo(self, title: str, due_date: str):
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            query = ("INSERT INTO todos (title, due_date, status) " 
                "VALUES (?, ?, ?)")
            c.execute(query, (title, due_date, 'pending'))
            conn.commit()

    def get_all_todos(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('SELECT id, title, due_date, status FROM todos')
            return c.fetchall()

    def complete_todo(self, todo_id: int):
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            query = 'UPDATE todos SET status = ? WHERE id = ?'
            c.execute(query, ('completed', todo_id))
            conn.commit()
