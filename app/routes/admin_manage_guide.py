from flask import render_template, request, redirect, url_for, flash
from .admin_blueprint import admin_bp
from ..database.db_connection import get_db_connection

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




