from werkzeug.security import generate_password_hash

password = input('Enter password to hash: ')
hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
print('Hashed password:', hashed_password)