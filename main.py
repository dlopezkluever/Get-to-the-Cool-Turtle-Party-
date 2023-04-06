from turtle import Turtle, Screen
from Classes import Player, Score
import random
import time

# screen set-up
screen = Screen()
screen.setup(510, 800)
screen.title("Get to the Cool Turtle Party!!")
screen.bgpic("Back_Image.png")
screen.tracer(0)
score = Score()

# cars graphic import!
screen.addshape("1.gif")
screen.addshape("2.gif")
screen.addshape("3.gif")
screen.addshape("4.gif")
screen.addshape("5.gif")
screen.addshape("6.gif")
screen.addshape("7.gif")
screen.addshape("10.gif")
screen.addshape("11.gif")
screen.addshape("12.gif")
screen.addshape("13.gif")
screen.addshape("14.gif")
screen.addshape("15.gif")
screen.addshape("16.gif")
shapes_list = ["1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif", "7.gif"]
shapes_list_backside = ["10.gif", "11.gif", "12.gif", "13.gif", "14.gif", "15.gif", "16.gif"]

# Creation of random y-coordinate locations, in the correct lanes
y_positions_left = []
o = 0
p = 0
y_positions_right = []
for _ in range(12):
    y = -312.5 + 50*o
    y_positions_left.append(y)
    o += 1

for _ in range(12):
    yy = -337.5 + 50*p
    y_positions_right.append(yy)
    p += 1

# Ernie is my brother, and in this game, the turtle: His call &
ernie = Player()
screen.listen()
screen.onkeypress(key="Up", fun=ernie.up)
screen.onkeypress(key="Down", fun=ernie.down)

# Car Creation, the cars are all in a list, needs to be updated every level... or I guess not?
cars = []
for _ in range(600):
    car = Turtle()
    coche = shapes_list[random.randint(0, 6)]
    car.shape(coche)
    car.pu()
    top_lane = random.choice(y_positions_left)
    car.setpos(-270, top_lane)
    cars.append(car)

cars_back = []
for _ in range(600):
    car = Turtle()
    coche = shapes_list_backside[random.randint(0, 6)]
    car.shape(coche)
    car.pu()
    car.setheading(180)
    bottom_lane = random.choice(y_positions_right)
    car.goto(270, bottom_lane)
    cars_back.append(car)

screen.tracer()
pop_up = Turtle()
pop_up.color("white")
pop_up.hideturtle()
goers = []
goers_back = []
chance_int = 60
velocity = 5
playing = True

while playing:
    # Car Creation Sequence
    chance = random.randint(1, chance_int)
    if chance <= 10:
        goer = random.choice(cars)
        goer_back = random.choice(cars_back)
        goer.speed("fastest")
        goer_back.speed("fastest")
        goers.append(goer)
        goers_back.append(goer_back)
    # time.sleep(.01)
    for goer in goers:
        goer.forward(velocity)
        if ernie.distance(goer) <= 15:
            playing = False
            pop_up.write("SPLAT!", align="center", font=("Arial", 30, "normal"))
            if score.high_score <= score.level:
                score.high_score = score.level
                New_high_score = str(score.high_score)
                with open("high_score.txt", mode="w") as zcore:
                    zcore.write(New_high_score)

    for goer_back in goers_back:
        goer_back.forward(velocity)
        if ernie.distance(goer_back) <= 15:
            playing = False
            pop_up.write("SPLAT!", align="center", font=("Arial", 30, "normal"))
            if score.high_score < score.level:
                score.high_score = score.level
                New_high_score = str(score.high_score)
                with open("high_score.txt", mode="w") as zcore:
                    zcore.write(New_high_score)
    screen.update()
    if ernie.ycor() >= 260:
        score.level += 1
        if chance_int <= 50:
            chance_int -= 2
        elif chance_int <= 30:
            chance_int -= 1
        else:
            chance_int -= 3
        velocity += 1
        screen.update()
        score.update_score()
        time.sleep(.25)
        ernie.resetinator()
        screen.update()

screen.exitonclick()
