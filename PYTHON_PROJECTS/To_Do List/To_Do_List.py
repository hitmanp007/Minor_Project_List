import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# -----------------------------
# Main Window
# -----------------------------

root = tk.Tk()
root.title("My To-Do List")
root.geometry("650x650")
root.resizable(False, False)


background_image = Image.open("C:/Users/pranav/Desktop/Minor_Projects/PYTHON_PROJECTS/To_Do List/background.jpg")
background_image = background_image.resize((650, 650))

background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(
    root,
    image=background_photo
)

background_label.place(
    x=0,
    y=0,
    relwidth=1,
    relheight=1
)

# -----------------------------
# Variables
# -----------------------------

tasks = []


# -----------------------------
# Functions
# -----------------------------

def update_counter():
    total = len(tasks)
    completed = sum(task["completed"] for task in tasks)

    counter_label.config(
        text=f"Total: {total}   |   Completed: {completed}   |   Remaining: {total - completed}"
    )


def add_task():
    task_text = task_entry.get().strip()

    if not task_text:
        messagebox.showwarning(
            "Empty Task",
            "Please enter a task."
        )
        return

    # Check duplicate
    for task in tasks:
        if task["text"].lower() == task_text.lower():
            messagebox.showwarning(
                "Duplicate Task",
                "This task already exists."
            )
            return

    tasks.append({
        "text": task_text,
        "completed": False
    })

    task_entry.delete(0, tk.END)

    display_tasks()


def complete_task(index):
    if not tasks[index]["completed"]:

        tasks[index]["completed"] = True

        display_tasks()

        # Celebration
        messagebox.showinfo(
            "🎉 Task Completed!",
            f"Great job! 🎉\n\n"
            f'"{tasks[index]["text"]}"\n\n'
            "You completed a task! Keep going! 💪"
        )


def remove_task(index):
    task_name = tasks[index]["text"]

    answer = messagebox.askyesno(
        "Remove Task",
        f"Do you want to remove:\n\n{task_name}?"
    )

    if answer:
        tasks.pop(index)
        display_tasks()


def display_tasks():

    # Remove old task widgets
    for widget in task_container.winfo_children():
        widget.destroy()

    if not tasks:
        empty_label = tk.Label(
            task_container,
            text="No tasks yet! Add something to get started 🚀",
            font=("Arial", 12)
        )
        empty_label.pack(pady=30)

    else:

        for index, task in enumerate(tasks):

            task_frame = tk.Frame(
                task_container,
                bd=1,
                relief="solid",
                padx=8,
                pady=8
                
            )

            task_frame.pack(
                fill="x",
                pady=5,
                padx=5
            )

            # Task text
            if task["completed"]:
                task_text = "✓ " + task["text"]

                task_label = tk.Label(
                    task_frame,
                    text=task_text,
                    font=("Arial", 12, "overstrike"),
                    width=30,
                    anchor="w"
                )

            else:
                task_text = "○ " + task["text"]

                task_label = tk.Label(
                    task_frame,
                    text=task_text,
                    font=("Arial", 12),
                    width=30,
                    anchor="w"
                )

            task_label.pack(
                side="left",
                padx=5
            )

            # Complete button
            if not task["completed"]:

                complete_button = tk.Button(
                    task_frame,
                    text="✓ Complete",
                    command=lambda i=index: complete_task(i)
                )

                complete_button.pack(
                    side="right",
                    padx=3
                )

            # Remove button
            remove_button = tk.Button(
                task_frame,
                text="🗑 Remove",
                command=lambda i=index: remove_task(i)
            )

            remove_button.pack(
                side="right",
                padx=3
            )

    update_counter()


# -----------------------------
# Title
# -----------------------------

title_label = tk.Label(
    root,
    text="✨ MY TO-DO LIST ✨",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=(20, 5))


subtitle_label = tk.Label(
    root,
    text="Organize your day, one task at a time!",
    font=("Arial", 11)
)

subtitle_label.pack(pady=(0, 20))


# -----------------------------
# Input Area
# -----------------------------

input_frame = tk.Frame(root)
input_frame.pack()


task_entry = tk.Entry(
    input_frame,
    width=40,
    font=("Arial", 13)
)

task_entry.pack(
    side="left",
    padx=5
)


add_button = tk.Button(
    input_frame,
    text="＋ Add Task",
    font=("Arial", 11, "bold"),
    command=add_task
)

add_button.pack(
    side="left",
    padx=5
)


# Press Enter to add
task_entry.bind(
    "<Return>",
    lambda event: add_task()
)


# -----------------------------
# Counter
# -----------------------------

counter_label = tk.Label(
    root,
    text="Total: 0   |   Completed: 0   |   Remaining: 0",
    font=("Arial", 11, "bold")
)

counter_label.pack(pady=15)


# -----------------------------
# Task Area
# -----------------------------

task_container = tk.Frame(root)

task_container.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=5,
)


# -----------------------------
# Start
# -----------------------------

task_entry.focus()

display_tasks()

root.mainloop()