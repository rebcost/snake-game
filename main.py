from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
from snake import Snake
from time import sleep

# -----------------------------------SETTINGS------------------------------------------
W = 600
H = 600
COLOR = "black"
DELAY = 0.1

screen = Screen()
screen.screensize(W,H)
screen.bgcolor(COLOR)
screen.title("Snake Game")
screen.tracer(0)

def refresh():
    screen.update()
    sleep(DELAY)

# ----------------------------------------------------------------------------------


snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

gameON = True

while gameON:
    refresh()
    snake.mover()

    # Detectar a colisão entre a comida e a cobra
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extender()
        score.add()

    # Detectar a colisão com a parede
    if snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() < -280 or snake.head.ycor() > 280:
        gameON = False
        score.gameOver()

    # Detecta a colisão com o corpo
    for seguimento in snake.seguimentos[1:]:
        if snake.head.distance(seguimento) < 10:
            gameON = False
            score.gameOver()

screen.exitonclick()