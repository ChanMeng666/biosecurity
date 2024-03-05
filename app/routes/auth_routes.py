from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from ..database.db_connection import get_db_connection
import re

auth_bp = Blueprint('auth', __name__, template_folder='../templates')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
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
            session['username'] = username  # Store the username in the session.
            session['role'] = user_record[2]
            # Close the cursor after we are done using it before any redirects.
            cursor.close()

            if session['role'] == 'agronomist':
                connection.close()
                return redirect(url_for('agronomist.agronomist_home'))


            elif session['role'] == 'staff':
                connection.close()
                return redirect(url_for('staff.staff_home'))


            elif session['role'] == 'administrator':
                connection = get_db_connection()
                cursor = connection.cursor(prepared=True)

                # Fetch additional info about user
                admin_info_sql = "SELECT first_name, last_name, email, work_phone_number, hire_date, position, department FROM staff_and_administrators WHERE user_id=%s"
                cursor.execute(admin_info_sql, (session['user_id'],))
                admin_info = cursor.fetchone()
                session['admin_info'] = admin_info
                cursor.close()
                connection.close()
                return redirect(url_for('admin.admin_home'))
        else:
            cursor.close()
            connection.close()
            error = 'Invalid username or password. Please try again.'

    return render_template('login.html', error=error)



@auth_bp.route('/logout')
def logout():
    # Clear all data in the session to log out the user.
    session.clear()
    return redirect(url_for('auth.login'))



@auth_bp.route('/sources')
def sources():
    return render_template('sources.html')




# Function to check password complexity
def is_password_complex(password):
    complexity_check = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).{8,}$')
    return complexity_check.match(password)





@auth_bp.route('/register/agronomist', methods=['GET', 'POST'])
def register_agronomist():
    if request.method == 'POST':
        # Extract data from form
        form_data = {
            'username': request.form['username'],
            'password': request.form['password'],
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'phone_number': request.form['phone'],
            'address': request.form['address'],
        }

        # Check password complexity
        # password_complexity_regex = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z\d]).{8,}$')
        if not is_password_complex(form_data['password']):
            flash('Password must contain at least 8 characters, including uppercase and lowercase letters, numbers, and special characters.', 'danger')
            return render_template('register_for_agronomist.html', form_data=form_data)


        # Check username availability
        connection = get_db_connection()
        cursor = connection.cursor(prepared=True)
        cursor.execute('SELECT * FROM users WHERE username = %s', (form_data['username'],))
        existing_user = cursor.fetchone()
        if existing_user:
            flash('Username already exists. Please choose a different username.', 'danger')
            cursor.close()
            connection.close()
            return render_template('register_for_agronomist.html', form_data=form_data)

        # Hash password and store new user
        hashed_pwd = generate_password_hash(form_data['password'])
        insert_user_sql = (
            'INSERT INTO users (username, password_hash, role_name, status) '
            'VALUES (%s, %s, %s, %s)'
        )
        cursor.execute(insert_user_sql, (form_data['username'], hashed_pwd, 'agronomist', 'active'))
        user_id = cursor.lastrowid

        # Add the agronomist specific details to the agronomists table
        insert_agronomist_sql = (
            'INSERT INTO agronomists (user_id, first_name, last_name, email, phone_number, address, date_joined) '
            'VALUES (%s, %s, %s, %s, %s, %s, CURDATE())'
        )
        cursor.execute(insert_agronomist_sql, (user_id, form_data['first_name'], form_data['last_name'], form_data['email'], form_data['phone_number'], form_data['address']))

        # Commit changes and close connection
        connection.commit()
        cursor.close()
        connection.close()

        flash('Congratulations! Registration successful.', 'success')

        return render_template('register_for_agronomist.html', form_data=form_data)

    return render_template('register_for_agronomist.html', form_data=None)


@auth_bp.route('/register/admin', methods=['GET', 'POST'])
def register_admin():
    if request.method == 'POST':
        # Extract data from form
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

        # Check password complexity
        # password_complexity_regex = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z\d]).{8,}$')
        if not is_password_complex(form_data['password']):
            flash('Password must contain at least 8 characters, including uppercase and lowercase letters, numbers, and special characters.', 'danger')
            return render_template('register_for_admin.html', form_data=form_data)

        # Check username availability
        connection = get_db_connection()
        cursor = connection.cursor(prepared=True)
        cursor.execute('SELECT * FROM users WHERE username = %s', (form_data['username'],))
        existing_user = cursor.fetchone()
        if existing_user:
            flash('Username already exists. Please choose a different username.', 'danger')
            cursor.close()
            connection.close()
            return render_template('register_for_admin.html', form_data=form_data)

        # Hash password and store new user
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

        flash('Congratulations! Registration successful.', 'success')

        return render_template('register_for_admin.html', form_data=form_data)

    return render_template('register_for_admin.html', form_data=None)



@auth_bp.route('/register/staff', methods=['GET', 'POST'])
def register_staff():
    if request.method == 'POST':
        # Extract data from form
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

        # Check password complexity
        # password_complexity_regex = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z\d]).{8,}$')
        if not is_password_complex(form_data['password']):
            flash('Password must contain at least 8 characters, including uppercase and lowercase letters, numbers, and special characters.', 'danger')
            return render_template('register_for_staff.html', form_data=form_data)


        # Check username availability
        connection = get_db_connection()
        cursor = connection.cursor(prepared=True)
        cursor.execute('SELECT * FROM users WHERE username = %s', (form_data['username'],))
        existing_user = cursor.fetchone()
        if existing_user:
            flash('Username already exists. Please choose a different username.', 'danger')
            cursor.close()
            connection.close()
            return render_template('register_for_staff.html', form_data=form_data)

        # Hash password and store new user
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

        flash('Congratulations! Registration successful.', 'success')

        return render_template('register_for_staff.html', form_data=form_data)

    return render_template('register_for_staff.html', form_data=None)


@auth_bp.route('/update_user_info', methods=['POST'])
def update_user_info():
    data = request.json
    field = data.get('field')
    new_value = data.get('value')
    user_id = session.get('user_id')

    if not user_id:
        return jsonify(success=False, message="Unauthorized access."), 401

    connection = get_db_connection()
    cursor = connection.cursor(prepared=True)

    try:
        # Replace 'password' field with 'password_hash'
        if field == 'password':
            field = 'password_hash'

            # Check password complexity before proceeding
            if not is_password_complex(new_value):
                return jsonify(success=False, message="Password does not meet complexity requirements."), 422

            # Hash the new password
            new_value = generate_password_hash(new_value)

        # Check for unique username if the username field is being updated
        if field == "username":
            cursor.execute("SELECT user_id FROM users WHERE username = %s", (new_value,))
            if cursor.fetchone():
                return jsonify(success=False, message="Username is already taken"), 409

        # Construct the update query dynamically based on the field
        update_query = f"UPDATE users SET {field} = %s WHERE user_id = %s" if field in ['username',
                                                                                        'password_hash'] else "UPDATE staff_and_administrators SET " + field + " = %s WHERE user_id = %s"

        cursor.execute(update_query, (new_value, user_id))
        connection.commit()
        return jsonify(success=True)

    except Exception as e:
        # Proper logging should replace the print statement
        print(f"An error occurred: {e}")
        return jsonify(success=False, message="Update failed due to server error."), 500

    finally:
        cursor.close()
        connection.close()