from flask import Blueprint, render_template

# 创建 Blueprint
errors_bp = Blueprint('errors', __name__, template_folder='../templates/errors')

# 定义路由
@errors_bp.route('/')
def errors_index():
    return render_template('errors/errors_home.html')