from app import app

with app.app_context():
    print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)