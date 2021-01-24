from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('cyan')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        ran_x = random.randint(-285, 285)
        ran_y = random.randint(-285, 285)
        self.goto(ran_x, ran_y)

