from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.print_score()

    def print_score(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score +=1
        self.print_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)