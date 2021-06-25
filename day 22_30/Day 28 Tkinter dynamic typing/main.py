import tkinter as tk
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
TICK = '✔'
reps = 0
tick_count = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global tick_count

    window.after_cancel(timer)
    reps = 0
    tick_count = 0
    canvas.itemconfig(timer_text, text='00:00')
    label_timer.config(text='Timer')
    label_tick.config(text='')
    
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global tick_count
    reps += 1
    

    work_min = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 2 != 0 and reps < 8:
        label_timer.config(text='Work',fg='Green')
        count_down(work_min)
    elif reps % 2 == 0 and reps <8:
        label_timer.config(text='5min Break',fg='Pink')
        count_down(short_break)
    elif reps == 8:
        reps = 0
        tick_count = 0
        label_timer.config(text='25 min Break', fg='Red')
        count_down(long_break)
        
        


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global tick_count
    global timer
    
    count_min = math.floor(count/60) # calculates mins
    count_sec = math.floor(count%60) # calculates secs
        
    # add leading zero if number less than 10
    if count_sec < 10:
        count_sec = f'{count_sec:02d}'
        
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    # loop by calling itself, reducing the count by 1 until it gets to zero
    if count > 0:
       timer =  window.after(1000,count_down, count - 1)
    # If the count == 0 then put a tick after each completed work cycle
    else:
        if reps % 2 != 0: # after work cycle
            tick_count += 1
            label_tick.config(text=TICK * tick_count )
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.minsize(width=400, height=300)
window.title('Pomedoro Technique')
window.config(padx=100, pady=50, bg=YELLOW)

image_path = r'C:\Users\pfiel\Documents\Python\100doc\day 22_30\Day 28 Tkinter dynamic typing\Pomedoro\tomato.png'
tomato_img = tk.PhotoImage(file=image_path)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img )
timer_text = canvas.create_text(100, 130,text='00:00', font=(FONT_NAME,35,'bold'), fill='white' )
canvas.grid(column=1,row=1)


label_timer = tk.Label(text='Timer',fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,'bold'),)
label_timer.grid(column=1,row=0)

label_tick = tk.Label(text='',fg=GREEN,bg=YELLOW,font=(FONT_NAME,14,'bold'))
label_tick.grid(column=1,row=3)


button_start = tk.Button(text='Start', highlightthickness=0,command=start_timer)
button_start.grid(column=0,row=2)

button_reset = tk.Button(text='Reset', highlightthickness=0, command=reset_timer)
button_reset.grid(column=2,row=2)

window.mainloop()