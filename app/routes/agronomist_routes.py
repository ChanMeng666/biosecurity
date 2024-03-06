from flask import Blueprint, render_template, session, redirect, url_for

agronomist_bp = Blueprint('agronomist', __name__, template_folder='../templates/agronomist')

@agronomist_bp.route('/home')  # The URL path for the home route.
def agronomist_home():  # The name of this function determines the endpoint by default, which would be 'admin.admin_home' because it's within the 'admin' Blueprint.
    if 'agronomist_info' in session:
        agronomist_info = session['agronomist_info']
        return render_template('agronomist/agronomist_home.html', agronomist_info=agronomist_info)
    else:
        return redirect(url_for('errors.errors_index'))