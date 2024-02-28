from string import punctuation
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import connect

app = Flask(__name__)

db_conn = None
connection = None


def get_cursor():
    global db_conn
    global connection
    connection = mysql.connector.connect(
        user=connect.db_user,
        password=connect.db_pass,
        host=connect.db_host,
        database=connect.db_name,
        autocommit=True
    )
    db_conn = connection.cursor(dictionary=True, buffered=True)
    return db_conn

# Define the validate_password function once time to reuse it throughout the application
def validate_password(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in punctuation for c in password)
    return has_upper and has_lower and has_digit and has_special


@app.route("/")
def home():
    return render_template('base.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        # Initialize variables to None
        connection = None
        cursor = None

        try:
            # Get a new database connection
            connection = mysql.connector.connect(
                user=connect.db_user,
                password=connect.db_pass,
                host=connect.db_host,
                database=connect.db_name,
                autocommit=False
            )
            cursor = connection.cursor()

            # Collect form data
            username = request.form['username']
            password = request.form['password']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            phone = request.form['phone']
            address = request.form['address']

            # Check if password is complex enough
            if not validate_password(password):  # Assuming validate_password is a function defined elsewhere
                return render_template('register.html',
                                       error_message='Password must be at least 8 characters long and include uppercase, lowercase, numbers, and special characters.')

            # Hash password
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

            # Insert user into users table and get user_id
            cursor.execute("INSERT INTO users (username, password_hash, role_name, status) VALUES (%s, %s, 'agronomist', 'active')", (username, hashed_password))
            user_id = cursor.lastrowid  # Get the last inserted id

            # Insert data into agronomists table with the user_id
            cursor.execute("INSERT INTO agronomists (user_id, first_name, last_name, email, phone_number, address, date_joined) VALUES (%s, %s, %s, %s, %s, %s, CURDATE())", (user_id, first_name, last_name, email, phone, address))

            # Commit to DB
            connection.commit()

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            # Handle errors and rollback any changes here
            if connection is not None:
                connection.rollback()
        finally:
            # Ensure the cursor and connection are closed properly
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

        # Redirect to the login page
        return redirect(url_for('login'))



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        cursor = get_cursor()

        cursor.execute("SELECT user_id, password_hash, role_name FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user['password_hash'], password):
            role = user['role_name']
            if role == 'agronomist':
                return redirect(url_for('agronomist_profile'))
            elif role == 'staff':
                return redirect(url_for('staff_profile'))
            elif role == 'administrator':
                return redirect(url_for('administrator_profile'))
        return 'Login Failed', 401


# 测试用：
@app.route("/register_for_staff", methods=["GET", "POST"])
def register_for_staff():
    if request.method == "GET":
        return render_template('register_for_staff.html')
    else:
        # Initialize variables to None
        connection = None
        cursor = None

        try:
            # Get a new database connection
            connection = mysql.connector.connect(
                user=connect.db_user,
                password=connect.db_pass,
                host=connect.db_host,
                database=connect.db_name,
                autocommit=False
            )
            cursor = connection.cursor()

            # Collect form data
            username = request.form['username']
            password = request.form['password']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            phone = request.form['phone']
            position = request.form['position']
            department = request.form['department']

            # Check if password is complex enough
            if not validate_password(password):  # Assuming validate_password is a function defined elsewhere
                return render_template('register.html',
                                       error_message='Password must be at least 8 characters long and include uppercase, lowercase, numbers, and special characters.')

            # Hash password
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

            # Insert user into users table and get user_id
            cursor.execute("INSERT INTO users (username, password_hash, role_name, status) VALUES (%s, %s, 'staff', 'active')", (username, hashed_password))
            user_id = cursor.lastrowid  # Get the last inserted id

            # Insert data into agronomists table with the user_id
            cursor.execute("INSERT INTO staff_and_administrators (user_id, first_name, last_name, email, work_phone_number, hire_date, position, department) VALUES (%s, %s, %s, %s, %s, CURDATE(), %s, %s)", (user_id, first_name, last_name, email, phone, position, department))

            # Commit to DB
            connection.commit()

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            # Handle errors and rollback any changes here
            if connection is not None:
                connection.rollback()
        finally:
            # Ensure the cursor and connection are closed properly
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

        # Redirect to the login page
        return redirect(url_for('login'))





# 测试用：
@app.route("/register_for_admin", methods=["GET", "POST"])
def register_for_admin():
    if request.method == "GET":
        return render_template('register_for_admin.html')
    else:
        # Initialize variables to None
        connection = None
        cursor = None

        try:
            # Get a new database connection
            connection = mysql.connector.connect(
                user=connect.db_user,
                password=connect.db_pass,
                host=connect.db_host,
                database=connect.db_name,
                autocommit=False
            )
            cursor = connection.cursor()

            # Collect form data
            username = request.form['username']
            password = request.form['password']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            phone = request.form['phone']
            position = request.form['position']
            department = request.form['department']

            # Check if password is complex enough
            if not validate_password(password):  # Assuming validate_password is a function defined elsewhere
                return render_template('register.html',
                                       error_message='Password must be at least 8 characters long and include uppercase, lowercase, numbers, and special characters.')

            # Hash password
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

            # Insert user into users table and get user_id
            cursor.execute("INSERT INTO users (username, password_hash, role_name, status) VALUES (%s, %s, 'administrator', 'active')", (username, hashed_password))
            user_id = cursor.lastrowid  # Get the last inserted id

            # Insert data into agronomists table with the user_id
            cursor.execute("INSERT INTO staff_and_administrators (user_id, first_name, last_name, email, work_phone_number, hire_date, position, department) VALUES (%s, %s, %s, %s, %s, CURDATE(), %s, %s)", (user_id, first_name, last_name, email, phone, position, department))

            # Commit to DB
            connection.commit()

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            # Handle errors and rollback any changes here
            if connection is not None:
                connection.rollback()
        finally:
            # Ensure the cursor and connection are closed properly
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

        # Redirect to the login page
        return redirect(url_for('login'))



@app.route("/check_username")
def check_username():
    username = request.args.get('username')
    cursor = get_cursor()
    cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
    user_exists = cursor.fetchone()
    return {'exists': bool(user_exists)}





@app.route("/agronomist_profile")
def agronomist_profile():
    return render_template('agronomist_profile.html')

@app.route("/staff_profile")
def staff_profile():
    return render_template('staff_profile.html')

@app.route("/administrator_profile")
def administrator_profile():
    return render_template('administrator_profile.html')



if __name__ == '__main__':
    app.run()
