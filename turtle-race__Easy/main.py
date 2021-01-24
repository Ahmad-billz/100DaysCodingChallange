from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your Bet', prompt='Which turtle is going to win the race '
                                                          '\n(Orange, Red, Green, Purple, Blue, Black): ').lower()
y_pos = [100, 60, 20, -20, -60, -100]
color = ['orange', 'red', 'green', 'purple', 'blue', 'black']
all_turtles= []

for turtle_index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 225:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! - {winning_color} turtle is the winner")
            else:
                print(f"You lost! - {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()