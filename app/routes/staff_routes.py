from flask import Blueprint, render_template, session, redirect, url_for

staff_bp = Blueprint('staff', __name__, template_folder='../templates/staff')

@staff_bp.route('/home')
def staff_home():
    if 'staff_info' in session:
        staff_info = session['staff_info']
        return render_template('staff/staff_home.html', staff_info=staff_info)
    else:
        return redirect(url_for('errors.errors_index'))

@staff_bp.route('/staff/view-agronomist')
def staff_view_agronomist():

    return render_template('staff/staff_view_agronomist.html')

@staff_bp.route('/staff/manage-guide')
def staff_manage_guide():

    return render_template('staff/staff_manage_guide.html')