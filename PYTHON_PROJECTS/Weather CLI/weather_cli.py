from tkinter import *
import requests
from PIL import ImageTk, Image
import os


root = Tk()
root.title("Weather App")
root.geometry("300x400")


# -----------------------
# IMAGE PATH
# -----------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(BASE_DIR, "summer.jpg")


# Load image
image = Image.open(image_path)

a = ImageTk.PhotoImage(image)


# Show image
image_label = Label(root, image=a)
image_label.pack()


# -----------------------
# CITY INPUT
# -----------------------

l1 = Label(root, text="Enter city name")

t1 = Entry(root)

l1.pack()

t1.pack()


# -----------------------
# WEATHER API
# -----------------------

def get_weather():

    city = t1.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric"

    result = requests.get(url).json()

    print(result)

button = Button(
    root,
    text="Click Here",
    command=get_weather
)

button.pack(pady=10)


mainloop()