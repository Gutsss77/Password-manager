/* Read How to use sql code to execute I correctly :) */

CREATE DATABASE password_users;
USE password_users;

CREATE TABLE log_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    contact_no VARCHAR(15),
    password VARCHAR(100) NOT NULL
);



CREATE TABLE web_passwords (
id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
website VARCHAR(70) NOT NULL,
username VARCHAR(70) NOT NULL,
password VARCHAR(70) NOT NULL,
FOREIGN KEY (user_id) REFERENCES log_users(id) ON DELETE CASCADE
);

CREATE USER 'Gutsss'@'localhost' IDENTIFIED BY 'gutsss77';
GRANT ALL PRIVILEGES ON password_users.* TO 'Gutsss'@'localhost';
FLUSH PRIVILEGES;

SELECT * FROM web_passwords;
SELECT * FROM log_users;
