from tkinter import *
root = Tk()
root.title("Banking System")
root.geometry("300x400")

title = Label(
    root,
    text="PYTHON BANK",
    font=("Arial", 18, "bold")
)


def registration():
    root = Tk()
    root.geometry("300x400")
    l1 = Label(root,text="name :",font=("Arial", 18, "bold"))
    l2 = Label(root,text="id :",font=("Arial", 18, "bold"))
    l3 = Label(root,text="password : :",font=("Arial", 18, "bold"))
    l4 = Label(root,text="initial deposit :",font=("Arial", 18, "bold"))

    l1.grid(row=0,column=0)
    l2.grid(row=1,column=0)
    l3.grid(row=2,column=0)
    l4.grid(row=3,column=0)

reg = Button(root,text="Create Account",command=registration)
log = Button(root,text="Login")
reg.place(x=100.,y=100,width=100,height=50)
log.place(x=100.,y=200,width=100,height=50)

title.pack(pady=10)
mainloop()