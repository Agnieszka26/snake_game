from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as high_score:
            self.high_score = int(high_score.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.print_score()

    def print_score(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score +=1
        self.print_score()

    def update_high_score(self):
        with open("high_score.txt", mode="w") as w_high_score:
            w_high_score.write(str(self.high_score))

    def end_game(self):
        self.goto(0,0)
        self.write("END GAME", align=ALIGNMENT, font=FONT)
        self.update_score()
        self.update_high_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score=0
        self.update_score()
