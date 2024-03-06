from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from ..database.db_connection import get_db_connection
import re

auth_bp = Blueprint('auth', __name__, template_folder='../templates')


def render_toast(type, message):
    return {'type': type, 'message': message}

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

@auth_bp.route('/logout')
def logout():

    session.clear()
    return redirect(url_for('auth.login'))

@auth_bp.route('/sources')
def sources():
    return render_template('sources.html')

def is_password_complex(password):
    complexity_check = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).{8,}$')
    return complexity_check.match(password)

@auth_bp.route('/register/agronomist', methods=['GET', 'POST'])
def register_agronomist():
    if request.method == 'POST':
        form_data = {
            'username': request.form['username'],
            'password': request.form['password'],
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'phone_number': request.form['phone'],
            'address': request.form['address'],
        }

        if not is_password_complex(form_data['password']):

            toast = render_toast('danger', 'Password must contain at least 8 characters, including uppercase and lowercase letters, numbers, and special characters.')
            return jsonify(success=False, form_data=form_data, toast=toast), 422

        connection = get_db_connection()
        cursor = connection.cursor(prepared=True)
        cursor.execute('SELECT * FROM users WHERE username = %s', (form_data['username'],))
        existing_user = cursor.fetchone()
        if existing_user:
            toast = render_toast('danger', 'Username already exists. Please choose a different username.')
            return jsonify(success=False, form_data=form_data, toast=toast), 409

        hashed_pwd = generate_password_hash(form_data['password'])
        insert_user_sql = (
            'INSERT INTO users (username, password_hash, role_name, status) '
            'VALUES (%s, %s, %s, %s)'
        )
        cursor.execute(insert_user_sql, (form_data['username'], hashed_pwd, 'agronomist', 'active'))
        user_id = cursor.lastrowid

        insert_agronomist_sql = (
            'INSERT INTO agronomists (user_id, first_name, last_name, email, phone_number, address, date_joined) '
            'VALUES (%s, %s, %s, %s, %s, %s, CURDATE())'
        )
        cursor.execute(insert_agronomist_sql, (user_id, form_data['first_name'], form_data['last_name'], form_data['email'], form_data['phone_number'], form_data['address']))

        connection.commit()
        cursor.close()
        connection.close()

        toast = render_toast('success', 'Congratulations! Registration successful.')
        return jsonify(success=True, form_data=form_data, toast=toast)

    return render_template('register_for_agronomist.html', form_data=None)


@auth_bp.route('/register/admin', methods=['GET', 'POST'])
def register_admin():
    if request.method == 'POST':
        form_data = {
            'username': request.form['username'],
            'password': request.form['password'],
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'work_phone_number': request.form['phone'],
            'position': request.form['position'],
            'department': request.form['department'],
        }

        if not is_password_complex(form_data['password']):

            toast = render_toast('danger', 'Password must contain at least 8 characters, including uppercase and lowercase letters, numbers, and special characters.')
            return jsonify(success=False, form_data=form_data, toast=toast), 422

        connection = get_db_connection()
        cursor = connection.cursor(prepared=True)
        cursor.execute('SELECT * FROM users WHERE username = %s', (form_data['username'],))
        existing_user = cursor.fetchone()
        if existing_user:
            toast = render_toast('danger', 'Username already exists. Please choose a different username.')
            return jsonify(success=False, form_data=form_data, toast=toast), 409


        hashed_pwd = generate_password_hash(form_data['password'])
        insert_user_sql = (
            'INSERT INTO users (username, password_hash, role_name, status) '
            'VALUES (%s, %s, %s, %s)'
        )
        cursor.execute(insert_user_sql, (form_data['username'], hashed_pwd, 'administrator', 'active'))
        user_id = cursor.lastrowid

        insert_admin_sql = (
            'INSERT INTO staff_and_administrators (user_id, first_name, last_name, email, work_phone_number, hire_date, position, department) '
            'VALUES (%s, %s, %s, %s, %s, CURDATE(), %s, %s)'
        )
        cursor.execute(insert_admin_sql, (user_id, form_data['first_name'], form_data['last_name'], form_data['email'], form_data['work_phone_number'], form_data['position'], form_data['department']))

        connection.commit()
        cursor.close()
        connection.close()

        toast = render_toast('success', 'Congratulations! Registration successful.')
        return jsonify(success=True, form_data=form_data, toast=toast)

    return render_template('register_for_admin.html', form_data=None)



