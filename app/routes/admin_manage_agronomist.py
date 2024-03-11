from .admin_blueprint import admin_bp
from flask import render_template
@admin_bp.route('/admin/manage-agronomist')
def admin_manage_agronomist():

    return render_template('admin/admin_manage_agronomist.html')
