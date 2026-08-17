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

tk.Label(
    register,
    text="REGISTER",
    font=("Arial", 20)
).pack(pady=50)


tk.Button(
    register,
    text="Back",
    command=show_dash
).pack()


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