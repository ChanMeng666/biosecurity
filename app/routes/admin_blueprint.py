from flask import Blueprint
import re

admin_bp = Blueprint('admin', __name__, template_folder='../templates/admin')

def is_password_complex(password):
    complexity_check = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).{8,}$')
    return complexity_check.match(password)