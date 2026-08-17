import tkinter as tk
root = tk.Tk()
root.title("Banking System")
root.geometry("300x400")

# pages

home_page = tk.Frame(root)
dashboard = tk.Frame(root)
register  = tk.Frame(root)
login     = tk.Frame(root)
# dashboard = tk.Frame(root)
# dashboard = tk.Frame(root)


# frames

def show_home():

    home_page.pack_forget()

    dashboard.pack()



def show_dash():

    dashboard.pack_forget()

    register.pack()    


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

home_page.pack()
root.mainloop()