CREATE TABLE roles (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role_id INT NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100) NOT NULL UNIQUE,
    phone_number VARCHAR(20),
    date_joined DATETIME NOT NULL,
    status ENUM('active', 'inactive') NOT NULL,
    FOREIGN KEY (role_id) REFERENCES roles(role_id)
);

CREATE TABLE agronomists (
    agronomist_id INT NOT NULL,
    address TEXT,
    FOREIGN KEY (agronomist_id) REFERENCES users(user_id)
);

CREATE TABLE staff (
    staff_id INT NOT NULL,
    FOREIGN KEY (staff_id) REFERENCES users(user_id)
);

CREATE TABLE administrators (
    administrator_id INT NOT NULL,
    FOREIGN KEY (administrator_id) REFERENCES users(user_id)
);

CREATE TABLE agriculture_items (
    agriculture_id INT AUTO_INCREMENT PRIMARY KEY,
    item_type ENUM('pest', 'weed') NOT NULL,
    common_name VARCHAR(255) NOT NULL,
    scientific_name VARCHAR(255),
    key_characteristics TEXT,
    biology TEXT,
    impacts TEXT,
    control TEXT
);

CREATE TABLE images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    agriculture_id INT NOT NULL,
    image_path VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (agriculture_id) REFERENCES agriculture_items(agriculture_id)
);

INSERT INTO roles (role_name) VALUES ('Agronomist');
INSERT INTO roles (role_name) VALUES ('Staff');
INSERT INTO roles (role_name) VALUES ('Administrator');

