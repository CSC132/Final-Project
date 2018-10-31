from Tkinter import *
from time import sleep
from random import randint

master = Tk()

# score that will be incremented as a
# global variable in food_touched() function:
score = 0

def startGame():
    w = Canvas(master, width=600, height=550)
    w.grid(row=0, column=0, columnspan=3, sticky=N+E+W+S)

    # create rectangle (snake):
    snake = []
    x1 = 0
    y1 = 0
    x2 = 10
    y2 = 10
        for rectangle in range(3):
            rectangle = w.create_rectangle(x1, y1, x2, y2, fill="Green", tags="rectangle")
        snake.append(rectangle)
        x1 += 10
        y1 += 10
        x2 += 10
        y2 += 10
    print snake
    
    #print snake

    # create food and place it on canvas:
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
                # bbox returns a list of integers that
                # encapsulates/bounds the object.
                # if they are EXACTLY equal, snake ate food.
                # (every move function will behave this way.
                #  improvements to come).
                if w.bbox("rectangle") == w.bbox("food"):
                        food_toucher()
                w.move(rectangle, 0, -1)
                sleep(0.001)
                w.update()

    def move_down():
        while (w.coords(rectangle)[3] <= 550):
            # game over if it hits bottom
            if (w.coords(rectangle)[3] == 550):
                master.destroy()                
            else:
                if w.bbox("rectangle") == w.bbox("food"):
                        food_toucher()
                w.move(rectangle, 0, 1)
                sleep(0.001)
                w.update()

    def move_left():
        while (w.coords(rectangle)[0] >= 0):
            # game over if it hits left wall
            if (w.coords(rectangle)[0] == 0):
                master.destroy()
            else:
                if w.bbox("rectangle") == w.bbox("food"):
                        food_toucher()
                w.move(rectangle, -1, 0)
                sleep(0.001)
                w.update()

    def move_right():
        while (w.coords(rectangle)[2] <= 600):
            # game over if it hits right wall
            if (w.coords(rectangle)[2] == 600):
                master.destroy()
            else:
                if w.bbox("rectangle") == w.bbox("food"):
                        food_toucher()
                w.move(rectangle, 1, 0)
                sleep(0.001)
                w.update()
                
    w.bind_all('<Key>', move_snake)
    
    def food_toucher():
        # gives the coordinates where the food was touched at:
        print "Food touched at:"
        print w.coords(rectangle), w.coords(food)
        print w.bbox("rectangle"), w.bbox("food")

        # increments and prints score:
        global score
        score += 1
        print score 

        # new coordinates:
        new_x = randint(10, 590)
        new_y = randint(10,540)
        
        # relocates the food somewhere else in the canvas.
        # to keep its size of 10 (decided upon create_oval creation) consistent,
        # use new_x and new_x + 10 when plotting new x values, likewise for y.
        w.coords(food, new_x, new_y, new_x + 10, new_y + 10)
        print "new ones:"
        print w.coords(rectangle), w.coords(food)
        print w.bbox("rectangle"), w.bbox("food")
    

# what's called when 'quit' is pressed:
def stop():
    master.destroy()

# what's called when 'instructions' is pressed:
def instructions():
    newwin = Toplevel(master)
    display = Label(newwin, text="The goal of The Snake game is to eat the fruit to make the snake longer. " \
                     "Use the arrow keys to move the snake around the screen. " \
                    "If the snake's head touches any part of its body, the game is over, so be careful!")
    
    display.pack()

######################### Buttons #################################

# Start button:  
b1 = Button(master, text="Start Game", command=startGame)
b1.grid(row=1, column=0, sticky=N+E+W+S)

# Quit button:
b2 = Button(master, text="Quit", command=stop)
b2.grid(row=1, column=1, sticky=N+E+W+S)

# Instructions button:
b3 = Button(master, text="Instructions", command=instructions) 
b3.grid(row=1, column=2, sticky=N+E+W+S)

###################### create a GUI window#########################

# set the title
master.title("SNAKEGAME..RELOADED")

# start the GUI
master.mainloop()