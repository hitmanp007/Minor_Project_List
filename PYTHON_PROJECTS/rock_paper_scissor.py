import tkinter as tk
import random


# --------------------------------
# Variables
# --------------------------------

player_score = 0
computer_score = 0
round_number = 0


choices = {
    0: "STONE",
    1: "PAPER",
    2: "SCISSOR"
}


# --------------------------------
# Game Function
# --------------------------------

def play(player_choice):

    global player_score
    global computer_score
    global round_number

    # Computer choice
    computer_choice = random.choice([0, 1, 2])

    round_number += 1

    # Display choices
    player_label.config(
        text=f"You chose: {choices[player_choice]}"
    )

    computer_label.config(
        text=f"Computer chose: {choices[computer_choice]}"
    )


    # -----------------------------
    # Check round result
    # -----------------------------

    if player_choice == computer_choice:

        result_label.config(
            text="DRAW!"
        )

    elif (
        (player_choice == 0 and computer_choice == 2) or
        (player_choice == 1 and computer_choice == 0) or
        (player_choice == 2 and computer_choice == 1)
    ):

        player_score += 1

        result_label.config(
            text="YOU WIN THIS ROUND! 🎉"
        )

    else:

        computer_score += 1

        result_label.config(
            text="COMPUTER WINS THIS ROUND!"
        )


    # Update score
    score_label.config(
        text=f"You: {player_score}    Computer: {computer_score}"
    )


    # -----------------------------
    # Check final winner
    # -----------------------------

    if player_score == 2:

        result_label.config(
            text="🏆 YOU WON THE GAME!"
        )

        disable_buttons()


    elif computer_score == 2:

        result_label.config(
            text="💻 COMPUTER WON THE GAME!"
        )

        disable_buttons()


    elif round_number == 3:

        if player_score > computer_score:

            result_label.config(
                text="🏆 YOU WON THE GAME!"
            )

        elif computer_score > player_score:

            result_label.config(
                text="💻 COMPUTER WON THE GAME!"
            )

        else:

            result_label.config(
                text="🤝 GAME DRAW!"
            )

        disable_buttons()


# --------------------------------
# Disable buttons
# --------------------------------

def disable_buttons():

    stone_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissor_button.config(state="disabled")


# --------------------------------
# Restart Game
# --------------------------------

def restart():

    global player_score
    global computer_score
    global round_number

    player_score = 0
    computer_score = 0
    round_number = 0

    player_label.config(text="You chose: ")
    computer_label.config(text="Computer chose: ")

    result_label.config(
        text="Choose your move!"
    )

    score_label.config(
        text="You: 0    Computer: 0"
    )

    stone_button.config(state="normal")
    paper_button.config(state="normal")
    scissor_button.config(state="normal")


# --------------------------------
# Window
# --------------------------------

root = tk.Tk()

root.title("Stone Paper Scissor")
root.geometry("450x500")


# --------------------------------
# Title
# --------------------------------

title = tk.Label(
    root,
    text="STONE PAPER SCISSOR",
    font=("Arial", 20, "bold")
)

title.pack(pady=20)


# --------------------------------
# Score
# --------------------------------

score_label = tk.Label(
    root,
    text="You: 0    Computer: 0",
    font=("Arial", 15, "bold")
)

score_label.pack(pady=10)


# --------------------------------
# Choices
# --------------------------------

player_label = tk.Label(
    root,
    text="You chose: ",
    font=("Arial", 13)
)

player_label.pack(pady=5)


computer_label = tk.Label(
    root,
    text="Computer chose: ",
    font=("Arial", 13)
)

computer_label.pack(pady=5)


# --------------------------------
# Result
# --------------------------------

result_label = tk.Label(
    root,
    text="Choose your move!",
    font=("Arial", 15, "bold")
)

result_label.pack(pady=20)


# --------------------------------
# Buttons
# --------------------------------

button_frame = tk.Frame(root)

button_frame.pack(pady=10)


stone_button = tk.Button(
    button_frame,
    text="🪨 STONE",
    width=12,
    height=2,
    command=lambda: play(0)
)

stone_button.grid(row=0, column=0, padx=5)


paper_button = tk.Button(
    button_frame,
    text="📄 PAPER",
    width=12,
    height=2,
    command=lambda: play(1)
)

paper_button.grid(row=0, column=1, padx=5)


scissor_button = tk.Button(
    button_frame,
    text="✂ SCISSOR",
    width=12,
    height=2,
    command=lambda: play(2)
)

scissor_button.grid(row=0, column=2, padx=5)


# --------------------------------
# Restart Button
# --------------------------------

restart_button = tk.Button(
    root,
    text="PLAY AGAIN",
    width=15,
    height=2,
    command=restart
)

restart_button.pack(pady=25)


# --------------------------------
# Run
# --------------------------------

root.mainloop()