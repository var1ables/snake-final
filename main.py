from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#screen commands
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

#import snake and food from their files
snake = Snake()
food = Food()
scoreboard = Scoreboard()


#definited the controls
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right,'Right')


#game loop created
game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detecting collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()


    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game = False
        scoreboard.game_over()

    #detect collisions with snake body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game = False
            scoreboard.game_over()

screen.exitonclick()
