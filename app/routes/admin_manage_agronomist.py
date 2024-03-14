from .admin_blueprint import admin_bp, is_password_complex
from flask import render_template, session, redirect, request, url_for, flash
from app.database.db_connection import get_db_connection
from mysql.connector import Error
from werkzeug.security import generate_password_hash


@admin_bp.route('/admin/manage-agronomist', methods=['GET', 'POST'])
def admin_manage_agronomist():
    if 'admin_info' not in session:
        return redirect(url_for('auth_login.login'))

    search_query = request.args.get('search_query', '')
    search_type = request.args.get('search_type', '')
    page = request.args.get('page', 1, type=int)
    per_page = 10

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    agronomists = []  # Initialize agronomists to an empty list
    total_records = 0  # Initialize total_records

    try:
        query_params = []

        base_query = """
            SELECT COUNT(*) as total FROM users u
            JOIN agronomists a ON u.user_id = a.user_id
            WHERE u.role_name = 'agronomist'
        """
        if search_type and search_query:
            search_columns = {
                'User ID': 'u.user_id',
                'Username': 'u.username',
                'Agronomist ID': 'a.agronomist_id',
                'First Name': 'a.first_name',
                'Last Name': 'a.last_name',
                'Email': 'a.email',
                'Phone Number': 'a.phone_number',
                'Address': 'a.address',
                'Date Joined': 'a.date_joined'
            }

            if search_type in search_columns:
                base_query += f" AND {search_columns[search_type]} LIKE %s"
                search_query_formatted = f"%{search_query}%"
                query_params.append(search_query_formatted)
            else:
                flash('Invalid search type selected.', 'warning')
                return redirect(url_for('admin.admin_manage_agronomist'))

        cursor.execute(base_query, query_params)
        total_records = cursor.fetchone()['total']

        # The SELECT query should match the structure of the COUNT query
        select_query = base_query.replace('COUNT(*) as total',
                                          'u.user_id, u.username, u.role_name, a.agronomist_id, a.first_name, a.last_name, a.email, a.phone_number, a.address, a.date_joined')
        select_query += ' LIMIT %s OFFSET %s'
        query_params.extend([per_page, (page - 1) * per_page])

        cursor.execute(select_query, query_params)
        agronomists = cursor.fetchall()

    except Error as e:
        flash(f"Error fetching data: {e}", 'danger')

    finally:
        cursor.close()
        connection.close()

    total_pages = (total_records + per_page - 1) // per_page

    return render_template('admin/admin_manage_agronomist.html', agronomists=agronomists, page=page, total_pages=total_pages, search_query=search_query, search_type=search_type)


@admin_bp.route('/admin/delete-agronomist', methods=['POST'])
def admin_delete_agronomist():
    if 'admin_info' not in session:
        return redirect(url_for('auth_login.login'))

    user_id = request.form.get('user_id')
    if not user_id:
        flash('Please select an agronomist first.', 'warning')
        return redirect(url_for('admin.admin_manage_agronomist'))

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM agronomists WHERE user_id = %s', (user_id,))
        connection.commit()
        flash('Agronomist deleted successfully.', 'success')
    except Error as e:
        flash(f'An error occurred: {e}', 'danger')
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('admin.admin_manage_agronomist'))




@admin_bp.route('/admin/edit-agronomist', methods=['POST'])
def edit_agronomist():
    if 'admin_info' not in session:
        return redirect(url_for('auth_login.login'))

    user_id = request.form.get('user_id')
    if not user_id:
        flash('Please select an agronomist first.', 'warning')
        return redirect(url_for('admin.admin_manage_agronomist'))

    # 重定向到新的编辑页面视图函数，并传递user_id
    return redirect(url_for('admin.admin_manage_agronomist_edit', user_id=user_id))

