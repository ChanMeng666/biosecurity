from flask import Blueprint, render_template, session, redirect, url_for, request, flash, jsonify
from app.database.db_connection import get_db_connection
from mysql.connector import errors as mysql_errors

admin_bp = Blueprint('admin', __name__, template_folder='../templates/admin')


@admin_bp.route('/home')
def admin_home():
    if 'admin_info' in session:
        admin_info = session['admin_info']
        return render_template('admin/admin_home.html', admin_info=admin_info)
    else:
        return redirect(url_for('errors.errors_index'))



@admin_bp.route('/admin/manage-staff', methods=['GET', 'POST'])
def admin_manage_staff():
    if 'admin_info' not in session:
        return redirect(url_for('errors.errors_index'))

    page = request.args.get('page', 1, type=int)
    per_page = 10
    search_field = None
    search_value = None

    if request.method == 'POST':
        search_field = request.form.get('choose_staff')
        search_value = request.form.get('input_staff')
        if search_field == 'Choose...':
            search_field = None

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    where_clause = ""
    params = []

    if search_field and search_value:
        if search_field in ['user_id', 'username']:
            where_clause = f" AND u.{search_field} LIKE %s"
        else:
            where_clause = f" AND s.{search_field} LIKE %s"
        params.append(f"%{search_value}%")

    # Fetch total number of records for pagination
    total_query = f"""
        SELECT COUNT(*) FROM users u
        JOIN staff_and_administrators s ON u.user_id = s.user_id
        WHERE u.role_name = 'staff'{where_clause}
    """
    cursor.execute(total_query, params)
    total_records = cursor.fetchone()['COUNT(*)']

    # Calculate the starting point for the rows to fetch
    starting_point = (page - 1) * per_page

    # Fetch the records for the current page
    staff_query = f"""
        SELECT u.user_id, u.username, u.role_name, s.staff_number, s.first_name, s.last_name, 
        s.email, s.work_phone_number, s.hire_date, s.position, s.department
        FROM users u
        JOIN staff_and_administrators s ON u.user_id = s.user_id
        WHERE u.role_name = 'staff'{where_clause}
        LIMIT %s OFFSET %s
    """
    cursor.execute(staff_query, params + [per_page, starting_point])

    staff_list = cursor.fetchall()
    cursor.close()
    connection.close()

    # Calculate total pages
    total_pages = (total_records + per_page - 1) // per_page

    return render_template('admin/admin_manage_staff.html', staff_list=staff_list, page=page, total_pages=total_pages, search_field=search_field, search_value=search_value)


@admin_bp.route('/admin/manage-agronomist')
def admin_manage_agronomist():

    return render_template('admin/admin_manage_agronomist.html')

@admin_bp.route('/admin/manage-guide')
def admin_manage_guide():

    return render_template('admin/admin_manage_guide.html')