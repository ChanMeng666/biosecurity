from flask import url_for

def get_home_url_by_role(role):
    if role == 'administrator':
        return url_for('admin.admin_home')
    elif role == 'staff':
        return url_for('staff.staff_home')
    elif role == 'agronomist':
        return url_for('agronomist.agronomist_home')
    else:
        return url_for('auth.login')