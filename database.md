## Database Setup

Follow the steps below to set up the database and required tables.

### 1. Create the Database

```sql
CREATE DATABASE IF NOT EXISTS password_users;
USE password_users;
```
### 2. Create the log_users Table
```sql
CREATE TABLE IF NOT EXISTS log_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    contact_no VARCHAR(15),
    password VARCHAR(100) NOT NULL
);
```
### 3. Create the web_passwords Table
```sql
CREATE TABLE IF NOT EXISTS web_passwords (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    website VARCHAR(70) NOT NULL,
    username VARCHAR(70) NOT NULL,
    password VARCHAR(70) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES log_users(id) ON DELETE CASCADE
);
```
### 4. Test the Tables (Optional)
```sql
SELECT * FROM log_users;
SELECT * FROM web_passwords;
```
