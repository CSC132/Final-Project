from Tkinter import *
from time import sleep
from random import randint, choice
import RPi.GPIO as GPIO

red = 27
green = 18
blue = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red, False)
GPIO.output(blue, False)
GPIO.output(green, False)

master = Tk()

run = True
score = 0
speed = 0.05
snakeLength = 3
moveCount = 0

# booleans will be used to help prevent changing
# movement to the current opposite direction
goingLeft = False
goingRight = False
goingUp = False
goingDown = False

def startGame():
    global score
    GPIO.output(green, True)

    # canvas that runs the game:
    w = Canvas(master, width=600, height=550)
    w.grid(row=1, column=0, columnspan=3, sticky=N+E+W+S)
    master.attributes("-fullscreen", True)

    #scoreboard put on top of display
    scoreboard = Label(master, text="Score: {}".format(score))
    scoreboard.grid(row=0, column=1, sticky=N)
    
    # create rectangle (snake):
    snake = []
    x1 = 20
    y1 = 0
    x2 = 30
    y2 = 10
    head = w.create_rectangle(x1, y1, x2, y2, fill="Green", tags="head")
    snake.append(head)
    for i in range(1, snakeLength):
        x1 -= 10
        x2 -= 10
        rectangle = w.create_rectangle(x1, y1, x2, y2, fill="Green")
        snake.append(rectangle)

    # creating list of possible multiples of 10:
    def f(x):
        return (x % 10 == 0)

    listX = filter(f, range(10, 590))
    listY = filter(f, range(10, 540))

    foodX = choice(listX)
    foodY = choice(listY)
    poisonX = choice(listX)
    poisonY = choice(listY)

    # creating food and poison; changing their direction
    # using a random value from the list of multiples of 10:
    food = w.create_oval(0, 0, 10, 10, fill="red", tags = "food")
    w.move(food, foodX, foodY)
    poison = w.create_oval(0, 0, 10, 10, fill="purple", tags="poison")
    w.move(poison, poisonX, poisonY)
    
    # function called when an arrow key is pressed:
    def move_snake(event):
        global run
        run = True
        
        if event.keysym == "Up":
            move_up()
        elif event.keysym == "Down":
            move_down()
        elif event.keysym == "Left":
            move_left()
        elif event.keysym == "Right":
            move_right()

    def move_up():
        global goingDown, goingUp, goingLeft, goingRight, run
        goingUp = True
        goingRight = False
        goingLeft = False

        # only move up if it's not moving down
        if (goingDown == False):
            while (run == True and w.coords(head)[1] >= 0):
                # game over if it hits top
                if (w.coords(head)[1] == 0):
                    reset()
                else:
                    check_item()
                    move(0, -10)
                    sleep(speed)
                    w.update()

    def move_down():
        global goingDown, goingUp, goingLeft, goingRight, run
        goingDown = True
        goingRight = False
        goingLeft = False

        # only move down if it's not moving up
        if (goingUp == False):
            while (run == True and w.coords(head)[3] <= 550):
                # game over if it hits bottom
                if (w.coords(head)[3] == 550):
                    reset()
                else:
                    check_item()
                    move(0, 10)                    
                    sleep(speed)
                    w.update()

    def move_left():
        global goingDown, goingUp, goingLeft, goingRight, run
        goingLeft = True
        goingUp = False
        goingDown = False

        # only move left if it's not moving right        
        if (goingRight == False):
            while (run == True and w.coords(head)[0] >= 0):
                # game over if it hits left wall
                if (w.coords(head)[0] == 0):
                    reset()
                else:
                    check_item()                        
                    move(-10, 0)
                    sleep(speed)
                    w.update()

    def move_right():
        global goingDown, goingUp, goingLeft, goingRight, run
        goingRight = True
        goingUp = False
        goingDown = False

        # only move right if it's not moving left        
        if (goingLeft == False):
            while (run == True and w.coords(head)[2] <= 600):
                # game over if it hits right wall
                if (w.coords(head)[2] == 600):
                    reset()
                else:
                    check_item()
                    move(10, 0)
                    sleep(speed)
                    w.update()

    # checks collision between head and food/poison:
    def check_item():
        if w.bbox("head") == w.bbox("food"):
            food_toucher()
        elif w.bbox("head") == w.bbox("poison"):
            poison_toucher()

    # this function moves the head, and keeps track of the
    # coordinates of the previous body part. We need to keep
    # track of the previous body parts because every body part
    # but the head will be moving to the previous body part's
    # coordinates.
    def move(x, y):
        x1 = w.coords(head)[0]
        y1 = w.coords(head)[1]
        x2 = w.coords(head)[2]
        y2 = w.coords(head)[3]
        w.move(head, x, y)
        
        for i in range(1, len(snake)):
            x1, y1, x2, y2 = follow_head(i, x1, y1, x2, y2)

            # checking collision between head and other body parts:
            if w.coords(head) == w.coords(snake[i]):
                reset()      

    # keeps track of every coordinate from all body parts
    # and moves snake body according to its previous coords.
    def follow_head(i, x1, y1, x2, y2):
        newx1 = w.coords(snake[i])[0]
        newy1 = w.coords(snake[i])[1]
        newx2 = w.coords(snake[i])[2]
        newy2 = w.coords(snake[i])[3]
        w.coords(snake[i], x1, y1, x2, y2)
        x1 = newx1
        y1 = newy1
        x2 = newx2
        y2 = newy2
        return x1, y1, x2, y2            

    # handles score incrementing, speed changes,
    # and new food/poison placement:
    def food_toucher():
        # blink LED when it eats food:
        GPIO.output(green, False)
        sleep(0.1)
        GPIO.output(green, True)
        sleep(0.1)
        
        # gives the coordinates where the food was touched at:
        print "Food touched at:"
        print w.bbox("head"), w.bbox("food")

        # increments and prints score:
        global score
        score += 1
        print score
        
        scoreboard.destroy()
        newScoreboard = Label(master, text="Score: {}".format(score))
        newScoreboard.grid(row=0, column=1, sticky=N)
        
        
        global speed
        if (score >= 5 and score < 10):
            speed = 0.05/2
        elif (score >= 10):
            speed = 0.05/4

        # new coordinates:
        food_x = choice(listX)
        food_y = choice(listY)
        poison_x = choice(listX)
        poison_y = choice(listY)
        
        # relocates the food somewhere else in the canvas.
        # to keep its size of 10 (decided upon create_oval creation) consistent,
        # use new_x and new_x + 10 when plotting new x values, likewise for y.
        w.coords(food, food_x, food_y, food_x + 10, food_y + 10)
        w.coords(poison, poison_x, poison_y, poison_x + 10, poison_y + 10)
        print "new ones:"
        print w.bbox("head"), w.bbox("food")
        grow()
        
    def poison_toucher():
        # blink LED red if it ate poison:
        GPIO.output(green, False)
        GPIO.output(red, True)
        sleep(0.1)
        GPIO.output(red, False)
        sleep(0.1)
        GPIO.output(green, True)

        
        # gives the coordinates where the food was touched at:
        print "poison touched at:"
        print w.bbox("head"), w.bbox("poison")

        # increments and prints score:
        global score
        score -= 1
        print score
        
        scoreboard.destroy()
        newScoreboard = Label(master, text="Score: {}".format(score))
        newScoreboard.grid(row=0, column=1, sticky=N)

        global speed            
        if (score < 0):
            print "You've been poisoned"
            reset()
        if (score <= 5):
            speed *= 2
        elif (score <= 15):
            speed *= 2

        food_x = choice(listX)
        food_y = choice(listY)
        poison_x = choice(listX)
        poison_y = choice(listY)

        w.coords(food, food_x, food_y, food_x + 10, food_y + 10)
        w.coords(poison, poison_x, poison_y, poison_x + 10, poison_y + 10)
        print "new ones:"
        print w.bbox("head"), w.bbox("poison")

    # w.coords returns the x1, y1, x2, y2 values respectively,
    # so get coords of the tail (last item in the snake list)
    # and create the new rectangle with those coordinates
    def grow():
        x1, y1, x2, y2 = w.coords(snake[len(snake)-1])
        rectangle = w.create_rectangle(x1, y1, x2, y2, fill="Green")
        snake.append(rectangle)
        
    # destroys current snake, cleans up score and
    # direction sentinels, and calls statGame() again.
    def reset():
        global score, goingDown, goingUp, goingLeft, run

        GPIO.output(green, False)
        for i in range(0, 2):
            GPIO.output(red, True)
            sleep(0.5)
            GPIO.output(red, False)
            sleep(0.5)
            
        w.destroy()
        score = 0
        goingLeft = False
        goingRight = False
        goingUp = False
        goingDown = False
        run = False
        startGame()
        
    w.bind_all('<Key>', move_snake)

# what's called when 'quit' is pressed.
# cleanup GPIO pins and sets run = False
# so move function doesn't try to update
# one last time after destroying mainloop:
def stop():
    global run
    run = False   
    GPIO.cleanup()
    master.destroy()
    print "Goodbye"

# what's called when 'instructions' is pressed:
def instructions():
    newwin = Toplevel(master)
    display = Label(newwin, text="The goal of The Snake game is to eat the fruit\n to make the snake longer. " \
                     "\n\nUse the arrow keys to move the \nsnake around the screen. " \
                    "\n\nIf the snake's head touches any part of its body, \n the game is over, so be careful!",
                    height=20, width=40)
    
    display.pack()

############### Buttons ##################

# Start button:  
b1 = Button(master, text="Start Game", command=startGame)
b1.grid(row=2, column=0, sticky=N+E+W+S)

# Quit button:
b2 = Button(master, text="Quit", command=stop)
b2.grid(row=2, column=1, sticky=N+E+W+S)

# Instructions button:
b3 = Button(master, text="Instructions", command=instructions) 
b3.grid(row=2, column=2, sticky=N+E+W+S)

###################### create a GUI window #########################

# set the title
master.title("SNAKEGAME..RELOADED")

# start the GUI
master.mainloop()
