from flask import Blueprint, session, redirect, url_for, jsonify, request
import user_management

# 创建一个Blueprint对象
admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/get_administrator_info')
def get_administrator_info():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    admin_details = user_management.get_administrator_details(user_id)
    if admin_details:
        return jsonify(admin_details)
    else:
        return jsonify({"error": "Administrator details not found"}), 404


@admin_bp.route('/update_administrator_details', methods=['POST'])
def update_administrator_details():
    # 确保用户已登录并且是管理员
    if 'user_id' not in session or session.get('role') != 'administrator':
        return jsonify({'error': 'Unauthorized'}), 401

    # 获取前端发送的数据
    data = request.get_json()
    user_id = session['user_id']
    field = data.get('field')
    value = data.get('value')


    # 如果字段是密码，特别处理
    if field == 'password':
        success, message = user_management.update_administrator_password(user_id, value)
        if success:
            return jsonify({'success': success, 'message': message})
        else:
            return jsonify({'error': message}), 400

    # 如果字段是用户名，检查是否唯一
    if field == 'username' and user_management.check_if_user_exists(value):
        return jsonify({'error': 'Username already exists'}), 409


    # 更新数据库的逻辑
    success = user_management.update_administrator_detail(user_id, field, value)
    if success:
        return jsonify({'success': True, 'message': 'Details updated successfully.'})
    else:
        return jsonify({'error': 'Update failed'}), 500