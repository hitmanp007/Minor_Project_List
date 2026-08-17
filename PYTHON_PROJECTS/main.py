import tkinter as tk


# --------------------------------
# ONE WINDOW
# --------------------------------

root = tk.Tk()

root.title("Multiple Pages")
root.geometry("400x300")


# --------------------------------
# TWO PAGES
# --------------------------------

home_page = tk.Frame(root)

page2 = tk.Frame(root)


# --------------------------------
# FUNCTIONS TO CHANGE PAGE
# --------------------------------

def show_page2():

    home_page.pack_forget()

    page2.pack()


def show_home():

    page2.pack_forget()

    home_page.pack()


# --------------------------------
# HOME PAGE
# --------------------------------

tk.Label(
    home_page,
    text="HOME PAGE",
    font=("Arial", 20)
).pack(pady=50)


tk.Button(
    home_page,
    text="Go to Page 2",
    command=show_page2
).pack()


# --------------------------------
# PAGE 2
# --------------------------------

tk.Label(
    page2,
    text="PAGE 2",
    font=("Arial", 20)
).pack(pady=50)


tk.Button(
    page2,
    text="Go to Home",
    command=show_home
).pack()


# --------------------------------
# START WITH HOME
# --------------------------------

home_page.pack()


# --------------------------------
# RUN
# --------------------------------

root.mainloop()