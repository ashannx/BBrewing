import time as t
import tkinter as tk

DARKER_BACKGROUND = "#68A2B9"
LIGHT_BACKGROUND = "#A2C4D1"
BROWN = "#D2C9B5"
BLACK = "#231F20"
FONT = ("Arial", 10, "normal")
TITLE_FONT = ("Arial", 12, "underline")
LARGE_LABEL_FONT = ("Arial", 12, "normal")

window = tk.Tk()
window.title("Brewing")
window.config(padx=10, pady=10, bg=DARKER_BACKGROUND, width=200, height=200)

# Brew Number
# Row 0
brew_number_label = tk.Label(bg=DARKER_BACKGROUND, text="Brew Number: ", font=LARGE_LABEL_FONT, foreground=BLACK)
brew_number_label.grid(column=0, row=0, sticky="news", pady=20)
brew_number = tk.Entry(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width=10)
brew_number.grid(column=1, row=0, sticky="news", pady=20)

search_button = tk.Button(text="Look Up", bg=LIGHT_BACKGROUND, font=FONT, activebackground=DARKER_BACKGROUND, foreground=BLACK)
search_button.grid(column=2, row=0, padx=7, sticky="news", pady=20)

add_new_button = tk.Button(text="Add", bg=LIGHT_BACKGROUND, font=FONT, activebackground=DARKER_BACKGROUND, foreground=BLACK)
add_new_button.grid(column=3, row=0, sticky="news", pady=20)

# Basic Info
# Row 1
basic_label = tk.Label(bg=DARKER_BACKGROUND, text="Basic Info:", font=TITLE_FONT, foreground=BLACK, anchor="w")
basic_label.grid(column=0, row=1, sticky="news", columnspan=2)

brew_date_label = tk.Label(bg=DARKER_BACKGROUND, text="Brew Date:", font=FONT, foreground=BLACK, anchor="e", width=10)
brew_date_label.grid(column=1, row=1, sticky="news", pady=20)
brew_date = tk.Entry(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width=10)
brew_date.grid(column=2, row=1, sticky="news", pady=20)

type_label = tk.Label(bg=DARKER_BACKGROUND, text="Type:", font=FONT, foreground=BLACK, anchor="e", width=10)
type_label.grid(column=3, row=1, sticky="news", pady=20)
b_type = tk.Entry(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width=10)
b_type.grid(column=4, row=1, sticky="news", pady=20)

# Fermentation
# Row 2
fermentation_label = tk.Label(bg=DARKER_BACKGROUND, text="Fermentation:", font=TITLE_FONT, foreground=BLACK, anchor="w")
fermentation_label.grid(column=0, row=2, sticky="news", columnspan=2)

FV_tank_label = tk.Label(bg=DARKER_BACKGROUND, text="Tank:", font=FONT, foreground=BLACK, anchor="e", width=10)
FV_tank_label.grid(column=1, row=2, sticky="news", pady=25)
FV_tank = tk.Entry(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width="10")
FV_tank.grid(column=2, row=2, sticky="news", pady=25)

date_plated_label = tk.Label(bg=DARKER_BACKGROUND, text="Plated:", font=FONT, foreground=BLACK, anchor="e", width=10)
date_plated_label.grid(column=3, row=2, sticky="news", pady=25)
date_plated_date = tk.Entry(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width="10")
date_plated_date.grid(column=4, row=2, sticky="news", pady=25)

crashed_label = tk.Label(bg=DARKER_BACKGROUND, text="Crashed:", font=FONT, foreground=BLACK, anchor="e", width=10)
crashed_label.grid(column=5, row=2, sticky="news", pady=25)
crashed = tk.Entry(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width=10)
crashed.grid(column=6, row=2, sticky="news", pady=25)

# Row 3

one_label = tk.Label(bg=DARKER_BACKGROUND, text="1", font=FONT, foreground=BLACK, width=10)
one_label.grid(column=1, row=3, sticky="news")

two_label = tk.Label(bg=DARKER_BACKGROUND, text="2", font=FONT, foreground=BLACK, width=10)
two_label.grid(column=2, row=3, sticky="news")

