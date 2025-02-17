import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Reset the timer and stop the countdown."""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config = ""
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """Start the Pomodoro countdown."""
    global reps
    reps += 1
    work_sec = WORK_MIN * 1
    short_break_sec = SHORT_BREAK_MIN * 1
    long_break_sec = LONG_BREAK_MIN * 1

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)  # Convert minutes to seconds
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    """Recursive countdown function using Tkinter's after() method."""
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")  # Update timer text

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # Call itself every second
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✅"
            check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
# Create a window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Load the image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Start Button
start_button = Button(window, text="Start", font=("Arial", 14, "bold"),
                      fg="white", bg=GREEN, width=8, command=start_timer)
start_button.grid(column=1, row=3)

# Reset Button
reset_button = Button(window, text="Reset", font=("Arial", 14, "bold"),
                      fg="white", bg=RED, width=8, command=reset_timer)
reset_button.grid(column=3, row=3)

# title_label = Label(text="Timer")
title_label = Label(window, text="Timer", font=("Courier", 35, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=2, row=1)

check_mark = Label(window, text="", font=("Courier", 20, "bold"), fg=GREEN, bg=YELLOW)
check_mark.grid(column=2, row=4)

window.mainloop()
