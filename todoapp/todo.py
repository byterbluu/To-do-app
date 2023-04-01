from flask import Blueprint, render_template, request, redirect, url_for, g

from todoapp.auth import login_required

from .models import Tododb, User
from todoapp import db

bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/list')
@login_required
def index():
    todos = Tododb.query.all()
    return render_template('todo/index.html', todos = todos)

#CREATE A NEW TASK

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']

        todo = Tododb(g.user.id, title, desc)

        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/create.html')


#UPDATE A TASK

def get_todo(id):
    todo = Tododb.query.get_or_404(id)
    return todo 

#view of update

@bp.route('/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
     
    todo = get_todo(id)

    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        todo.status = True if request.form.get('status') == 'on' else False

        db.session.commit()
        return redirect(url_for('todo.index'))
     
    return render_template('todo/update.html', todo = todo)


#DELETE A TASK

@bp.route('/delete/<int:id>')
@login_required
def delete(id):
    todo = get_todo(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('todo.index'))