three_label = tk.Label(bg=DARKER_BACKGROUND, text="3", font=FONT, foreground=BLACK, width=10)
three_label.grid(column=3, row=3, sticky="news")

four_label = tk.Label(bg=DARKER_BACKGROUND, text="4", font=FONT, foreground=BLACK, width=10)
four_label.grid(column=4, row=3, sticky="news")

five_label = tk.Label(bg=DARKER_BACKGROUND, text="5", font=FONT, foreground=BLACK, width=10)
five_label.grid(column=5, row=3, sticky="news")

six_label = tk.Label(bg=DARKER_BACKGROUND, text="6", font=FONT, foreground=BLACK, width=10)
six_label.grid(column=6, row=3, sticky="news")

notes_label = tk.Label(bg=DARKER_BACKGROUND, text="notes", font=FONT, foreground=BLACK, width=10)
notes_label.grid(column=7, row=3, sticky="news")

# Row 4
WLD_label = tk.Label(bg=DARKER_BACKGROUND, text="WLD", font=FONT, foreground=BLACK, width=10)
WLD_label.grid(column=0, row=4, sticky="news")

WLD_one_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_one_check.grid(column=1, row=4, padx=7)

WLD_two_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_two_check.grid(column=2, row=4, padx=7)

WLD_three_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_three_check.grid(column=3, row=4, padx=7)

WLD_four_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_four_check.grid(column=4, row=4, padx=7)

WLD_five_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_five_check.grid(column=5, row=4, padx=7)

WLD_six_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_six_check.grid(column=6, row=4, padx=7)

WLD_notes = tk.Text(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width=30, height=1)
WLD_notes.grid(column=7, row=4, sticky="news", pady=3)

# Row 5
WLN_label = tk.Label(bg=DARKER_BACKGROUND, text="WLN", font=FONT, foreground=BLACK, width=10)
WLN_label.grid(column=0, row=5, sticky="news")

WLN_one_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_one_check.grid(column=1, row=5, padx=7)

WLN_two_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_two_check.grid(column=2, row=5, padx=7)

WLN_three_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_three_check.grid(column=3, row=5, padx=7)

WLN_four_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_four_check.grid(column=4, row=5, padx=7)

WLN_five_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_five_check.grid(column=5, row=5, padx=7)

WLN_six_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_six_check.grid(column=6, row=5, padx=7)

WLN_notes = tk.Text(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width="25", height=1)
WLN_notes.grid(column=7, row=5, sticky="news", pady=3)


# Brite
# Row 6
brite_label = tk.Label(bg=DARKER_BACKGROUND, text="Brite:", font=TITLE_FONT, foreground=BLACK, anchor="w")
brite_label.grid(column=0, row=6, sticky="news", columnspan=2)

BB_tank_label = tk.Label(bg=DARKER_BACKGROUND, text="Tank:", font=FONT, foreground=BLACK, anchor="e", width=10)
BB_tank_label.grid(column=1, row=6, sticky="news", pady=25)
BB_tank = tk.Entry(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width="10")
BB_tank.grid(column=2, row=6, sticky="news", pady=25)

date_plated_BB_label = tk.Label(bg=DARKER_BACKGROUND, text="Plated:", font=FONT, foreground=BLACK, anchor="e", width=10)
date_plated_BB_label.grid(column=3, row=6, sticky="news", pady=25)
date_plated_BB_date = tk.Entry(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width="10")
date_plated_BB_date.grid(column=4, row=6, sticky="news", pady=25)

transferred_label = tk.Label(bg=DARKER_BACKGROUND, text="Crashed:", font=FONT, foreground=BLACK, anchor="e", width=10)
transferred_label.grid(column=5, row=6, sticky="news", pady=25)
transferred = tk.Entry(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width=10)
transferred.grid(column=6, row=6, sticky="news", pady=25)

# Row 7

one_BB_label = tk.Label(bg=DARKER_BACKGROUND, text="1", font=FONT, foreground=BLACK, width=10)
one_BB_label.grid(column=1, row=7, sticky="news")

