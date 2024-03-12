from flask import Blueprint, render_template, session, redirect, url_for, request
from app.database.db_connection import get_db_connection

agronomist_bp = Blueprint('agronomist', __name__, template_folder='../templates/agronomist')

@agronomist_bp.route('/home')
def agronomist_home():
    if 'agronomist_info' in session:
        agronomist_info = session['agronomist_info']
        return render_template('agronomist/agronomist_home.html', agronomist_info=agronomist_info)
    else:
        return redirect(url_for('errors.errors_index'))

@agronomist_bp.route('/agronomist/view-guide')
def agronomist_view_guide():
    if 'agronomist_info' not in session:
        return redirect(url_for('errors.errors_index'))

    page = request.args.get('page', 1, type=int)
    per_page = 20  # Since we want 5 rows and 4 cards per row
    offset = (page - 1) * per_page

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Get the total count of items for pagination
    cursor.execute("SELECT COUNT(*) AS total FROM agriculture_items")
    total_items = cursor.fetchone()['total']
    total_pages = (total_items + per_page - 1) // per_page


    cursor.execute("""
        SELECT ai.agriculture_id,
               ai.common_name,
               im.image_path
        FROM agriculture_items ai
        JOIN images im ON ai.agriculture_id = im.agriculture_id AND im.is_primary = 1
        LIMIT %s OFFSET %s
    """, (per_page, offset))

    items = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('agronomist/agronomist_view_guide.html', items=items, page=page, total_pages=total_pages)


# @agronomist_bp.route('/agronomist/view-guide-details/<int:agriculture_id>')
# def agronomist_view_guide_details(agriculture_id):
#     if 'agronomist_info' not in session:
#         return redirect(url_for('errors.errors_index'))
#
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)
#
#     # Prepared statement to prevent SQL injection
#     cursor.execute("""
#         SELECT * FROM agriculture_items ai
#         WHERE ai.agriculture_id = %s
#     """, (agriculture_id,))
#
#     item_details = cursor.fetchone()
#
#     cursor.close()
#     connection.close()
#
#     if item_details is None:
#         return redirect(url_for('errors.errors_index'))
#
#     # Pass the details to the template
#     return render_template('agronomist/agronomist_view_guide_details.html', item_details=item_details)

@agronomist_bp.route('/agronomist/view-guide-details/<int:agriculture_id>')
def agronomist_view_guide_details(agriculture_id):
    if 'agronomist_info' not in session:
        return redirect(url_for('errors.errors_index'))

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Fetch item details
    cursor.execute("""
        SELECT * FROM agriculture_items ai
        WHERE ai.agriculture_id = %s
    """, (agriculture_id,))
    item_details = cursor.fetchone()

    # Fetch images for the carousel
    cursor.execute("""
        SELECT image_path FROM images
        WHERE agriculture_id = %s
    """, (agriculture_id,))
    images = cursor.fetchall()

    cursor.close()
    connection.close()

    if item_details is None:
        return redirect(url_for('errors.errors_index'))

    # Pass the details and images to the template
    return render_template('agronomist/agronomist_view_guide_details.html', item_details=item_details, images=images)

