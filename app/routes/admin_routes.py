from flask import Blueprint, render_template


admin_bp = Blueprint('admin', __name__, template_folder='../templates/admin')

@admin_bp.route('/home')  # The URL path for the home route.
def admin_home():  # The name of this function determines the endpoint by default, which would be 'admin.admin_home' because it's within the 'admin' Blueprint.
    return render_template('admin/admin_home.html')