@admin_bp.route('/admin/manage-agronomist/edit/<int:user_id>', methods=['GET', 'POST'])
def admin_manage_agronomist_edit(user_id):
    if 'admin_info' not in session:
        return redirect(url_for('auth_login.login'))

    if request.method == 'GET':
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("""
                SELECT u.user_id, u.username, a.agronomist_id, a.first_name, a.last_name, a.email,
                       a.phone_number, a.address, a.date_joined
                FROM users u
                JOIN agronomists a ON u.user_id = a.user_id
                WHERE u.user_id = %s
            """, (user_id,))
            agronomist = cursor.fetchone()
            if not agronomist:
                flash('Agronomist not found.', 'warning')
                return redirect(url_for('admin.admin_manage_agronomist'))
        except Error as e:
            flash(f'An error occurred: {e}', 'danger')
            return redirect(url_for('admin.admin_manage_agronomist'))
        finally:
            cursor.close()
            connection.close()

        return render_template('admin/admin_manage_agronomist_edit.html', agronomist=agronomist)


    else:  # POST request

        username = request.form['username']

        password = request.form['password']

        first_name = request.form['first_name']

        last_name = request.form['last_name']

        email = request.form['email']

        phone = request.form['phone']

        address = request.form['address']

        date_joined = request.form['date_joined']

        try:

            connection = get_db_connection()

            cursor = connection.cursor()

            # Update password if provided and complex
            if password:
                if is_password_complex(password):
                    password_hash = generate_password_hash(password)
                    cursor.execute("""
                            UPDATE users SET password_hash = %s
                            WHERE user_id = %s
                        """, (password_hash, user_id))
                else:
                    flash('Password complexity requirement not met.', 'warning')
                    # # Fetch the agronomist from the database again to pass to the template
                    # agronomist = ...  # Add the logic to fetch the agronomist here
                    # return render_template('admin/admin_manage_agronomist_edit.html', agronomist=agronomist)

                    return redirect(url_for('admin.admin_manage_agronomist_edit', user_id=user_id))

            # # Update password if provided and complex
            #
            # if password:
            #     if not is_password_complex(password):
            #         flash('Password complexity requirement not met.', 'warning')
            #         # Return to the edit page with the current agronomist information
            #         return render_template('admin/admin_manage_agronomist_edit.html', agronomist=agronomist)

                # if is_password_complex(password):
                #
                #     password_hash = generate_password_hash(password)
                #
                #     cursor.execute("""
                #
                #             UPDATE users SET password_hash = %s
                #
                #             WHERE user_id = %s
                #
                #         """, (password_hash, user_id))
                #
                # else:
                #
                #     flash('Password complexity requirement not met.', 'warning')
                #
                #     return redirect(url_for('admin.admin_manage_agronomist_edit', user_id=user_id))

            # Update the rest of the fields

            cursor.execute("""

                    UPDATE agronomists SET 

                        first_name = %s, 

                        last_name = %s, 

                        email = %s, 

                        phone_number = %s, 

                        address = %s, 

                        date_joined = %s

                    WHERE user_id = %s

                """, (first_name, last_name, email, phone, address, date_joined, user_id))

            connection.commit()

            flash('Agronomist updated successfully.', 'success')


        except Error as e:

            connection.rollback()

            flash(f'An error occurred: {e}', 'danger')


        finally:

            cursor.close()

            connection.close()

        return redirect(url_for('admin.admin_manage_agronomist'))


@admin_bp.route('/admin/add-agronomist', methods=['POST'])
def add_agronomist():
    if 'admin_info' not in session:
        return redirect(url_for('auth_login.login'))

    username = request.form['add_agronomist_username']
    password = request.form['add_agronomist_password']
    first_name = request.form['add_agronomist_first_name']
    last_name = request.form['add_agronomist_last_name']
    email = request.form['add_agronomist_email']
    phone = request.form['add_agronomist_phone']
    address = request.form['add_agronomist_address']

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Check if username already exists
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            flash('Username already exists.', 'warning')
            return redirect(url_for('admin.admin_manage_agronomist'))

        # Check password complexity
        if not is_password_complex(password):
            flash('Password complexity requirement not met.', 'warning')
            return redirect(url_for('admin.admin_manage_agronomist'))

        # Insert into users table
        password_hash = generate_password_hash(password)
        cursor.execute("""
            INSERT INTO users (username, password_hash, role_name, status) 
            VALUES (%s, %s, 'agronomist', 'active')
        """, (username, password_hash))
        user_id = cursor.lastrowid

        # Insert into agronomists table
        cursor.execute("""
            INSERT INTO agronomists (user_id, first_name, last_name, email, phone_number, address, date_joined) 
            VALUES (%s, %s, %s, %s, %s, %s, CURDATE())
        """, (user_id, first_name, last_name, email, phone, address))

        connection.commit()
        flash('Agronomist added successfully.', 'success')

    except Error as e:
        connection.rollback()
        flash(f'An error occurred: {e}', 'danger')

    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('admin.admin_manage_agronomist'))


