from .auth_blueprint import auth_bp, render_toast
from flask import request, jsonify, render_template
from werkzeug.security import generate_password_hash
from ..database.db_connection import get_db_connection
from .auth_blueprint import is_password_complex

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

