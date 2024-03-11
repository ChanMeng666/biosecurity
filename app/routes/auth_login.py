from .auth_blueprint import auth_bp, render_toast
from flask import request, session, jsonify, render_template, url_for
from werkzeug.security import check_password_hash
from ..database.db_connection import get_db_connection

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    global redirect_url
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        connection = get_db_connection()
        cursor = connection.cursor(prepared=True)
        sql = "SELECT user_id, password_hash, role_name FROM users WHERE status='active' AND username=%s"
        cursor.execute(sql, (username,))
        user_record = cursor.fetchone()

        if user_record and check_password_hash(user_record[1], password):

            session['user_id'] = user_record[0]
            session['username'] = username
            session['role'] = user_record[2]
            cursor.close()

            if session['role'] == 'agronomist':
                redirect_url = url_for('agronomist.agronomist_home')

                connection = get_db_connection()
                cursor = connection.cursor(prepared=True)

                agronomist_info_sql = "SELECT first_name, last_name, email, phone_number, address, date_joined FROM agronomists WHERE user_id=%s"
                cursor.execute(agronomist_info_sql, (session['user_id'],))
                agronomist_info = cursor.fetchone()
                session['agronomist_info'] = agronomist_info
                cursor.close()
                connection.close()


            elif session['role'] == 'staff':
                redirect_url = url_for('staff.staff_home')

                connection = get_db_connection()
                cursor = connection.cursor(prepared=True)

                staff_info_sql = "SELECT first_name, last_name, email, work_phone_number, hire_date, position, department FROM staff_and_administrators WHERE user_id=%s"
                cursor.execute(staff_info_sql, (session['user_id'],))
                staff_info = cursor.fetchone()
                session['staff_info'] = staff_info
                cursor.close()
                connection.close()


            elif session['role'] == 'administrator':
                redirect_url = url_for('admin.admin_home')

                connection = get_db_connection()
                cursor = connection.cursor(prepared=True)

                admin_info_sql = "SELECT first_name, last_name, email, work_phone_number, hire_date, position, department FROM staff_and_administrators WHERE user_id=%s"
                cursor.execute(admin_info_sql, (session['user_id'],))
                admin_info = cursor.fetchone()
                session['admin_info'] = admin_info
                cursor.close()
                connection.close()

            # Return a JSON response with the redirect URL
            return jsonify(success=True, redirect_url=redirect_url)

        else:
            cursor.close()
            connection.close()

            toast = render_toast('danger', 'Invalid username or password. Please try again.')
            return jsonify(success=False, toast=toast), 401

    return render_template('login.html')
