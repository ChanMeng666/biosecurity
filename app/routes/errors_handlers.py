from flask import Blueprint, render_template

errors_bp = Blueprint('errors', __name__, template_folder='../templates/errors')

@errors_bp.route('/')
def errors_index():
    return render_template('errors/errors_home.html')