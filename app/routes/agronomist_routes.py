from flask import Blueprint, render_template

agronomist_bp = Blueprint('agronomist', __name__, template_folder='../templates/agronomist')

@agronomist_bp.route('/home')  # The URL path for the home route.
def agronomist_home():  # The name of this function determines the endpoint by default, which would be 'admin.admin_home' because it's within the 'admin' Blueprint.
    return render_template('agronomist/agronomist_home.html')

