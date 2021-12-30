from turtle import Turtle

SCORE_COLOR = "white"
ALIGN = "center"
FONT = ("Arial", 24, "normal")
SCORE_POSITION = (0,270)

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color(SCORE_COLOR)
        self.penup()
        self.goto(SCORE_POSITION[0], SCORE_POSITION[1])       
        self.hideturtle()
        self.update_score()

    def add(self):
        self.score += 1
        self.clear()
        self.update_score()  

    def update_score(self):
        self.write(f"Pontos: {self.score}",align=ALIGN, font=FONT)

    def gameOver(self):
        self.goto(0,0)
        self.write(f"Game Over",align=ALIGN, font=FONT)
        
