from Tkinter import *
from random import randint

master = Tk()


def startGame():
    w = Canvas(master, width=600, height=550)
    w.grid(row=0, column=0, columnspan=3, sticky=N+E+W+S)
    rectangle = w.create_rectangle(0, 0, 30, 30, fill="Green", tags="rectangle")
    food = w.create_oval(0, 0, 10, 10, fill="red", tags = "food")
    w.move(food, randint(10, 590), randint(10, 540))
    def move_rec(event):
        if event.keysym == "Up":
            w.move(rectangle, 0, -5)
        elif event.keysym == "Down":
            w.move(rectangle, 0, 5)
        elif event.keysym == "Right":
            w.move(rectangle, 5, 0)
        elif event.keysym == "Left":
            w.move(rectangle, -5, 0)
    w.bind_all('<Key>', move_rec)
def stop():
    master.destroy()

def instructions():
    newwin = Toplevel(master)
    display = Label(newwin, text="The goal of The Snake game is to eat the fruit to make the snake longer. " \
                     "Use the arrow keys to move the snake around the screen. " \
                    "If the snake's head touches any part of its body, the game is over, so be careful!" )
    
    display.pack()
    
b1 = Button(master, text="Start Game", command=startGame)
b1.grid(row=1, column=0, sticky=N+E+W+S)

b2 = Button(master, text="Quit", command=stop)
b2.grid(row=1, column=1, sticky=N+E+W+S)

b3 = Button(master, text="Instructions", command=instructions) 
b3.grid(row=1, column=2, sticky=N+E+W+S)
###################################################
#w = Canvas(master, width=600, height=550)
#w.grid(row=0, column=0, columnspan=3, sticky=N+E+W+S)
#rectangle = w.create_rectangle(0, 0, 30, 30, fill="Green", tags="rectangle")
#food = w.create_oval(0, 0, 10, 10, fill="red", tags = "food")
#w.move(food, randint(10, 590), randint(10, 540))
###################################################
#def move_rec(event):
 #   if event.keysym == "Up":
  #      w.move(rectangle, 0, -5)
   # elif event.keysym == "Down":
    #    w.move(rectangle, 0, 5)
    #elif event.keysym == "Right":
     #   w.move(rectangle, 5, 0)
    #elif event.keysym == "Left":
     #   w.move(rectangle, -5, 0)
#w.bind_all('<Key>', move_rec)
###################################################
mainloop()

