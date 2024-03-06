from flask import Blueprint, render_template, session, redirect, url_for

admin_bp = Blueprint('admin', __name__, template_folder='../templates/admin')

@admin_bp.route('/home')
def admin_home():
    if 'admin_info' in session:
        admin_info = session['admin_info']
        return render_template('admin/admin_home.html', admin_info=admin_info)
    else:
        return redirect(url_for('errors.errors_index'))