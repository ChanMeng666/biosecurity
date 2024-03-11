from flask import Blueprint, render_template
import re

auth_bp = Blueprint('auth', __name__, template_folder='../templates')

def render_toast(type, message):
    return {'type': type, 'message': message}


def is_password_complex(password):
    complexity_check = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).{8,}$')
    return complexity_check.match(password)

@auth_bp.route('/sources')
def sources():
    return render_template('sources.html')