@auth_bp.route('/register/staff', methods=['GET', 'POST'])
def register_staff():
    if request.method == 'POST':
        form_data = {
            'username': request.form['username'],
            'password': request.form['password'],
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'work_phone_number': request.form['phone'],
            'position': request.form['position'],
            'department': request.form['department'],
        }

        if not is_password_complex(form_data['password']):
            toast = render_toast('danger', 'Password must contain at least 8 characters, including uppercase and lowercase letters, numbers, and special characters.')
            return jsonify(success=False, form_data=form_data, toast=toast), 422

        connection = get_db_connection()
        cursor = connection.cursor(prepared=True)
        cursor.execute('SELECT * FROM users WHERE username = %s', (form_data['username'],))
        existing_user = cursor.fetchone()
        if existing_user:
            toast = render_toast('danger', 'Username already exists. Please choose a different username.')
            return jsonify(success=False, form_data=form_data, toast=toast), 409

        hashed_pwd = generate_password_hash(form_data['password'])
        insert_user_sql = (
            'INSERT INTO users (username, password_hash, role_name, status) '
            'VALUES (%s, %s, %s, %s)'
        )
        cursor.execute(insert_user_sql, (form_data['username'], hashed_pwd, 'staff', 'active'))
        user_id = cursor.lastrowid

        insert_staff_sql = (
            'INSERT INTO staff_and_administrators (user_id, first_name, last_name, email, work_phone_number, hire_date, position, department) '
            'VALUES (%s, %s, %s, %s, %s, CURDATE(), %s, %s)'
        )
        cursor.execute(insert_staff_sql, (user_id, form_data['first_name'], form_data['last_name'], form_data['email'], form_data['work_phone_number'], form_data['position'], form_data['department']))

        connection.commit()
        cursor.close()
        connection.close()

        toast = render_toast('success', 'Congratulations! Registration successful.')
        return jsonify(success=True, form_data=form_data, toast=toast)

    return render_template('register_for_staff.html', form_data=None)


@auth_bp.route('/update_user_info', methods=['POST'])
def update_user_info():
    data = request.json
    field = data.get('field')
    new_value = data.get('value')
    user_id = session.get('user_id')
    role = session.get('role')

    if not user_id:
        toast = render_toast('danger', 'Unauthorized access. Please log in.')
        return jsonify(success=False, toast=toast), 401

    connection = get_db_connection()
    cursor = connection.cursor(prepared=True)

    try:
        if field == 'password':
            field = 'password_hash'

            if not is_password_complex(new_value):
                toast = render_toast('danger', 'Password does not meet complexity requirements.')
                return jsonify(success=False, toast=toast), 422

            new_value = generate_password_hash(new_value)

        if field == "username":
            cursor.execute("SELECT user_id FROM users WHERE username = %s", (new_value,))
            if cursor.fetchone():
                toast = render_toast('success', 'Username is already taken.')
                return jsonify(success=False, toast=toast), 409



        # update_query = f"UPDATE users SET {field} = %s WHERE user_id = %s" if field in ['username',
        #                                                                                 'password_hash'] else "UPDATE staff_and_administrators SET " + field + " = %s WHERE user_id = %s"
        #
        # cursor.execute(update_query, (new_value, user_id))

        # Update logic based on role
        if role == 'agronomist':
            if field in ['phone_number', 'address']:
                update_query = f"UPDATE agronomists SET {field} = %s WHERE user_id = %s"
                cursor.execute(update_query, (new_value, user_id))
            else:
                toast = render_toast('danger', f'An error occurred: Unknown field {field}')
                return jsonify(success=False, toast=toast), 400
        else:
            if field in ['username', 'password_hash']:
                update_query = f"UPDATE users SET {field} = %s WHERE user_id = %s"
                cursor.execute(update_query, (new_value, user_id))
            else:
                update_query = f"UPDATE staff_and_administrators SET {field} = %s WHERE user_id = %s"
                cursor.execute(update_query, (new_value, user_id))





        connection.commit()
        toast = render_toast('success', 'Information updated successfully.')
        return jsonify(success=True, toast=toast)

    except Exception as e:
        print(f"An error occurred: {e}")
        toast = render_toast('error', f'An error occurred: {e}')
        return jsonify(success=False, toast=toast), 500

    finally:
        cursor.close()
        connection.close()