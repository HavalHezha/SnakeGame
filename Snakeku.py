from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random




def submit():
    global BACKGROUND_COLOR
    global SNAKE_COLOR
    global FOOD_COLOR
    BACKGROUND_COLOR = entry.get()
    SNAKE_COLOR = entry2.get()
    FOOD_COLOR = entry3.get()
    ask.destroy()
ask = tk.Tk()

ask.title("Snake Siting")
ask.resizable(False, False)
ask.geometry("400x200")

label10 = tk.Label(ask, text="Welcome To Snake Game , THIS game made by Nano(Haval)")
label10.pack(pady=10)
label = tk.Label(ask, text="Enter background color:")
label.pack()

entry = tk.Entry(ask)
entry.pack()

label2 = tk.Label(ask, text="Enter snake color:")
label2.pack()

entry2 = tk.Entry(ask)
entry2.pack()

label3 = tk.Label(ask, text="Enter food color:")
label3.pack()

entry3 = tk.Entry(ask)
entry3.pack()
submit_button = tk.Button(ask, text="Play", command=submit)
submit_button.pack()

ask.mainloop()


GAME_WIDTH = 1000
GAME_HEIGHT = 560
SPEED = 100
SPACE_SIZE = 30
BODY_PARTS = 3


class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinate = []
        self.squares = []
        for i in range(0, BODY_PARTS):
            self.coordinate.append([0, 0])

        for x, y in self.coordinate:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill= SNAKE_COLOR, tag="SNAKE_COLOR")
            self.squares.append(square)
class Food:

    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE)- 1) * SPACE_SIZE
        self.coordinate = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):
    global score

    x, y = snake.coordinate[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinate.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinate[0] and y == food.coordinate[1]:
        score += 1
        label.config(text="Score: {}".format(score))  # Corrected line
        canvas.delete("food")
        food = Food()  # You missed the parenthesis here; corrected
    else:
        del snake.coordinate[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)
def change_direction(new_direction):
    global direction
    if new_direction == 'left':
        if new_direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if new_direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if new_direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if new_direction != 'up':
            direction = new_direction

def check_collisions(snake):

    x, y = snake.coordinate[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    for body_part in snake.coordinate[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas',50), text="Game Over", fill="red", tag="GAMEOVERMSG")

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window,  text="Score:{}".format(score), font=('consolas', 40), background=SNAKE_COLOR)
label.pack()


canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/100) - (window_width/100))
y = int((screen_height/40) - (window_height/40))

window.geometry(f"{window_width}x{window_height}+{y}+{x}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
snake = Snake()
food = Food()

next_turn(snake, food)
window.mainloop()
