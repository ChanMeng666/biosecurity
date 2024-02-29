from flask import render_template, request, redirect, url_for
from user_management import register_user, login_user, check_if_user_exists, register_staff, register_admin
import mysql.connector
import connect
from werkzeug.security import generate_password_hash, check_password_hash

def home():
    return render_template('base.html')

def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        return register_user(request.form)

def register_for_staff():
    if request.method == "GET":
        return render_template('register_for_staff.html')
    else:
        return register_staff(request.form)

def register_for_admin():
    if request.method == "GET":
        return render_template('register_for_admin.html')
    else:
        return register_admin(request.form)

def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        return login_user(request.form['username'], request.form['password'])

def check_username():
    username = request.args.get('username')
    return {'exists': check_if_user_exists(username)}

def agronomist_dashboard():
    return render_template('agronomist_dashboard.html')

def staff_dashboard():
    return render_template('staff_dashboard.html')

def administrator_dashboard():
    return render_template('administrator_dashboard.html')

def agronomist_profile():
    return render_template('agronomist_profile.html')

def staff_profile():
    return render_template('staff_profile.html')

def administrator_profile():
    return render_template('administrator_profile.html')

