# Ray Min
# 06/19/2024
# Reaction time game. Wait for the button to turn green and click it.
# the program will record the time it took from the button turning green to you clicking it and record the time is ms
# Note - results are slower than other online reaction games ive tried. will have to look into later

from tkinter import *
import random
import time
import math

root = Tk()
root.title("Reaction Time Game")
root.geometry("1200x600")
root.configure(bg="#330060")

# timer starts at 0
start_time = 0
# best time starts at 0
best_time = float("inf")
# countdown control. Starts at True. Turns to False if button is clicked too early
play = True


# function for when start button is clicked
# creates a random timer from 2-5 seconds until button turns green
def start_click():
    global play
    play = True
    duration = random.randint(2,5)
    text = "Wait for green"
    button.config(text=text, bg="pink")
    timer(duration)
    start_time = 0

# function that checks if countdown timer is complete
# if complete, button turns green and a timer starts
def timer(time_left):
    global countdown, play
    if not play:
        return
    
    countdown = time_left
    if time_left > 0:
        button.after(250, lambda: timer(time_left - .25))
        button.config( bg="pink", command=cheater)
    else:
        green_text = "Go"
        button.config(text=green_text, bg="lightgreen", command=time_tracker)
        global start_time
        start_time = time.perf_counter()

# In case user clicks before button turns green
def cheater():
    global play
    play = False # stops the countdown
    cheater_text = "Clicked too early. wait for green\nClick to play again"
    button.config(text=cheater_text, bg="lightblue", command=start_click)

# function that tracks duration of ms it takes to click button after turned green
def time_tracker():
    global start_time, your_time_result, best_time, your_best_time
    elapsed_time = math.floor((time.perf_counter() - start_time) * 1000)
    your_time_result = str(elapsed_time)
    your_time.config(text=f"{your_time_result} ms")
    button.config(text=f"{elapsed_time} ms\nClick to play again", bg="lightblue", command=start_click)

    if elapsed_time < best_time:
        best_time = elapsed_time
        your_best_time.config(text=f"{elapsed_time} ms")
    


# Button
button_text = "Press to start"
button = Button(text=button_text, font=("Arial, 20"), bd=0, bg="lightblue", command=start_click)
button.place(relx=.325, rely=.05, relwidth=.65, relheight=.90)

# scores background
background = Label(bg="#270049")
background.place(relx=.05, rely=.05, relwidth=.25, relheight=.8)

# Your time
your_time_text = Label(text="Your Time", font=("", 20, "bold"), bg="#270049", fg="white")
your_time_text.place(relx=.05, rely=.05, relwidth=.25, relheight=.10)
your_time_result = "Start to get score"
your_time = Label(text=your_time_result, bg="#270049", fg="white", font=(15))
your_time.place(relx=.05, rely=.15, relwidth=.25, relheight=.10)

# Your record
your_best_text = Label(text="Your Best Time", font=("", 20, "bold"), bg="#270049", fg="white")
your_best_text.place(relx=.05, rely=.35, relwidth=.25, relheight=.10)
your_best_result = "Start to get score"
your_best_time = Label(text=your_best_result, bg="#270049", fg="white", font=(15))
your_best_time.place(relx=.05, rely=.45, relwidth=.25, relheight=.10)

# World Average
average_text = Label(text="World Average", font=("", 20, "bold"), bg="#270049", fg="white")
average_text.place(relx=.05, rely=.65, relwidth=.25, relheight=.10)
average = "250 ms"
average = Label(text=average, bg="#270049", fg="white", font=(15))
average.place(relx=.05, rely=.75, relwidth=.25, relheight=.10)

# Copyright
copyright = Label(text="@Copyright Ray Min Productions", bg='#330060', fg="gold", font=(20))
copyright.place(relx=.05, rely=.88, relwidth=.25, relheight=.10)

# window
root.mainloop()