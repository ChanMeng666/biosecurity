from flask import Blueprint, render_template, session, redirect, url_for, request, flash, jsonify
from app.database.db_connection import get_db_connection
from mysql.connector import errors as mysql_errors
import re
from werkzeug.security import generate_password_hash

admin_bp = Blueprint('admin', __name__, template_folder='../templates/admin')


def is_password_complex(password):
    complexity_check = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).{8,}$')
    return complexity_check.match(password)

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
    # search_value = None
    search_value = ''

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



    selected_staff_id = request.args.get('selected_staff_id', type=int)
    edit_staff = None
    if selected_staff_id:
        try:
            cursor.execute("""
                SELECT * FROM staff_and_administrators WHERE user_id = %s
            """, (selected_staff_id,))
            edit_staff = cursor.fetchone()
        except mysql_errors.Error as e:
            flash(f'Error retrieving staff information: {e}', 'danger')

    # 处理编辑员工信息的逻辑
    if request.method == 'POST' and 'edit_staff_id' in request.form:
        user_id = request.form['edit_staff_id']
        return redirect(url_for('admin.edit_staff', user_id=user_id))


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

    return render_template('admin/admin_manage_staff.html', staff_list=staff_list, page=page, total_pages=total_pages, search_field=search_field, search_value=search_value, edit_staff=edit_staff, selected_staff_id=selected_staff_id)

@admin_bp.route('/delete-staff', methods=['POST'])
def delete_staff():
    if 'admin_info' not in session:
        return redirect(url_for('auth.login'))

    # 从表单中获取员工ID
    staff_id = request.form.get('delete_staff_id')
    if staff_id:
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            # 删除staff_and_administrators表中的记录
            cursor.execute("DELETE FROM staff_and_administrators WHERE user_id = %s", (staff_id,))
            # 删除users表中的记录
            cursor.execute("DELETE FROM users WHERE user_id = %s", (staff_id,))
            connection.commit()
            cursor.close()
            connection.close()
            flash('Staff member deleted successfully.', 'success')
        except mysql_errors.Error as e:
            flash(f'Error deleting staff member: {e}', 'danger')
            return redirect(url_for('admin.admin_manage_staff'))

    return redirect(url_for('admin.admin_manage_staff'))


@admin_bp.route('/admin/add-staff', methods=['POST'])
def admin_add_staff():
    if 'admin_info' not in session:
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('admin.admin_manage_staff'))

    form_data = {
        'username': request.form.get('username'),
        'password': request.form.get('password'),
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'email': request.form.get('email'),
        'phone': request.form.get('phone'),
        'position': request.form.get('position'),
        'department': request.form.get('department')
    }

    if not is_password_complex(form_data['password']):
        flash('Password must contain at least 8 characters, including uppercase and lowercase letters, numbers, and special characters.', 'danger')
        return redirect(url_for('admin.admin_manage_staff', form_data=form_data))

    # Hash the password
    password_hash = generate_password_hash(form_data['password'])


    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username = %s", (form_data['username'],))
        if cursor.fetchone():
            flash('Username already taken. Choose a different one.', 'danger')
            return redirect(url_for('admin.admin_manage_staff', form_data=form_data))

        # Insert new user with hashed password
        cursor.execute("INSERT INTO users (username, password_hash, role_name) VALUES (%s, %s, 'staff')", (form_data['username'], password_hash))
        user_id = cursor.lastrowid

        # Insert staff details
        cursor.execute("""
                INSERT INTO staff_and_administrators (
                    user_id, first_name, last_name, email, work_phone_number, hire_date, position, department
                ) VALUES (%s, %s, %s, %s, %s, CURDATE(), %s, %s)
            """, (user_id, form_data['first_name'], form_data['last_name'], form_data['email'], form_data['phone'],
                  form_data['position'], form_data['department']))

        connection.commit()
        flash('Staff member added successfully.', 'success')
        return redirect(url_for('admin.admin_manage_staff'))

    except mysql_errors.Error as e:
        connection.rollback()
        flash(f'Error adding staff member: {e}', 'danger')
        return redirect(url_for('admin.admin_manage_staff', form_data=form_data))

    finally:
        cursor.close()
        connection.close()


@admin_bp.route('/edit-staff/<int:user_id>', methods=['GET', 'POST'])
def edit_staff(user_id):
    if 'admin_info' not in session:
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('auth.login'))

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if request.method == 'POST':
        # Extract form data
        username = request.form['edit_staff_username']
        password = request.form['edit_staff_password']
        first_name = request.form['edit_staff_first_name']
        last_name = request.form['edit_staff_last_name']
        email = request.form['edit_staff_email']
        phone = request.form['edit_staff_phone']
        hire_date = request.form['edit_staff_hire_date']
        position = request.form['edit_staff_position']
        department = request.form['edit_staff_department']

        # Update staff information
        try:
            if password:  # If password is provided, update it
                password_hash = generate_password_hash(password)
                cursor.execute("""
                    UPDATE users SET username = %s, password_hash = %s
                    WHERE user_id = %s
                """, (username, password_hash, user_id))
            else:  # If password is not provided, do not update it
                cursor.execute("""
                    UPDATE users SET username = %s
                    WHERE user_id = %s
                """, (username, user_id))

            cursor.execute("""
                UPDATE staff_and_administrators SET
                first_name = %s, last_name = %s, email = %s,
                work_phone_number = %s, hire_date = %s,
                position = %s, department = %s
                WHERE user_id = %s
            """, (first_name, last_name, email, phone, hire_date, position, department, user_id))

            connection.commit()
            flash('Staff updated successfully.', 'success')
        except mysql_errors.Error as e:
            connection.rollback()
            flash(f'Error updating staff: {e}', 'danger')
        finally:
            cursor.close()
            connection.close()

        return redirect(url_for('admin.edit_staff', user_id=user_id))

    # GET request: fetch current staff information
    try:
        cursor.execute("""
            SELECT u.username, s.first_name, s.last_name, s.email,
            s.work_phone_number, s.hire_date, s.position, s.department
            FROM users u
            JOIN staff_and_administrators s ON u.user_id = s.user_id
            WHERE u.user_id = %s
        """, (user_id,))
        staff = cursor.fetchone()
    finally:
        cursor.close()
        connection.close()

    return render_template('admin/admin_manage_staff.html', edit_staff=staff, user_id=user_id)


@admin_bp.route('/admin/manage-agronomist')
def admin_manage_agronomist():

    return render_template('admin/admin_manage_agronomist.html')

@admin_bp.route('/admin/manage-guide')
def admin_manage_guide():

    return render_template('admin/admin_manage_guide.html')