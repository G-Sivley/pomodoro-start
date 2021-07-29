from tkinter import *
import math
from playsound import playsound


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

# ---------------------------- Sound Handling ---------------------------- #
def play_sound(sound):
    playsound(sound)

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    check_label["text"] = ""
    timer_label.config(text="TIMER", fg=GREEN)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps 
    reps += 1
    
    time_in_seconds = 0
    if reps % 2 != 0:
        time_in_seconds = WORK_MIN * 60
        timer_label.config(text="Time to work!", fg=GREEN)
        play_sound("work_time.wav")

    elif reps % 8 == 0:
        time_in_seconds = LONG_BREAK_MIN * 60
        timer_label.config(text="Long break!", fg=RED)
        play_sound("long_break.wav")

    else:
        time_in_seconds = SHORT_BREAK_MIN * 60
        timer_label.config(text="Short Break!", fg=PINK)
        play_sound("short_break.wav")

        
    countdown(time_in_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    global timer
    count_minute = math.floor(count / 60)
    count_second = count % 60 

    if count_minute < 10:
        count_minute = "0" + str(count_minute)

    if count_second < 10:
        count_second = "0" + str(count_second)

    time_remaining = f"{count_minute}:{count_second}"

    canvas.itemconfig(canvas_text, text=time_remaining)
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    
    else:
        start_timer()
        if reps % 2 == 0:
            
            curr_label = "✓" + check_label["text"]
            check_label.config(text=curr_label)

# ---------------------------- UI SETUP ------------------------------- #

# Initialize the window of Tkiniter
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create the canvas for the image and timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# Create the text timer number
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer label
timer_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

# Start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# Check label
check_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 55, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()