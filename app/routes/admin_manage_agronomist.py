from .admin_blueprint import admin_bp
from flask import render_template, session, redirect, request, url_for, flash
from app.database.db_connection import get_db_connection
from mysql.connector import Error


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

