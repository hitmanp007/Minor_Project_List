import random


print("""
==============================
    STONE PAPER SCISSOR
==============================

Press 0 for STONE
Press 1 for PAPER
Press 2 for SCISSOR
""")


# Computer chooses randomly
com = random.choice([0, 1, 2])

# User chooses
you = int(input("Enter your choice: "))


# Store choices
words = {
    0: "STONE",
    1: "PAPER",
    2: "SCISSOR"
}


# Check invalid input
if you not in words:
    print("Invalid choice! Please choose 0, 1 or 2.")

else:

    print(f"\nOPPONENT CHOSE : {words[com]}")
    print(f"YOU CHOSE      : {words[you]}")

    # Draw
    if com == you:
        print("\nDRAW!")

    # User wins
    elif (
        (you == 0 and com == 2) or
        (you == 1 and com == 0) or
        (you == 2 and com == 1)
    ):
        print("\nYOU WIN! 🎉")

    # Otherwise computer wins
    else:
        print("\nYOU LOSE! 😢")