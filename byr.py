from Tkinter import *
from time import sleep
from random import randint, choice

master = Tk()

score = 0
length = 3
def startGame():
    w = Canvas(master, width=600, height=550)
    w.grid(row=0, column=0, columnspan=3, sticky=N+E+W+S)

    # create rectangle (snake):
    snake = []
    x1 = 0
    y1 = 0
    x2 = 10
    y2 = 10
    head = w.create_rectangle(x1, y1, x2, y2, fill="Green", tags="head")
    snake.append(head)
    for i in range(1, length):
        x1 += 10
        x2 += 10
        rectangle = w.create_rectangle(x1, y1, x2, y2, fill="Green")
        snake.append(rectangle)

    # creating list of possible multiples of 10:
    def f(x):
        return (x % 10 == 0)

    listX = filter(f, range(10, 590))
    listY = filter(f, range(10, 540))

    foodX = choice(listX)
    foodY = choice(listY)
    
    food = w.create_oval(0, 0, 10, 10, fill="red", tags = "food")
    w.move(food, foodX, foodY)

    
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
        while (w.coords(head)[1] >= 0):
            # game over if it hits top
            if (w.coords(head)[1] == 0):
                master.destroy()
            else:
                if w.bbox("head") == w.bbox("food"):
                        food_toucher()

                x1 = w.coords(head)[0]
                y1 = w.coords(head)[1]
                x2 = w.coords(head)[2]
                y2 = w.coords(head)[3]
                w.move(head, 0, -10)
                
                for i in range(1, len(snake)):
                    x1, y1, x2, y2 = follow_head(i, x1, y1, x2, y2)
                    
                sleep(0.1)
                w.update()

    def move_down():
        while (w.coords(head)[3] <= 550):
            # game over if it hits bottom
            if (w.coords(head)[3] == 550):
                master.destroy()
            else:
                if w.bbox("head") == w.bbox("food"):
                        food_toucher()
                        
                x1 = w.coords(snake[0])[0]
                y1 = w.coords(snake[0])[1]
                x2 = w.coords(snake[0])[2]
                y2 = w.coords(snake[0])[3]
                w.move(snake[0], 0, 10)
                
                for i in range(1, len(snake)):
                    newx1 = w.coords(snake[i])[0]
                    newy1 = w.coords(snake[i])[1]
                    newx2 = w.coords(snake[i])[2]
                    newy2 = w.coords(snake[i])[3]
                    w.coords(snake[i], x1, y1, x2, y2)
                    x1 = newx1
                    y1 = newy1
                    x2 = newx2
                    y2 = newy2
                            
                sleep(0.1)
                w.update()

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

    def move_left():
        while (w.coords(head)[0] >= 0):
            # game over if it hits left wall
            if (w.coords(head)[0] == 0):
                master.destroy()
            else:
                if w.bbox("head") == w.bbox("food"):
                        food_toucher()

                x1 = w.coords(head)[0]
                y1 = w.coords(head)[1]
                x2 = w.coords(head)[2]
                y2 = w.coords(head)[3]
                w.move(head, -10, 0)
                
                for i in range(1, len(snake)):
                    x1, y1, x2, y2 = follow_head(i, x1, y1, x2, y2)
                    
                sleep(0.1)
                w.update()

    def move_right():
        while (w.coords(head)[2] <= 600):
            # game over if it hits right wall
            if (w.coords(head)[2] == 600):
                master.destroy()
            else:
                if w.bbox("head") == w.bbox("food"):
                        food_toucher()

                x1 = w.coords(head)[0]
                y1 = w.coords(head)[1]
                x2 = w.coords(head)[2]
                y2 = w.coords(head)[3]
                w.move(head, 10, 0)
                
                for i in range(1, len(snake)):
                    x1, y1, x2, y2 = follow_head(i, x1, y1, x2, y2)
                    
                sleep(0.1)
                w.update()
                
    w.bind_all('<Key>', move_snake)
    
    def food_toucher():
        # gives the coordinates where the food was touched at:
        print "Food touched at:"
        print w.bbox("head"), w.bbox("food")

        # increments and prints score:
        global score
        score += 1
        print score

        # new coordinates:
        new_x = choice(listX)
        new_y = choice(listY)
        
        # relocates the food somewhere else in the canvas.
        # to keep its size of 10 (decided upon create_oval creation) consistent,
        # use new_x and new_x + 10 when plotting new x values, likewise for y.
        w.coords(food, new_x, new_y, new_x + 10, new_y + 10)
        print "new ones:"
        print w.bbox("head"), w.bbox("food")




# what's called when 'quit' is pressed:
def stop():
    master.destroy()

# what's called when 'instructions' is pressed:
def instructions():
    newwin = Toplevel(master)
    display = Label(newwin, text="The goal of The Snake game is to eat the fruit to make the snake longer. " \
                     "Use the arrow keys to move the snake around the screen. " \
                    "If the snake's head touches any part of its body, the game is over, so be careful!",
                    length=100, width=100)
    
    display.pack()

############### Buttons ##################

# Start button:  
b1 = Button(master, text="Start Game", command=startGame)
b1.grid(row=1, column=0, sticky=N+E+W+S)

# Quit button:
b2 = Button(master, text="Quit", command=stop)
b2.grid(row=1, column=1, sticky=N+E+W+S)

# Instructions button:
b3 = Button(master, text="Instructions", command=instructions) 
b3.grid(row=1, column=2, sticky=N+E+W+S)

###################### create a GUI window #########################

# set the title
master.title("SNAKEGAME..RELOADED")

# start the GUI
master.mainloop()
