from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
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
        cursor.close()
        connection.close()
        if user_record and check_password_hash(user_record[1], password):
            if user_record[2] == 'agronomist':
                return redirect(url_for('agronomist.agronomist_home'))
            elif user_record[2] == 'staff':
                return redirect(url_for('staff.staff_home'))
            elif user_record[2] == 'administrator':
                return redirect(url_for('admin.admin_home'))
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)


@auth_bp.route('/sources')
def sources():
    return render_template('sources.html')


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
        password_complexity_regex = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z\d]).{8,}$')
        if not password_complexity_regex.match(form_data['password']):
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

        # flash('Congratulations! Registration successful.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register_for_agronomist.html', form_data=None)

@auth_bp.route('/register/admin')
def register_admin():
    return render_template('register_for_admin.html')


@auth_bp.route('/register/staff')
def register_staff():
    return render_template('register_for_staff.html')