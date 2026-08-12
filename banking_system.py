from tkinter import *
root = Tk()
root.title("Banking System")
root.geometry("300x400")

title = Label(
    root,
    text="PYTHON BANK",
    font=("Arial", 18, "bold")
)
reg = Button(root,text="Create Account")
log = Button(root,text="Login")
reg.place(x=100.,y=100,width=100,height=50)
log.place(x=100.,y=200,width=100,height=50)

title.pack(pady=10)
mainloop()