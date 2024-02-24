from flask import Flask, flash, render_template, request, redirect, url_for
import mysql.connector
import connect

app = Flask(__name__)

dbconn = None
connection = None

def getCursor():
    global dbconn
    global connection
    connection = mysql.connector.connect(
        user=connect.dbuser,
        password=connect.dbpass,
        host=connect.dbhost,
        database=connect.dbname,
        autocommit=True
    )
    dbconn = connection.cursor(dictionary=True, buffered=True)
    return dbconn


@app.route("/")
def home():
    return render_template('base.html')


if __name__ == '__main__':
    app.run()
