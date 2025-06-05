from flask import Flask, render_template, request, redirect, url_for
from service import ToDoService

app = Flask(__name__)
service = ToDoService()

@app.route('/')
def index():
    todos = service.get_all_todos()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form['title']
    due_date = request.form['due_date']
    service.add_todo(title, due_date)
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>')
def complete_todo(todo_id):
    service.complete_todo(todo_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    service.init_db()
    app.run(debug=True)
