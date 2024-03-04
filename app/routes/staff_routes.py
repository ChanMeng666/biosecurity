from flask import Blueprint, render_template


staff_bp = Blueprint('staff', __name__, template_folder='../templates/staff')

@staff_bp.route('/home')  # The URL path for the home route.
def staff_home():  # The name of this function determines the endpoint by default, which would be 'admin.admin_home' because it's within the 'admin' Blueprint.
    return render_template('staff/staff_home.html')
