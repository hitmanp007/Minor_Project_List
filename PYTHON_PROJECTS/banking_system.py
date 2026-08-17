from tkinter import *
root = Tk()
root.title("Banking System")
root.geometry("300x400")

title = Label(
    root,
    text="PYTHON BANK",
    font=("Arial", 18, "bold")
)

def show_home():

    registration_frame.pack_forget()
    login_frame.pack_forget()
    dashboard_frame.pack_forget()

    home_frame.pack(fill="both", expand=True)

    Label(
    home_frame,
    text="PYTHON BANK",
    font=("Arial", 20, "bold")
).pack(pady=50)


Button(
    home_frame,
    text="Create Account",
    command=show_registration
).pack(pady=10)


Button(
    home_frame,
    text="Login",
    command=show_login
).pack(pady=10)
#main page
def dashboard():
    
    
    reg = Button(root,text="Create Account")
    log = Button(root,text="Login")
    reg.place(x=100.,y=100,width=100,height=50)
    log.place(x=100.,y=200,width=100,height=50)

# # registration page
# def registration():
#     root = Tk()
#     root.geometry("300x500")
#     n = Label(root,text="Name").place(x=50,y=100,width=100,height=50)
#     i = Label(root,text="ID").place(x=50,y=170,width=100,height=50)
#     p = Label(root,text="Pass").place(x=50,y=250,width=100,height=50)
#     e = Label(root,text="Email").place(x=50,y=320,width=100,height=50)
#     t1 =Entry(root).place(x=120,y=100,width=170,height=50)
#     t2 =Entry(root).place(x=120,y=170,width=170,height=50)
#     t3 =Entry(root).place(x=120,y=250,width=170,height=50)
#     t4 =Entry(root).place(x=120,y=320,width=170,height=50)
#     s = Button(root,text="submit",command=dashboard).place(x=75,y=380,width=100,height=50)
# def login():
#     root = Tk()
#     pass


main = Button(root,text="click to start",command=dashboard)
main.place(x=100.,y=100,width=100,height=50)
title.pack(pady=10)

mainloop()