from flask import Flask
from .routes.admin_routes import admin_bp
from .routes.staff_routes import staff_bp
from .routes.agronomist_routes import agronomist_bp
from .routes.home_routes import home_bp
from .routes.auth_routes import auth_bp
from .routes.errors_handlers import errors_bp


app = Flask(__name__)
app.config.from_object('config.Config')


app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(staff_bp, url_prefix='/staff')
app.register_blueprint(agronomist_bp, url_prefix='/agronomist')
app.register_blueprint(home_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(errors_bp, url_prefix='/errors')
