from flask import Blueprint, render_template, session, redirect, url_for

admin_bp = Blueprint('admin', __name__, template_folder='../templates/admin')

@admin_bp.route('/home')
def admin_home():
    if 'admin_info' in session:
        admin_info = session['admin_info']
        return render_template('admin/admin_home.html', admin_info=admin_info)
    else:
        return redirect(url_for('errors.errors_index'))

@admin_bp.route('/admin/manage-staff')
def admin_manage_staff():

    return render_template('admin/admin_manage_staff.html')

@admin_bp.route('/admin/manage-agronomist')
def admin_manage_agronomist():

    return render_template('admin/admin_manage_agronomist.html')

@admin_bp.route('/admin/manage-guide')
def admin_manage_guide():

    return render_template('admin/admin_manage_guide.html')