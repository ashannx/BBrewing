import time as t
import tkinter as tk

DARKER_BACKGROUND = "#68A2B9"
LIGHT_BACKGROUND = "#A2C4D1"
BROWN = "#D2C9B5"
BLACK = "#231F20"
FONT = ("Arial", 10, "normal")
TITLE_FONT = ("Arial", 14, "underline")
LARGE_LABEL_FONT = ("Arial", 14, "normal")

window = tk.Tk()
window.title("Brewing")
window.config(padx=10, pady=10, bg=DARKER_BACKGROUND, width=200, height=200)

# Row 0
brew_number_label = tk.Label(bg=DARKER_BACKGROUND, text="Brew Number:", font=LARGE_LABEL_FONT, foreground=BLACK)
brew_number_label.grid(column=0, row=0, sticky="news", pady=20)
brew_number = tk.Entry(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width=10)
brew_number.grid(column=1, row=0, sticky="news", pady=20)

search_button = tk.Button(text="Search", bg=LIGHT_BACKGROUND, font=FONT, activebackground=DARKER_BACKGROUND, foreground=BLACK)
search_button.grid(column=2, row=0, padx=10, sticky="news", pady=20)

add_new_button = tk.Button(text="Add", bg=LIGHT_BACKGROUND, font=FONT, activebackground=DARKER_BACKGROUND, foreground=BLACK)
add_new_button.grid(column=3, row=0, sticky="news", pady=20)

# Row 1
basic_label = tk.Label(bg=DARKER_BACKGROUND, text="Basic Info", font=TITLE_FONT, foreground=BLACK, anchor="w")
basic_label.grid(column=0, row=1, sticky="news", columnspan=2)

# Row 2
brew_date_label = tk.Label(bg=DARKER_BACKGROUND, text="Brew Date:", font=FONT, foreground=BLACK, anchor="e", width=10)
brew_date_label.grid(column=0, row=2, sticky="news", pady=20)
brew_date = tk.Entry(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width=10)
brew_date.grid(column=1, row=2, sticky="news", pady=20)

type_label = tk.Label(bg=DARKER_BACKGROUND, text="Type:", font=FONT, foreground=BLACK, anchor="e", width=10)
type_label.grid(column=2, row=2, sticky="news", pady=20)
b_type = tk.Entry(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width=10)
b_type.grid(column=3, row=2, sticky="news", pady=20)

# Row 3
fermentation_label = tk.Label(bg=DARKER_BACKGROUND, text="Fermentation", font=TITLE_FONT, foreground=BLACK, anchor="w")
fermentation_label.grid(column=0, row=3, sticky="news", columnspan=2)

# Row 4
FV_tank_label = tk.Label(bg=DARKER_BACKGROUND, text="FV Tank:", font=FONT, foreground=BLACK, anchor="e", width=10)
FV_tank_label.grid(column=0, row=4, sticky="news", pady=25)
FV_tank = tk.Entry(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width="10")
FV_tank.grid(column=1, row=4, sticky="news", pady=25)

date_plated_label = tk.Label(bg=DARKER_BACKGROUND, text="Date Plated:", font=FONT, foreground=BLACK, anchor="e", width=10)
date_plated_label.grid(column=2, row=4, sticky="news", pady=25)
date_plated_date = tk.Entry(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width="10")
date_plated_date.grid(column=3, row=4, sticky="news", pady=25)

crashed_label = tk.Label(bg=DARKER_BACKGROUND, text="Crashed:", font=FONT, foreground=BLACK, anchor="e", width=10)
crashed_label.grid(column=4, row=4, sticky="news", pady=25)
crashed = tk.Entry(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width=10)
crashed.grid(column=5, row=4, sticky="news", pady=25)

# Row 5
one_label = tk.Label(bg=DARKER_BACKGROUND, text="1", font=FONT, foreground=BLACK, width=10)
one_label.grid(column=1, row=5, sticky="news")

two_label = tk.Label(bg=DARKER_BACKGROUND, text="2", font=FONT, foreground=BLACK, width=10)
two_label.grid(column=2, row=5, sticky="news")

three_label = tk.Label(bg=DARKER_BACKGROUND, text="3", font=FONT, foreground=BLACK, width=10)
three_label.grid(column=3, row=5, sticky="news")

four_label = tk.Label(bg=DARKER_BACKGROUND, text="4", font=FONT, foreground=BLACK, width=10)
four_label.grid(column=4, row=5, sticky="news")

five_label = tk.Label(bg=DARKER_BACKGROUND, text="5", font=FONT, foreground=BLACK, width=10)
five_label.grid(column=5, row=5, sticky="news")

six_label = tk.Label(bg=DARKER_BACKGROUND, text="6", font=FONT, foreground=BLACK, width=10)
six_label.grid(column=6, row=5, sticky="news")

notes_label = tk.Label(bg=DARKER_BACKGROUND, text="notes", font=FONT, foreground=BLACK, width=10)
notes_label.grid(column=7, row=5, sticky="news")

# Row 6
WLD_label = tk.Label(bg=DARKER_BACKGROUND, text="WLD", font=FONT, foreground=BLACK, width=10)
WLD_label.grid(column=0, row=6, sticky="news")

WLD_one_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_one_check.grid(column=1, row=6, padx=10, pady=10)

WLD_two_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_two_check.grid(column=2, row=6, padx=10, pady=10)

WLD_three_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_three_check.grid(column=3, row=6, padx=10, pady=10)

WLD_four_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_four_check.grid(column=4, row=6, padx=10, pady=10)

WLD_five_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_five_check.grid(column=5, row=6, padx=10, pady=10)

WLD_six_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_six_check.grid(column=6, row=6, padx=10, pady=10)

WLD_notes = tk.Text(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width="10", height=2)
WLD_notes.grid(column=7, row=6, sticky="news", pady=3)

# Row 7
WLN_label = tk.Label(bg=DARKER_BACKGROUND, text="WLN", font=FONT, foreground=BLACK, width=10)
WLN_label.grid(column=0, row=7, sticky="news")

WLN_one_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_one_check.grid(column=1, row=7, padx=10, pady=10)

WLN_two_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_two_check.grid(column=2, row=7, padx=10, pady=10)

WLN_three_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_three_check.grid(column=3, row=7, padx=10, pady=10)

WLN_four_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_four_check.grid(column=4, row=7, padx=10, pady=10)

WLN_five_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_five_check.grid(column=5, row=7, padx=10, pady=10)

WLN_six_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_six_check.grid(column=6, row=7, padx=10, pady=10)

WLN_notes = tk.Text(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width="10", height=2)
WLN_notes.grid(column=7, row=7, sticky="news")


window.mainloop()