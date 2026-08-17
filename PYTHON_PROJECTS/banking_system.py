import tkinter as tk


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

# -----------------------------
# REGISTER PAGE
# -----------------------------

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
    command=show_dash
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

tk.Label(
    login,
    text="LOGIN",
    font=("Arial", 20)
).pack(pady=50)


tk.Button(
    login,
    text="Back",
    command=show_dash
).pack()


# -----------------------------
# Start with Home
# -----------------------------

home_page.pack()


root.mainloop()