from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from forms import TodoForm, UpdateTodoForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from models import Todo

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TodoForm()
    if form.validate_on_submit():
        todo = Todo(description=form.description.data)
        db.session.add(todo)
        db.session.commit()
        flash('Todo added!', 'success')
        return redirect(url_for('index'))
    todos = Todo.query.all()
    return render_template('index.html', todos=todos, form=form)

@app.route('/update/<int:todo_id>', methods=['GET', 'POST'])
def update_todo(todo_id):
    form = UpdateTodoForm()
    todo = Todo.query.get_or_404(todo_id)
    if form.validate_on_submit():
        todo.description = form.description.data
        db.session.commit()
        flash('Todo updated!', 'success')
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.description.data = todo.description
    return render_template('update.html', form=form, todo=todo)


@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    flash('Todo deleted!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
