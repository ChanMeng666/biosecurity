from flask import Flask, render_template
import mysql.connector
import connect

app = Flask(__name__)

db_conn = None
connection = None


def get_cursor():
    global db_conn
    global connection
    connection = mysql.connector.connect(
        user=connect.db_user,
        password=connect.db_pass,
        host=connect.db_host,
        database=connect.db_name,
        autocommit=True
    )
    db_conn = connection.cursor(dictionary=True, buffered=True)
    return db_conn


@app.route("/")
def home():
    return render_template('base.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/register")
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