two_BB_label = tk.Label(bg=DARKER_BACKGROUND, text="2", font=FONT, foreground=BLACK, width=10)
two_BB_label.grid(column=2, row=7, sticky="news")

three_BB_label = tk.Label(bg=DARKER_BACKGROUND, text="3", font=FONT, foreground=BLACK, width=10)
three_BB_label.grid(column=3, row=7, sticky="news")

four_BB_label = tk.Label(bg=DARKER_BACKGROUND, text="4", font=FONT, foreground=BLACK, width=10)
four_BB_label.grid(column=4, row=7, sticky="news")

five_BB_label = tk.Label(bg=DARKER_BACKGROUND, text="5", font=FONT, foreground=BLACK, width=10)
five_BB_label.grid(column=5, row=7, sticky="news")

six_BB_label = tk.Label(bg=DARKER_BACKGROUND, text="6", font=FONT, foreground=BLACK, width=10)
six_BB_label.grid(column=6, row=7, sticky="news")

notes_BB_label = tk.Label(bg=DARKER_BACKGROUND, text="notes", font=FONT, foreground=BLACK, width=10)
notes_BB_label.grid(column=7, row=7, sticky="news")

# Row 8
WLD_BB_label = tk.Label(bg=DARKER_BACKGROUND, text="WLD", font=FONT, foreground=BLACK, width=10)
WLD_BB_label.grid(column=0, row=8, sticky="news")

WLD_BB_one_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_BB_one_check.grid(column=1, row=8, padx=7)

WLD_BB_two_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_BB_two_check.grid(column=2, row=8, padx=7)

WLD_BB_three_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_BB_three_check.grid(column=3, row=8, padx=7)

WLD_BB_four_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_BB_four_check.grid(column=4, row=8, padx=7)

WLD_BB_five_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_BB_five_check.grid(column=5, row=8, padx=7)

WLD_BB_six_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_BB_six_check.grid(column=6, row=8, padx=7)

WLD_BB_notes = tk.Text(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width=30, height=1)
WLD_BB_notes.grid(column=7, row=8, sticky="news", pady=3)

# Row 9
WLN_BB_label = tk.Label(bg=DARKER_BACKGROUND, text="WLN", font=FONT, foreground=BLACK, width=10)
WLN_BB_label.grid(column=0, row=9, sticky="news")

WLN_BB_one_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_BB_one_check.grid(column=1, row=9, padx=7)

WLN_BB_two_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_BB_two_check.grid(column=2, row=9, padx=7)

WLN_BB_three_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_BB_three_check.grid(column=3, row=9, padx=7)

WLN_BB_four_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_BB_four_check.grid(column=4, row=9, padx=7)

WLN_BB_five_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_BB_five_check.grid(column=5, row=9, padx=7)

WLN_BB_six_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLN_BB_six_check.grid(column=6, row=9, padx=7)

WLN_BB_notes = tk.Text(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width=30, height=1)
WLN_BB_notes.grid(column=7, row=9, sticky="news", pady=3)

# Row 10
MRSA_BB_label = tk.Label(bg=DARKER_BACKGROUND, text="MRSA", font=FONT, foreground=BLACK, width=10)
MRSA_BB_label.grid(column=0, row=10, sticky="news")

MRSA_BB_one_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
MRSA_BB_one_check.grid(column=1, row=10, padx=7)

MRSA_BB_two_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
MRSA_BB_two_check.grid(column=2, row=10, padx=7)

MRSA_BB_three_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
MRSA_BB_three_check.grid(column=3, row=10, padx=7)

MRSA_BB_four_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
MRSA_BB_four_check.grid(column=4, row=10, padx=7)

MRSA_BB_five_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
MRSA_BB_five_check.grid(column=5, row=10, padx=7)

MRSA_BB_six_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
MRSA_BB_six_check.grid(column=6, row=10, padx=7)

MRSA_BB_notes = tk.Text(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width=30, height=1)
MRSA_BB_notes.grid(column=7, row=10, sticky="news", pady=3)

