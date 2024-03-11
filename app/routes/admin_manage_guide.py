from .admin_blueprint import admin_bp
from flask import render_template

@admin_bp.route('/admin/manage-guide')
def admin_manage_guide():

    return render_template('admin/admin_manage_guide.html')