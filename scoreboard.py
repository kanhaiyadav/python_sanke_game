from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.score = 0
        with open("high_score.txt", mode='r') as file:
            self.high_score = int(file.read())

    def update_score(self, position):
        self.clear()
        self.penup()
        self.goto(position)
        self.pendown()
        self.pencolor("yellow")
        self.hideturtle()
        self.write(arg=f"Score = {self.score}   High Score: {self.high_score}", align="center", font=("Rockwell", 14, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
            self.score = 0
            self.clear()
            self.write(arg=f"Score = {self.score}   High Score: {self.high_score}", align="center",
                       font=("Rockwell", 14, "normal"))

