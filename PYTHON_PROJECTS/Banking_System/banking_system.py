import tkinter as tk
from tkinter import messagebox


# -----------------------------
# STORAGE
# -----------------------------

accounts = {}

current_user = None


# -----------------------------
# MAIN WINDOW
# -----------------------------

root = tk.Tk()
root.title("Banking System")
root.geometry("300x400")


# -----------------------------
# PAGES
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
# PAGE SWITCHING
# -----------------------------

def hide_all_pages():

    home_page.pack_forget()
    dashboard.pack_forget()
    register.pack_forget()
    login.pack_forget()
    bank.pack_forget()
    deposit.pack_forget()
    widrawl.pack_forget()
    transaction.pack_forget()


def show_home():
    hide_all_pages()
    home_page.pack()


def show_dash():
    hide_all_pages()
    dashboard.pack()


def show_register():
    hide_all_pages()
    register.pack()


def show_login():
    hide_all_pages()
    login.pack()


def show_bank():

    hide_all_pages()

    welcome_label.config(
        text=f"Welcome, {accounts[current_user]['name']}"
    )

    balance_label.config(
        text=f"Balance: ₹{accounts[current_user]['balance']}"
    )

    bank.pack()


def show_deposite():

    hide_all_pages()

    deposit.pack()


def show_widrawl():

    hide_all_pages()

    widrawl.pack()


def show_transaction():

    hide_all_pages()

    update_transactions()

    transaction.pack()


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
# CREATE ACCOUNT
# -----------------------------

def create_account():

    name = name_entry.get()
    user_id = id_entry.get()
    email = email_entry.get()
    mobile = mobile_entry.get()
    password = password_entry.get()

    # Check empty fields
    if name == "" or user_id == "" or email == "" or mobile == "" or password == "":

        messagebox.showerror(
            "Error",
            "Please fill all fields!"
        )

        return


    # Check duplicate ID
    if user_id in accounts:

        messagebox.showerror(
            "Error",
            "Account already exists!"
        )

        return


    # Create account
    accounts[user_id] = {

        "name": name,
        "email": email,
        "mobile": mobile,
        "password": password,

        "balance": 0,

        "transactions": []
    }


    messagebox.showinfo(
        "Success",
        "Account created successfully!"
    )


    # Clear fields
    name_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    mobile_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


    show_dash()


tk.Label(
    register,
    text="CREATE ACCOUNT",
    font=("Arial", 20, "bold")
).pack(pady=20)


register_form = tk.Frame(register)
register_form.pack(pady=10)


# Name

tk.Label(
    register_form,
    text="Name"
).grid(row=0, column=0, padx=10, pady=5)


name_entry = tk.Entry(register_form)

name_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=5
)


# ID

tk.Label(
    register_form,
    text="ID"
).grid(row=1, column=0, padx=10, pady=5)


id_entry = tk.Entry(register_form)

id_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)


# Email

tk.Label(
    register_form,
    text="Email"
).grid(row=2, column=0, padx=10, pady=5)


email_entry = tk.Entry(register_form)

email_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=5
)


# Mobile

tk.Label(
    register_form,
    text="Mobile"
).grid(row=3, column=0, padx=10, pady=5)


mobile_entry = tk.Entry(register_form)

mobile_entry.grid(
    row=3,
    column=1,
    padx=10,
    pady=5
)


# Password

tk.Label(
    register_form,
    text="Password"
).grid(row=4, column=0, padx=10, pady=5)


password_entry = tk.Entry(
    register_form,
    show="*"
)

password_entry.grid(
    row=4,
    column=1,
    padx=10,
    pady=5
)


tk.Button(
    register,
    text="SUBMIT",
    command=create_account
).pack(pady=10)


tk.Button(
    register,
    text="BACK",
    command=show_dash
).pack()


# -----------------------------
# LOGIN PAGE
# -----------------------------

def check_login():

    global current_user

    user_id = login_id_entry.get()
    password = login_password_entry.get()


    if user_id in accounts:

        if accounts[user_id]["password"] == password:

            current_user = user_id

            messagebox.showinfo(
                "Success",
                "Login successful!"
            )

            show_bank()

        else:

            messagebox.showerror(
                "Error",
                "Wrong password!"
            )

    else:

        messagebox.showerror(
            "Error",
            "Account does not exist!"
        )


