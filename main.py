import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = 5
    short_break_sec = 5
    long_break_sec = 8
    # work_sec = WORK_MIN * 60
    # short_break_sec = SHORT_BREAK_MIN * 60
    # long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(row=0, column=1)

canvas = tkinter.Canvas(width=210, height=224, bg=YELLOW)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_img)
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

start_button = tkinter.Button(text="Start", font=(FONT_NAME, 12, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 12, "bold"), command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark = tkinter.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
checkmark.grid(row=3, column=1)

window.mainloop()
