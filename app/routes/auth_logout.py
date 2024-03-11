from .auth_blueprint import auth_bp
from flask import redirect, url_for, session

@auth_bp.route('/logout')
def logout():

    session.clear()
    return redirect(url_for('auth.login'))