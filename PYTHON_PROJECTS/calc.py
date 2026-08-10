from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x400")


# -----------------------------
# Calculator functions
# -----------------------------

def button_click(value):
    display.insert(END, value)


def clear():
    display.delete(0, END)


def calculate():
    try:
        expression = display.get()

        # Replace calculator symbols with Python operators
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")

        result = eval(expression)

        display.delete(0, END)
        display.insert(END, result)

    except:
        display.delete(0, END)
        display.insert(END, "Error")


def backspace():
    current = display.get()

    display.delete(0, END)
    display.insert(END, current[:-1])


# -----------------------------
# Title
# -----------------------------

title = Label(
    root,
    text="CALCULATOR",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)


# -----------------------------
# Display
# -----------------------------

display = Entry(
    root,
    font=("Arial", 22),
    justify="right"
)

display.pack(fill=X, padx=10, pady=5)


# -----------------------------
# Buttons
# -----------------------------

button_frame = Frame(root)
button_frame.pack()


# Row 1

Button(
    button_frame,
    text="AC",
    command=clear,
    width=7,
    height=2
).grid(row=0, column=0)

Button(
    button_frame,
    text="%",
    command=lambda: button_click("%"),
    width=7,
    height=2
).grid(row=0, column=1)

Button(
    button_frame,
    text="⌫",
    command=backspace,
    width=7,
    height=2
).grid(row=0, column=2)

Button(
    button_frame,
    text="÷",
    command=lambda: button_click("÷"),
    width=7,
    height=2
).grid(row=0, column=3)


# Row 2

Button(
    button_frame,
    text="7",
    command=lambda: button_click("7"),
    width=7,
    height=2
).grid(row=1, column=0)

Button(
    button_frame,
    text="8",
    command=lambda: button_click("8"),
    width=7,
    height=2
).grid(row=1, column=1)

Button(
    button_frame,
    text="9",
    command=lambda: button_click("9"),
    width=7,
    height=2
).grid(row=1, column=2)

Button(
    button_frame,
    text="×",
    command=lambda: button_click("×"),
    width=7,
    height=2
).grid(row=1, column=3)


# Row 3

Button(
    button_frame,
    text="4",
    command=lambda: button_click("4"),
    width=7,
    height=2
).grid(row=2, column=0)

Button(
    button_frame,
    text="5",
    command=lambda: button_click("5"),
    width=7,
    height=2
).grid(row=2, column=1)

Button(
    button_frame,
    text="6",
    command=lambda: button_click("6"),
    width=7,
    height=2
).grid(row=2, column=2)

Button(
    button_frame,
    text="-",
    command=lambda: button_click("-"),
    width=7,
    height=2
).grid(row=2, column=3)


# Row 4

Button(
    button_frame,
    text="1",
    command=lambda: button_click("1"),
    width=7,
    height=2
).grid(row=3, column=0)

Button(
    button_frame,
    text="2",
    command=lambda: button_click("2"),
    width=7,
    height=2
).grid(row=3, column=1)

Button(
    button_frame,
    text="3",
    command=lambda: button_click("3"),
    width=7,
    height=2
).grid(row=3, column=2)

Button(
    button_frame,
    text="+",
    command=lambda: button_click("+"),
    width=7,
    height=2
).grid(row=3, column=3)


# Row 5

Button(
    button_frame,
    text="0",
    command=lambda: button_click("0"),
    width=15,
    height=2
).grid(row=4, column=0, columnspan=2)

Button(
    button_frame,
    text=".",
    command=lambda: button_click("."),
    width=7,
    height=2
).grid(row=4, column=2)

Button(
    button_frame,
    text="=",
    command=calculate,
    width=7,
    height=2
).grid(row=4, column=3)


# -----------------------------
# Run
# -----------------------------

mainloop()