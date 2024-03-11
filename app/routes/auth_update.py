from .auth_blueprint import auth_bp, render_toast
from flask import request, jsonify, session
from werkzeug.security import generate_password_hash
from ..database.db_connection import get_db_connection
from .auth_blueprint import is_password_complex

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