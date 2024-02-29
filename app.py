from flask import Flask
import views

app = Flask(__name__)

# Define URL rules using functions from views.py
app.add_url_rule('/', 'home', views.home)
app.add_url_rule('/register', 'register', views.register, methods=['GET', 'POST'])
app.add_url_rule('/register_for_staff', 'register_for_staff', views.register_for_staff, methods=['GET', 'POST'])
app.add_url_rule('/register_for_admin', 'register_for_admin', views.register_for_admin, methods=['GET', 'POST'])
app.add_url_rule('/login', 'login', views.login, methods=['GET', 'POST'])
app.add_url_rule('/check_username', 'check_username', views.check_username)
app.add_url_rule('/agronomist_dashboard', 'agronomist_dashboard', views.agronomist_dashboard)
app.add_url_rule('/staff_dashboard', 'staff_dashboard', views.staff_dashboard)
app.add_url_rule('/administrator_dashboard', 'administrator_dashboard', views.administrator_dashboard)
app.add_url_rule('/agronomist_profile', 'agronomist_profile', views.agronomist_profile)
app.add_url_rule('/staff_profile', 'staff_profile', views.staff_profile)
app.add_url_rule('/administrator_profile', 'administrator_profile', views.administrator_profile)

if __name__ == '__main__':
    app.run(debug=True)
