from tkinter import *
import math
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
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    checks_label.config(text="")
    timer_label.config(text="Timer",fg=GREEN,bg=YELLOW)
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #



def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        reps += 1
        timer_label.config(text="Long Break",fg=RED,bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK, bg=YELLOW)
        reps += 1
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW)

def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checks_label.config(text=marks)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=150, pady=100, bg=YELLOW)



tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(window, width=200, height=224, bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",font=(FONT_NAME, 40, "bold"),fill="white")
canvas.grid(row=1,column=1)

timer_label = Label(text="Timer",font=(FONT_NAME,45),fg=GREEN,bg=YELLOW)
timer_label.grid(row=0,column=1)

checks_label = Label(bg=YELLOW,fg=GREEN)
checks_label.grid(row=3,column=1)

start_button = Button(text="Start", bg=YELLOW, highlightthickness=0,borderwidth=0,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0,borderwidth=0,command=reset_timer)
reset_button.grid(row=2,column=2)








window.mainloop()