import tkinter as tk
from tkinter import messagebox, simpledialog
import mysql.connector

def login_page():  # function for main window for logging
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showerror("Input Error", "Required fields cannot be left empty")
        return

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="Gutsss",  #change according to your mysql user(root)
            password="gutsss77",  #change according to your user password of mysql(root)
            database="password_users"
        )

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM log_users  WHERE username = %s AND password = %s',
                       (username, password))
        user = cursor.fetchone()

        conn.close()

        if user:
            user_data = f"ID: {user[0]}\n First Name: {user[1]}\n Username: {user[3]}\n Email: {user[4]}\n Contact Number: {user[5]}"
            messagebox.showinfo("Login Successful!", f"Login Successful!\n\n User Data:\n{user_data}")
            open_password_manager(user[0])
        else:
            messagebox.showerror("Login", "Invalid username or password")

    except mysql.connector.Error as err:
        messagebox.showerror("Database error", str(err))

def open_password_manager(user_id):
    def add_password():
        website = simpledialog.askstring("Input", "Enter the website:")
        username = simpledialog.askstring("Input", "Enter the username:")
        password = simpledialog.askstring("Input", "Enter the password:", show='*')

        if not website or not username or not password:
            messagebox.showerror("Input Error", "All fields are mandatory!")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="Gutsss",
                password="gutsss77",
                database="password_users"
            )
            cursor = conn.cursor()
            cursor.execute('INSERT INTO web_passwords (user_id, website, username, password) VALUES (%s, %s, %s, %s)',
                           (user_id, website, username, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Password added successfully!")
            view_passwords()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))

    def view_passwords():
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="Gutsss",
                password="gutsss77",
                database="password_users"
            )
            cursor = conn.cursor()
            cursor.execute('SELECT website, username, password FROM web_passwords WHERE user_id = %s', (user_id,))
            passwords = cursor.fetchall()
            conn.close()

            passwords_text.delete('1.0', tk.END)
            for pw in passwords:
                passwords_text.insert(tk.END, f"Website: {pw[0]}\nUsername: {pw[1]}\nPassword: {pw[2]}\n\n")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))

    password_manager_window = tk.Toplevel(root)
    password_manager_window.title("Password Manager")

    tk.Button(password_manager_window, text="Add Password", command=add_password).pack(pady=10)
    passwords_text = tk.Text(password_manager_window, height=15, width=50)
    passwords_text.pack(pady=10)

    view_passwords()


def registration_page(): #function for new person registration
    def register():
        first_name = entry_first_name.get()
        last_name = entry_last_name.get()
        username = entry_new_username.get()
        email = entry_email.get()
        contact_no = entry_contact_no.get()
        password = entry_create_password.get()
        confirm_password = entry_confirm_password.get()

        if first_name == "" or username == "" or email == "" or contact_no == "" or password == "" or confirm_password == "":
            messagebox.showerror("Input Error!", "All fields are mandatory!")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="Gutsss",
                password="gutsss77",
                database="password_users"
            )

            cursor = conn.cursor()
            cursor.execute('''INSERT INTO log_users (first_name, last_name, username, email, contact_no, password)
                           VALUES (%s,%s,%s,%s,%s,%s)''', (first_name, last_name, username, email, contact_no, password))

            conn.commit()
            messagebox.showinfo("Success", "Registration Successful!")
            registration_window.destroy()

        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "Email already registered!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))
        finally:
            conn.close()

    #creating window for new registraring person
    registration_window = tk.Toplevel(root)
    registration_window.title("Registration Page")

    tk.Label(registration_window, text="First name").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(registration_window, text="Last name").grid(row=1, column=0, padx=10, pady=10)
    tk.Label(registration_window, text="Username").grid(row=2, column=0, padx=10, pady=10)
    tk.Label(registration_window, text="Email").grid(row=3, column=0, padx=10, pady=10)
    tk.Label(registration_window, text="Contact Number").grid(row=4, column=0, padx=10, pady=10)
    tk.Label(registration_window, text="Password").grid(row=5, column=0, padx=10, pady=10)
    tk.Label(registration_window, text="Confirm Password").grid(row=6, column=0, padx=10, pady=10)

    entry_first_name = tk.Entry(registration_window)
    entry_last_name = tk.Entry(registration_window)
    entry_new_username= tk.Entry(registration_window)
    entry_email = tk.Entry(registration_window)
    entry_contact_no = tk.Entry(registration_window)
    entry_create_password = tk.Entry(registration_window, show='*')
    entry_confirm_password = tk.Entry(registration_window, show='*')

    entry_first_name.grid(row=0, column=1, padx=10, pady=10)
    entry_last_name.grid(row=1, column=1, padx=10, pady=10)
    entry_new_username.grid(row=2, column=1, padx=10, pady=10)
    entry_email.grid(row=3, column=1, padx=10, pady=10)
    entry_contact_no.grid(row=4, column=1, padx=10, pady=10)
    entry_create_password.grid(row=5, column=1, padx=10, pady=10)
    entry_confirm_password.grid(row=6, column=1, padx=10, pady=10)

    tk.Button(registration_window, text="Register", command=register).grid(row=8, column=0, columnspan=2, pady=10)


def open_forget_password():  # function for password forget
    def reset_password():  # function to reset password
        username = entry_forget_username.get()
        new_password = entry_forget_password.get()


        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="Gutsss",
                password="gutsss77",
                database="password_users"
            )
            cursor = conn.cursor()

            cursor.execute('''UPDATE log_users SET password = %s WHERE 
                           username = %s''', new_password, username)

            if cursor.rowcount == 0:
                messagebox.showerror("Error", "Username not found!")
            else:
                messagebox.showinfo("Success", "Password reset successful!")

            conn.commit()
            conn.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))

    # creating the forget password window
    password_forget_window = tk.Toplevel(root)
    password_forget_window.title("Reset Password")

    tk.Label(password_forget_window, text="Username").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(password_forget_window, text="New Password").grid(row=1, column=0, padx=10, pady=10)

    entry_forget_username = tk.Entry(password_forget_window)
    entry_forget_password = tk.Entry(password_forget_window)

    entry_forget_username.grid(row=0, column=1, padx=10, pady=10)
    entry_forget_password.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(password_forget_window, text="Reset Password", command=reset_password).grid(row=2, column=0, columnspan=2, pady=10)


root = tk.Tk()  # gui of main window
root.title("Login Page")

tk.Label(root, text="Username").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Password").grid(row=1, column=0, padx=10, pady=10)

entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show='*')

entry_username.grid(row=0, column=1, padx=10, pady=10)
entry_password.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Login", command=login_page).grid(row=2, column=0, columnspan=2, pady=10)
tk.Button(root, text="Forget Password", command=open_forget_password).grid(row=3, column=0, columnspan=2, pady=10)  # will open new window for password reset
tk.Button(root, text="Register", command=registration_page).grid(row=4, column=0, columnspan=2, pady=10)  # will open new window for new registration

root.mainloop()