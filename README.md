# Password-manager
Hi! I'm Ansh Sharma, and this project is a simple yet functional Password Manager application developed using Python's tkinter library for the GUI and MySQL for database connectivity.
The main purpose of this application is to securely store user passwords for various websites. For example, if a user has accounts on Instagram, Gmail, and Facebook, they can use this app to store all those credentials safely in one place.

## Features
1. User Registration & Login
    Users can register by creating a username and password. After logging in, they can store and manage their website credentials.
2. Secure Password Storage
    Each user’s data is stored separately in the database, ensuring that no other user can access another user's credentials.
3. Password Reset:
    Forgot your password? No worries. The app includes a "Forgot Password" feature to reset your login credentials.
4. Simple GUI
    Built using Tkinter — it's easy to use and understand, even for beginners.

Still in Development : This is a work in progress, and I’m actively working to add more features and improve security.

## Prerequisites
Before running this application, ensure you have the following:
1. Python installed (version 3.6+ recommended)
2. Required Python libraries:
   
   2.1 Tkinter (usually included with Python)
   
   2.2 mysql-connector-python (pip install mysql-connector-python)
3. A MySQL server installed and running (e.g., MySQL Workbench)

## Getting Started
Clone the repository or download the passmanager.py file.
Set up your MySQL database using the script above.
Make sure all required libraries are installed.
Run the ```passmanager.py``` script:

```bash
python passmanager.py 