tk.Label(
    login,
    text="LOGIN",
    font=("Arial", 20)
).pack(pady=50)


login_form = tk.Frame(login)
login_form.pack(pady=10)


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
).pack(pady=5)


tk.Button(
    login,
    text="Back",
    command=show_dash
).pack()


# -----------------------------
# BANK PAGE
# -----------------------------

welcome_label = tk.Label(
    bank,
    text="Welcome",
    font=("Arial", 20)
)

welcome_label.pack(pady=30)


balance_label = tk.Label(
    bank,
    text="Balance: ₹0",
    font=("Arial", 15)
)

balance_label.pack(pady=10)


tk.Button(
    bank,
    text="Deposit",
    command=show_deposite
).pack(pady=5)


tk.Button(
    bank,
    text="Withdraw",
    command=show_widrawl
).pack(pady=5)


tk.Button(
    bank,
    text="Transaction History",
    command=show_transaction
).pack(pady=5)


tk.Button(
    bank,
    text="Logout",
    command=show_dash
).pack(pady=20)


# -----------------------------
# DEPOSIT PAGE
# -----------------------------

def add_money():

    try:

        amount = float(deposit_entry.get())

        if amount <= 0:

            messagebox.showerror(
                "Error",
                "Enter a valid amount!"
            )

            return


        accounts[current_user]["balance"] += amount


        accounts[current_user]["transactions"].append(
            f"Deposited ₹{amount}"
        )


        deposit_entry.delete(0, tk.END)


        messagebox.showinfo(
            "Success",
            f"₹{amount} deposited successfully!"
        )


        show_bank()


    except ValueError:

        messagebox.showerror(
            "Error",
            "Please enter numbers only!"
        )


tk.Label(
    deposit,
    text="DEPOSIT MONEY",
    font=("Arial", 20)
).pack(pady=50)


deposit_entry = tk.Entry(
    deposit,
    font=("Arial", 15)
)

deposit_entry.pack(pady=10)


tk.Button(
    deposit,
    text="Deposit",
    command=add_money
).pack(pady=5)


tk.Button(
    deposit,
    text="Back",
    command=show_bank
).pack()


# -----------------------------
# WITHDRAW PAGE
# -----------------------------

def withdraw_money():

    try:

        amount = float(withdraw_entry.get())


        if amount <= 0:

            messagebox.showerror(
                "Error",
                "Enter a valid amount!"
            )

            return


        if amount > accounts[current_user]["balance"]:

            messagebox.showerror(
                "Error",
                "Insufficient balance!"
            )

            return


        accounts[current_user]["balance"] -= amount


        accounts[current_user]["transactions"].append(
            f"Withdrawn ₹{amount}"
        )


        withdraw_entry.delete(0, tk.END)


        messagebox.showinfo(
            "Success",
            f"₹{amount} withdrawn successfully!"
        )


        show_bank()


    except ValueError:

        messagebox.showerror(
            "Error",
            "Please enter numbers only!"
        )


tk.Label(
    widrawl,
    text="WITHDRAW MONEY",
    font=("Arial", 20)
).pack(pady=50)


withdraw_entry = tk.Entry(
    widrawl,
    font=("Arial", 15)
)

withdraw_entry.pack(pady=10)


tk.Button(
    widrawl,
    text="Withdraw",
    command=withdraw_money
).pack(pady=5)


tk.Button(
    widrawl,
    text="Back",
    command=show_bank
).pack()


# -----------------------------
# TRANSACTION PAGE
# -----------------------------

def update_transactions():

    transaction_text.delete(
        "1.0",
        tk.END
    )


    transactions = accounts[current_user]["transactions"]


    if len(transactions) == 0:

        transaction_text.insert(
            tk.END,
            "No transactions yet."
        )

    else:

        for item in transactions:

            transaction_text.insert(
                tk.END,
                item + "\n"
            )


tk.Label(
    transaction,
    text="TRANSACTION HISTORY",
    font=("Arial", 16)
).pack(pady=20)


transaction_text = tk.Text(
    transaction,
    width=30,
    height=12
)

transaction_text.pack(pady=10)


tk.Button(
    transaction,
    text="Back",
    command=show_bank
).pack()


# -----------------------------
# START APPLICATION
# -----------------------------

home_page.pack()

root.mainloop()