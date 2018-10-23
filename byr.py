from Tkinter import *
from time import sleep
from random import randint

master = Tk()

######## Buttons ##################

def sayHi():
    print "Hi"
    
def quitGame():
    master.destroy()

b1 = Button(master, text="Start Game", command=sayHi)
b1.grid(row=1, column=0, sticky=E)

b2 = Button(master, text="Quit", command=quitGame)
b2.grid(row=1, column=1, sticky=S)

###################################


w = Canvas(master, width=600, height=550)
w.pack()
w.grid(row=0, column=0, columnspan=3, sticky=N+E+W+S)

# rectangle
rectangle = w.create_rectangle(0, 0, 30, 30, fill="blue", tags="rectangle")

def move_snake(event):
    if event.keysym == "Up":
        move_up()
    elif event.keysym == "Down":
        move_down()
    elif event.keysym == "Left":
        move_left()
    elif event.keysym == "Right":
        move_right()


def move_up():
    while (w.coords(rectangle)[1] >= 0):
        # game over if it hits top
        if (w.coords(rectangle)[1] == 0):
            master.destroy()
        else:
            w.move(rectangle, 0, -5)
            sleep(0.02)
            w.update()

def move_down():
    while (w.coords(rectangle)[3] <= 550):
        # game over if it hits bottom
        if (w.coords(rectangle)[3] == 550):
            master.destroy()
        else:
            w.move(rectangle, 0, 5)
            sleep(0.02)
            w.update()

def move_left():
    while (w.coords(rectangle)[0] >= 0):
        # game over if it hits left wall
        if (w.coords(rectangle)[0] == 0):
            master.destroy()
        else:
            w.move(rectangle, -5, 0)
            sleep(0.02)
            w.update()

def move_right():
    while (w.coords(rectangle)[2] <= 600):
        # game over if it hits right wall
        if (w.coords(rectangle)[2] == 600):
            master.destroy()
        else:
            w.move(rectangle, 5, 0)
            sleep(0.02)
            w.update()

w.bind_all('<Key>', move_snake)


###################### create a GUI window

# set the title
master.title("SNAKEGAME..RELOADED")

# set the size
master.geometry("700x600")

# start the GUI
master.mainloop()

