from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-270,260)
        self.update()
        self.hideturtle()

    def update(self):
        self.write(f"Level: {self.level}", font=FONT)


    def increase_level(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.hideturtle()
        self.goto(-50,0)
        self.write("GAME OVER", font=FONT)

