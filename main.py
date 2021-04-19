import time as t
import tkinter as tk

DARKER_BACKGROUND = "#68A2B9"
LIGHT_BACKGROUND = "#A2C4D1"
BROWN = "#D2C9B5"
BLACK = "#231F20"
BUTTON_FONT = ("Arial", 10, "normal")

window = tk.Tk()
window.title("Brewing")
window.config(padx=10, pady=10, bg=DARKER_BACKGROUND, width=200, height=200)

brew_number = tk.Entry(bg=LIGHT_BACKGROUND, font=BUTTON_FONT, foreground=BLACK)
brew_number.grid(column=0, row=0, sticky="news")
search_button = tk.Button(text="Search", bg=LIGHT_BACKGROUND, font=BUTTON_FONT, activebackground=DARKER_BACKGROUND, foreground=BLACK)
search_button.grid(column=1, row=0, padx=5, sticky="news")

window.mainloop()