# Pkg
# Row 11
pkg_label = tk.Label(bg=DARKER_BACKGROUND, text="Packaged:", font=TITLE_FONT, foreground=BLACK, anchor="w")
pkg_label.grid(column=0, row=11, sticky="news", columnspan=2)

date_plated_pkg_label = tk.Label(bg=DARKER_BACKGROUND, text="Plated:", font=FONT, foreground=BLACK, anchor="e", width=10)
date_plated_pkg_label.grid(column=1, row=11, sticky="news", pady=25)

date_plated_pkg_date = tk.Entry(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width="10")
date_plated_pkg_date.grid(column=2, row=11, sticky="news", pady=25)

samples_pkg_label = tk.Label(bg=DARKER_BACKGROUND, text="Samples:", font=FONT, foreground=BLACK, anchor="e", width=10)
samples_pkg_label.grid(column=3, row=11, sticky="news", pady=25)

warm_label = tk.Label(bg=DARKER_BACKGROUND, text="Warm", font=FONT, foreground=BLACK, anchor="e", width=10)
warm_label.grid(column=4, row=11, sticky="news", pady=25)
warm_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND, anchor="w")
warm_check.grid(column=5, row=11, sticky="w")

cold_label = tk.Label(bg=DARKER_BACKGROUND, text="Cold", font=FONT, foreground=BLACK, anchor="e", width=10)
cold_label.grid(column=6, row=11, sticky="news", pady=25)
cold_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
cold_check.grid(column=7, row=11, sticky="w")

# Row 12

one_pkg_label = tk.Label(bg=DARKER_BACKGROUND, text="1", font=FONT, foreground=BLACK, width=10)
one_pkg_label.grid(column=1, row=12, sticky="news")

two_pkg_label = tk.Label(bg=DARKER_BACKGROUND, text="2", font=FONT, foreground=BLACK, width=10)
two_pkg_label.grid(column=2, row=12, sticky="news")

three_pkg_label = tk.Label(bg=DARKER_BACKGROUND, text="3", font=FONT, foreground=BLACK, width=10)
three_pkg_label.grid(column=3, row=12, sticky="news")

four_pkg_label = tk.Label(bg=DARKER_BACKGROUND, text="4", font=FONT, foreground=BLACK, width=10)
four_pkg_label.grid(column=4, row=12, sticky="news")

five_pkg_label = tk.Label(bg=DARKER_BACKGROUND, text="5", font=FONT, foreground=BLACK, width=10)
five_pkg_label.grid(column=5, row=12, sticky="news")

six_pkg_label = tk.Label(bg=DARKER_BACKGROUND, text="6", font=FONT, foreground=BLACK, width=10)
six_pkg_label.grid(column=6, row=12, sticky="news")

notes_pkg_label = tk.Label(bg=DARKER_BACKGROUND, text="notes", font=FONT, foreground=BLACK, width=10)
notes_pkg_label.grid(column=7, row=12, sticky="news")

# Row 13
WLD_pkg_label = tk.Label(bg=DARKER_BACKGROUND, text="WLD", font=FONT, foreground=BLACK, width=10)
WLD_pkg_label.grid(column=0, row=13, sticky="news")

WLD_pkg_one_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_pkg_one_check.grid(column=1, row=13, padx=7)

WLD_pkg_two_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_pkg_two_check.grid(column=2, row=13, padx=7)

WLD_pkg_three_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_pkg_three_check.grid(column=3, row=13, padx=7)

WLD_pkg_four_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_pkg_four_check.grid(column=4, row=13, padx=7)

WLD_pkg_five_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_pkg_five_check.grid(column=5, row=13, padx=7)

WLD_pkg_six_check = tk.Checkbutton(onvalue=1, offvalue=0, bg=DARKER_BACKGROUND, activebackground=DARKER_BACKGROUND)
WLD_pkg_six_check.grid(column=6, row=13, padx=7)

WLD_pkg_notes = tk.Text(bg=LIGHT_BACKGROUND, font=FONT, foreground=BLACK, width=30, height=1)
WLD_pkg_notes.grid(column=7, row=13, sticky="news", pady=3)


window.mainloop()