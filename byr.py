from Tkinter import *
from time import sleep
from random import randint

master = Tk()

######## Buttons ##################

def startGame():
    w = Canvas(master, width=600, height=550)
    w.grid(row=0, column=0, columnspan=3, sticky=N+E+W+S)

    # create rectangle (snake):
    rectangle = w.create_rectangle(0, 0, 30, 30, fill="Green", tags="rectangle")

    # create food:
    food = w.create_oval(0, 0, 10, 10, fill="red", tags = "food")
    w.move(food, randint(10, 590), randint(10, 540))

    # function called when an arrow key is pressed:
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
    
##    score = 0
##    def food_toucher():
##        for n in w.coords(rectangle):
##            for m in w.coords(food):
##                if ((n[0] == m[0]) or (n[1] == m[1]) or (n[2] == m[2])\
##                    or (n[3] == m[3])):
##                    w.move(food, randint(10, 590), randint(10, 540))
##                    score += 1
##                    print score
    
    

def stop():
    master.destroy()

def instructions():
    newwin = Toplevel(master)
    display = Label(newwin, text="The goal of The Snake game is to eat the fruit to make the snake longer. " \
                     "Use the arrow keys to move the snake around the screen. " \
                    "If the snake's head touches any part of its body, the game is over, so be careful!",
                    length=100, width=100)
    
    display.pack()
    
b1 = Button(master, text="Start Game", command=startGame)
b1.grid(row=1, column=0, sticky=N+E+W+S)

b2 = Button(master, text="Quit", command=stop)
b2.grid(row=1, column=1, sticky=N+E+W+S)

b3 = Button(master, text="Instructions", command=instructions) 
b3.grid(row=1, column=2, sticky=N+E+W+S)

###############################################################################


##w = Canvas(master, width=600, height=550)
##w.pack()
##w.grid(row=0, column=0, columnspan=3, sticky=N+E+W+S)

# rectangle
#rectangle = w.create_rectangle(0, 0, 30, 30, fill="blue", tags="rectangle")

##def move_snake(event):
##    if event.keysym == "Up":
##        move_up()
##    elif event.keysym == "Down":
##        move_down()
##    elif event.keysym == "Left":
##        move_left()
##    elif event.keysym == "Right":
##        move_right()
##
##
##def move_up():
##    while (w.coords(rectangle)[1] >= 0):
##        # game over if it hits top
##        if (w.coords(rectangle)[1] == 0):
##            master.destroy()
##        else:
##            w.move(rectangle, 0, -5)
##            sleep(0.02)
##            w.update()
##
##def move_down():
##    while (w.coords(rectangle)[3] <= 550):
##        # game over if it hits bottom
##        if (w.coords(rectangle)[3] == 550):
##            master.destroy()
##        else:
##            w.move(rectangle, 0, 5)
##            sleep(0.02)
##            w.update()
##
##def move_left():
##    while (w.coords(rectangle)[0] >= 0):
##        # game over if it hits left wall
##        if (w.coords(rectangle)[0] == 0):
##            master.destroy()
##        else:
##            w.move(rectangle, -5, 0)
##            sleep(0.02)
##            w.update()
##
##def move_right():
##    while (w.coords(rectangle)[2] <= 600):
##        # game over if it hits right wall
##        if (w.coords(rectangle)[2] == 600):
##            master.destroy()
##        else:
##            w.move(rectangle, 5, 0)
##            sleep(0.02)
##            w.update()

##w.bind_all('<Key>', move_snake)
###################################################################

###################### create a GUI window#########################

# set the title
master.title("SNAKEGAME..RELOADED")

# set the size
#master.geometry("600x550")

# start the GUI
master.mainloop()

