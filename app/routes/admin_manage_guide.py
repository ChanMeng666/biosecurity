from flask import render_template, request, redirect, url_for, flash
from .admin_blueprint import admin_bp
from ..database.db_connection import get_db_connection
import mysql.connector
from mysql.connector import Error

ITEMS_PER_PAGE = 20


@admin_bp.route('/admin/manage-guide', methods=['GET', 'POST'])
def admin_manage_guide():
    if request.method == 'POST':
        agriculture_id = request.form.get('agriculture_id')
        if agriculture_id:
            connection = get_db_connection()
            cursor = connection.cursor()
            delete_query = "DELETE FROM agriculture_items WHERE agriculture_id = %s"
            cursor.execute(delete_query, (agriculture_id,))
            connection.commit()
            cursor.close()
            connection.close()
            flash('Agricultural ID deleted successfully.', 'success')
            return redirect(url_for('admin.admin_manage_guide'))

    # Handle the GET request for searching and pagination
    page = request.args.get('page', 1, type=int)
    search_field = request.args.get('search_field', 'Choose...')
    search_value = request.args.get('search_value', '')
    offset = (page - 1) * ITEMS_PER_PAGE
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Construct the WHERE clause for searching
    where_clause = ""
    params = []
    table_alias = "ai" if search_field not in ['image_id', 'is_primary'] else "im"
    if search_field != 'Choose...' and search_value:
        where_clause = f"WHERE {table_alias}.{search_field} LIKE %s"
        params.append(f"%{search_value}%")

    count_query = f"SELECT COUNT(*) AS total FROM agriculture_items ai LEFT JOIN images im ON ai.agriculture_id = im.agriculture_id {where_clause}"
    cursor.execute(count_query, params)
    total_items = cursor.fetchone()['total']
    total_pages = (total_items + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE

    query = f"""
    SELECT
        ai.agriculture_id,
        ai.item_type,
        ai.common_name,
        ai.scientific_name,
        ai.key_characteristics,
        ai.biology,
        ai.impacts,
        ai.control,
        im.image_id,
        im.image_path,
        im.is_primary
    FROM agriculture_items ai
    LEFT JOIN images im ON ai.agriculture_id = im.agriculture_id
    {where_clause}
    ORDER BY ai.agriculture_id, im.is_primary DESC
    LIMIT %s OFFSET %s
    """
    params.extend([ITEMS_PER_PAGE, offset])
    cursor.execute(query, params)
    guide_items = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        'admin/admin_manage_guide.html',
        guide_items=guide_items,
        page=page,
        total_pages=total_pages,
        search_field=search_field,
        search_value=search_value
    )

@admin_bp.route('/admin/manage-guide/add', methods=['GET', 'POST'])
def admin_manage_guide_add():
    image_fields = request.form.get('image_fields', 1)
    form_data = request.form.to_dict()

    if request.method == 'POST':
        if 'add_image' in request.form:
            image_fields = int(image_fields) + 1
            form_data['image_fields'] = image_fields
            return render_template('admin/admin_manage_guide_add.html', image_fields=image_fields, form_data=form_data)
        else:
            connection = get_db_connection()
            cursor = connection.cursor()

            item_type = form_data['item_type']
            common_name = form_data['common_name']
            scientific_name = form_data['scientific_name']
            key_characteristics = form_data['key_characteristics']
            biology = form_data['biology']
            impacts = form_data['impacts']
            control = form_data['control']

            # Insert guide information into the agriculture_items table
            insert_query = """
            INSERT INTO agriculture_items (item_type, common_name, scientific_name, key_characteristics, biology, impacts, control)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (item_type, common_name, scientific_name, key_characteristics, biology, impacts, control))
            agriculture_id = cursor.lastrowid
            connection.commit()

            # Insert image information into the images table
            for i in range(int(image_fields)):
                is_primary_key = f'is_primary_{i}'
                image_path_key = f'image_path_{i}'
                if is_primary_key in form_data and image_path_key in form_data:
                    is_primary = form_data[is_primary_key]
                    image_path = form_data[image_path_key]
                    insert_image_query = """
                    INSERT INTO images (agriculture_id, image_path, is_primary)
                    VALUES (%s, %s, %s)
                    """
                    cursor.execute(insert_image_query, (agriculture_id, image_path, is_primary))
                    connection.commit()

            cursor.close()
            connection.close()

            flash('Guide added successfully!', 'success')
            return redirect(url_for('admin.admin_manage_guide_add'))

    return render_template('admin/admin_manage_guide_add.html', image_fields=image_fields, form_data=form_data)


@admin_bp.route('/admin/manage-guide/edit/<int:agriculture_id>', methods=['GET'])
def admin_manage_guide_edit(agriculture_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Fetch agriculture item details
    cursor.execute("""
        SELECT * FROM agriculture_items
        WHERE agriculture_id = %s
    """, (agriculture_id,))
    agriculture_item = cursor.fetchone()

    # Fetch images for the agriculture item
    cursor.execute("""
        SELECT * FROM images
        WHERE agriculture_id = %s
    """, (agriculture_id,))
    images = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        'admin/admin_manage_guide_edit.html',
        agriculture_item=agriculture_item,
        images=images
    )

@admin_bp.route('/admin/manage-guide/update/<int:agriculture_id>', methods=['POST'])
def admin_manage_guide_update(agriculture_id):
    # Get form data
    form_data = request.form.to_dict()

    # Open database connection
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Update the agriculture_items table with the new data
        update_query = """
        UPDATE agriculture_items
        SET item_type = %s, common_name = %s, scientific_name = %s,
            key_characteristics = %s, biology = %s, impacts = %s, control = %s
        WHERE agriculture_id = %s
        """
        cursor.execute(update_query, (
            form_data['item_type'],
            form_data['common_name'],
            form_data['scientific_name'],
            form_data['key_characteristics'],
            form_data['biology'],
            form_data['impacts'],
            form_data['control'],
            agriculture_id
        ))

        # Update images related to the agriculture_id
        # Assuming form inputs for images are named image_path_1, is_primary_1, image_path_2, is_primary_2, etc.
        for key in form_data.keys():
            if key.startswith('image_path_'):
                index = key.split('_')[-1]
                is_primary_key = f'is_primary_{index}'
                image_path = form_data[key]
                is_primary = form_data.get(is_primary_key, 0)

                # Update the images table
                # You will need to decide how to handle the image records. This is just a placeholder example.
                image_update_query = """
                UPDATE images
                SET image_path = %s, is_primary = %s
                WHERE agriculture_id = %s
                """
                cursor.execute(image_update_query, (image_path, is_primary, agriculture_id))

        # Commit the changes
        connection.commit()
        flash('Guide updated successfully!', 'success')
    except mysql.connector.Error as err:
        # Rollback in case of any error
        connection.rollback()
        flash(f'An error occurred: {err}', 'danger')
    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()

    # Redirect to the manage guide page
    return redirect(url_for('admin.admin_manage_guide'))