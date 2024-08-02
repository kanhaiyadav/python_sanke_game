from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
posi = [(0, 0), (-10, 0), (-20, 0)]


class Snake:
    segments = []

    def __init__(self):
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in posi:
            self.add_segment(position)

    def add_segment(self, position):
        timmy = Turtle(shape="square")
        timmy.color("white")
        timmy.penup()
        if not self.segments:
            timmy.color("orange")
            timmy.shape("circle")
        timmy.shapesize(stretch_len=0.5, stretch_wid=0.5)
        timmy.goto(position)
        self.segments.append(timmy)

    def extend(self, position):
        self.add_segment(position)

    def move_forward(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[i - 1].xcor()
            y_cor = self.segments[i - 1].ycor()
            self.segments[i].goto(x_cor, y_cor)

        self.segments[0].forward(10)

    def reset_snake(self):
        for seg in self.segments:
            seg.reset()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(0)
