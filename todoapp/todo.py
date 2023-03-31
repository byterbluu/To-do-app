from flask import Blueprint

bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/list')
def index():
    return 'List of Tasks'

@bp.route('/create')
def create():
    return 'Create a Tasks'