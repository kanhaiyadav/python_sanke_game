from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score
window = Screen()
window.setup(width=600, height=600)
window.title("My Snake Game")
window.bgcolor("black")
window.tracer(0)

state = True
snake = Snake()
food = Food()

window.listen()
window.onkey(key="Up", fun=snake.up)
window.onkey(key="Down", fun=snake.down)
window.onkey(key="Left", fun=snake.left)
window.onkey(key="Right", fun=snake.right)

writer = Score()
writer.update_score(position=(0, 280))

while state:
    window.update()
    time.sleep(0.08)
    snake.move_forward()
    if snake.head.distance(food) < 15:
        writer.score += 1
        snake.add_segment(snake.segments[-1].position())
        food.refresh()
        writer.update_score(position=(0, 280))
    if snake.head.xcor() > 285 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        writer.reset_score()
        snake.reset_snake()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 2:
            writer.reset_score()
            snake.reset_snake()
window.exitonclick()
