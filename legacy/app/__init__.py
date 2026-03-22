from flask import Flask
from .routes.staff_routes import staff_bp
from .routes.agronomist_routes import agronomist_bp
from .routes.home_routes import home_bp
from .routes.errors_handlers import errors_bp


from .routes.auth_blueprint import auth_bp
from .routes.auth_login import login
from .routes.auth_logout import logout
from .routes.auth_register import register_agronomist, register_admin, register_staff
from .routes.auth_update import update_user_info


from app.routes.admin_blueprint import admin_bp
from app.routes.admin_home import admin_home
from app.routes.admin_manage_staff import admin_manage_staff, delete_staff, admin_add_staff, edit_staff
from app.routes.admin_manage_agronomist import admin_manage_agronomist
from app.routes.admin_manage_guide import admin_manage_guide


from flask import Flask, g
from app.utils import get_home_url_by_role


app = Flask(__name__)
app.config.from_object('config.Config')


app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(staff_bp, url_prefix='/staff')
app.register_blueprint(agronomist_bp, url_prefix='/agronomist')
app.register_blueprint(home_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(errors_bp, url_prefix='/errors')


@app.context_processor
def utility_processor():
    def get_home_url_by_role_wrapper(role):
        return get_home_url_by_role(role)
    return dict(get_home_url_by_role=get_home_url_by_role_wrapper)