import tkinter as tk
accounts = {}

root = tk.Tk()
root.title("Banking System")
root.geometry("300x400")


# -----------------------------
# Pages
# -----------------------------

home_page = tk.Frame(root)
dashboard = tk.Frame(root)
register = tk.Frame(root)
login = tk.Frame(root)
bank = tk.Frame(root)
deposit = tk.Frame(root)
widrawl = tk.Frame(root)
transaction = tk.Frame(root)

# -----------------------------
# Page switching functions
# -----------------------------

def show_home():
    dashboard.pack_forget()
    register.pack_forget()
    login.pack_forget()

    home_page.pack()


def show_dash():
    home_page.pack_forget()
    register.pack_forget()
    login.pack_forget()

    dashboard.pack()


def show_register():
    home_page.pack_forget()
    dashboard.pack_forget()
    login.pack_forget()

    register.pack()


def show_login():
    home_page.pack_forget()
    dashboard.pack_forget()
    register.pack_forget()

    login.pack()

def show_bank():
    home_page.pack_forget()
    dashboard.pack_forget()
    register.pack_forget()
    login.pack_forget()

    bank.pack()
    
def show_deposite():
    home_page.pack_forget()
    dashboard.pack_forget()
    register.pack_forget()
    login.pack_forget()
    bank.pack_forget()

    deposit.pack()

def show_widrawl():
    home_page.pack_forget()
    dashboard.pack_forget()
    register.pack_forget()
    login.pack_forget()
    bank.pack_forget()

    deposit.pack_forget()
    widrawl.pack()

def show_transaction():
    home_page.pack_forget()
    dashboard.pack_forget()
    register.pack_forget()
    login.pack_forget()
    bank.pack_forget()

    deposit.pack_forget()    

        
# -----------------------------
# HOME PAGE
# -----------------------------

tk.Label(
    home_page,
    text="HOME PAGE",
    font=("Arial", 20)
).pack(pady=50)


tk.Button(
    home_page,
    text="Go to Dashboard",
    command=show_dash
).pack()


# -----------------------------
# DASHBOARD PAGE
# -----------------------------

tk.Label(
    dashboard,
    text="DASHBOARD",
    font=("Arial", 20)
).pack(pady=50)


tk.Button(
    dashboard,
    text="Create Account",
    command=show_register
).pack(pady=5)


tk.Button(
    dashboard,
    text="Login",
    command=show_login
).pack(pady=5)


# -----------------------------
# REGISTER PAGE
# -----------------------------
def create_account():

    name = name_entry.get()
    user_id = id_entry.get()
    email = email_entry.get()
    mobile = mobile_entry.get()
    password = password_entry.get()

    if user_id in accounts:
        print("Account already exists")

    else:
        accounts[user_id] = {
            "name": name,
            "id" : id,
            "email": email,
            "mobile": mobile,
            "password": password
        }

        print("Account created successfully!")

        show_dash()

tk.Label(
    register,
    text="CREATE ACCOUNT",
    font=("Arial", 20, "bold")
).pack(pady=20)




# Form frame
form = tk.Frame(register)
form.pack(pady=10)


# Name
tk.Label(form, text="Name").grid(row=0, column=0, padx=10, pady=5)

name_entry = tk.Entry(form)
name_entry.grid(row=0, column=1, padx=10, pady=5)


# ID
tk.Label(form, text="ID").grid(row=1, column=0, padx=10, pady=5)

id_entry = tk.Entry(form)
id_entry.grid(row=1, column=1, padx=10, pady=5)


# Email
tk.Label(form, text="Email").grid(row=2, column=0, padx=10, pady=5)

email_entry = tk.Entry(form)
email_entry.grid(row=2, column=1, padx=10, pady=5)


# Mobile
tk.Label(form, text="Mobile").grid(row=3, column=0, padx=10, pady=5)

mobile_entry = tk.Entry(form)
mobile_entry.grid(row=3, column=1, padx=10, pady=5)


# Password
tk.Label(form, text="Password").grid(row=4, column=0, padx=10, pady=5)

password_entry = tk.Entry(form, show="*")
password_entry.grid(row=4, column=1, padx=10, pady=5)

# Submit button
tk.Button(
    register,
    text="SUBMIT",
    command=create_account
).pack(pady=10)

# Back button
tk.Button(
    register,
    text="BACK",
    command=show_dash
).pack(pady=10)




# -----------------------------
# LOGIN PAGE
# -----------------------------
login_form = tk.Frame(login)
login_form.pack(pady=10)

tk.Label(
    login,
    text="LOGIN",
    font=("Arial", 20)
).pack(pady=50)

def check_login():

    user_id = login_id_entry.get()
    password = login_password_entry.get()

    if user_id in accounts:

        if accounts[user_id]["password"] == password:

            print("Login successful!")

            show_bank()

        else:

            print("Wrong password!")

    else:

        print("Account does not exist!")


tk.Label(
    login_form,
    text="ID"
).grid(row=0, column=0, padx=10, pady=5)

login_id_entry = tk.Entry(login_form)

login_id_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=5
)


tk.Label(
    login_form,
    text="Password"
).grid(row=1, column=0, padx=10, pady=5)

login_password_entry = tk.Entry(
    login_form,
    show="*"
)

login_password_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)

tk.Button(
    login,
    text="Submit",
    command=check_login
).pack()


tk.Button(
    login,
    text="Back",
    command=show_dash
).pack()

# -----------------------------
# Bank Page
# -----------------------------
tk.Label(
    bank,
    text="Welcome",
    font=("Arial", 20)
).pack(pady=50)

form = tk.Frame(bank)
form.pack(pady=10)

tk.Button(
    bank,
    text="Deposit",
    command=show_bank
).pack()

tk.Button(
    bank,
    text="widrawl",
    command=show_bank
).pack()

tk.Button(
    bank,
    text="Transaction",
    command=show_bank
).pack()

# -----------------------------
# Start with Home
# -----------------------------

home_page.pack()


root.mainloop()