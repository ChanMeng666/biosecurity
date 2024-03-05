from flask import Blueprint, render_template

staff_bp = Blueprint('staff', __name__, template_folder='../templates/staff')

@staff_bp.route('/home')
def staff_home():
    return render_template('staff/staff_home.html')
