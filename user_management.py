from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db_connection, get_cursor
from auth import validate_password
from flask import render_template, redirect, url_for
import mysql.connector
import connect

def register_user(form):
    # Initialize variables to None
    connection = None
    cursor = None
    try:
        # Get a new database connection
        connection = get_db_connection()
        cursor = get_cursor(connection)

        username = form['username']
        password = form['password']
        first_name = form['first_name']
        last_name = form['last_name']
        email = form['email']
        phone = form['phone']
        address = form['address']

        # Check if password is complex enough
        if not validate_password(password):
            return render_template('register.html',
                                   error_message='Password must be at least 8 characters long and include uppercase, lowercase, numbers, and special characters.')


        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Insert user into users table and get user_id
        cursor.execute("INSERT INTO users (username, password_hash, role_name, status) VALUES (%s, %s, 'agronomist', 'active')", (username, hashed_password))
        user_id = cursor.lastrowid

        # Insert data into agronomists table with the user_id
        cursor.execute("INSERT INTO agronomists (user_id, first_name, last_name, email, phone_number, address, date_joined) VALUES (%s, %s, %s, %s, %s, %s, CURDATE())", (user_id, first_name, last_name, email, phone, address))

        # Commit to DB
        connection.commit()
        return redirect(url_for('login'))

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        # Handle errors and rollback any changes here
        if connection is not None:
            connection.rollback()
        return render_template('register.html',
                               error_message='An error occurred. Please try again.')

    finally:
        # Ensure the cursor and connection are closed properly
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


def register_staff(form):
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = get_cursor(connection)

        username = form['username']
        password = form['password']
        first_name = form['first_name']
        last_name = form['last_name']
        email = form['email']
        phone = form['phone']
        position = form['position']
        department = form['department']

        if not validate_password(password):
            return render_template('register_for_staff.html',
                                   error_message='Password must be at least 8 characters long and include uppercase, lowercase, numbers, and special characters.')

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        cursor.execute("INSERT INTO users (username, password_hash, role_name, status) VALUES (%s, %s, 'staff', 'active')", (username, hashed_password))
        user_id = cursor.lastrowid

        cursor.execute("INSERT INTO staff_and_administrators (user_id, first_name, last_name, email, work_phone_number, position, department, hire_date) VALUES (%s, %s, %s, %s, %s, %s, %s, CURDATE())", (user_id, first_name, last_name, email, phone, position, department))

        connection.commit()
        return redirect(url_for('login'))

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        if connection is not None:
            connection.rollback()
        return render_template('register_for_staff.html',
                               error_message='An error occurred. Please try again.')

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


def register_admin(form):
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = get_cursor(connection)

        username = form['username']
        password = form['password']
        first_name = form['first_name']
        last_name = form['last_name']
        email = form['email']
        phone = form['phone']
        position = form['position']
        department = form['department']

        if not validate_password(password):
            return render_template('register_for_admin.html',
                                   error_message='Password must be at least 8 characters long and include uppercase, lowercase, numbers, and special characters.')

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        cursor.execute("INSERT INTO users (username, password_hash, role_name, status) VALUES (%s, %s, 'administrator', 'active')", (username, hashed_password))
        user_id = cursor.lastrowid

        cursor.execute("INSERT INTO staff_and_administrators (user_id, first_name, last_name, email, work_phone_number, position, department, hire_date) VALUES (%s, %s, %s, %s, %s, %s, %s, CURDATE())", (user_id, first_name, last_name, email, phone, position, department))

        connection.commit()
        return redirect(url_for('login'))

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        if connection is not None:
            connection.rollback()
        return render_template('register_for_admin.html',
                               error_message='An error occurred. Please try again.')

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()



def login_user(username, password):
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = get_cursor(connection)

        cursor.execute("SELECT user_id, password_hash, role_name FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user['password_hash'], password):
            role = user['role_name']
            # Depending on the role, redirect to the appropriate dashboard
            if role == 'agronomist':
                return redirect(url_for('agronomist_dashboard'))
            elif role == 'staff':
                return redirect(url_for('staff_dashboard'))
            elif role == 'administrator':
                return redirect(url_for('administrator_dashboard'))
        # If login fails, return an error message
        return 'Login Failed', 401

    except Exception as e:
        # Log the exception or handle it as per your logging policy
        print(f"An error occurred: {e}")
        # You can render a template with an error message or return a simple string
        return 'An error occurred during login.', 500

    finally:
        # Ensure the cursor and connection are closed properly
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()




def check_if_user_exists(username):
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = get_cursor(connection)

        cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
        return bool(cursor.fetchone())

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        return False

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

