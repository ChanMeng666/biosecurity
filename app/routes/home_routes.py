from flask import Blueprint, render_template

# 创建 Blueprint
home_bp = Blueprint('home', __name__, template_folder='../templates')

# 定义路由
@home_bp.route('/')
def home_index():
    return render_template('home.html')