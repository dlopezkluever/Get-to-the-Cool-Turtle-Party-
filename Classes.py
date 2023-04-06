from turtle import Turtle, Screen


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(.75)
        self.color('green')
        self.pu()
        self.setheading(90)
        self.setpos(0, -387.5)

    def resetinator(self):
        self.goto(0, -387.5)
        self.setheading(90)

    def up(self):
        self.forward(25)
        self.pu()

    def down(self):
        self.backward(25)
        self.pu()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt") as zcore:
            score_text = int(zcore.read())
        self.high_score = score_text
        self.shape("turtle")
        self.hideturtle()
        self.shapesize(.8)
        self.color()
        self.pu()
        self.setpos(-150, -380)
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level} High Score:{self.high_score}", font=("Arial", 20, "normal"), align="left")


# NOT USED

# class Car(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.pu()
#         self.carz = []
#         self.carz_back = []
#         self.goers = []
#         self.goers_back = []
#
#     def cars_go_brr(self, ypositionsA, ypositionsB, shapes_list, shapes_list_backside):
#         for _ in range(600):
#             car = Turtle()
#             coche = shapes_list[random.randint(0, 6)]
#             car.shape(coche)
#             car.pu()
#             top_lane = random.choice(ypositionsA)
#             car.setpos(-290, top_lane)
#             self.carz.append(car)
#
#         for _ in range(600):
#             car = Turtle()
#             coche = shapes_list_backside[random.randint(0, 6)]
#             car.shape(coche)
#             car.pu()
#             car.setheading(180)
#             bottom_lane = random.choice(ypositionsB)
#             car.goto(290, bottom_lane)
#             self.carz_back.append(car)
#
#     def cars_going(self):
#         goer = random.choice(self.carz)
#         goer_back = random.choice(self.carz_back)
#         goer.speed("fastest")
#         goer_back.speed("fastest")
#         self.goers.append(goer)
#         self.goers_back.append(goer_back)
#         for goer in self.goers:
#             goer.forward(20)
#         for goer_back in self.goers_back:
#             goer_back.forward(20)


# def cars_go_brr():
#     aim = random.choice(direction)
#     coche = shapes_list[random.randint(0, 7)]
#     car.shape(coche)
#     car.setheading(aim)
#     if car.heading == 0:
#         top_lane = random.choice(ypositionsA)
#         car.goto(-270, top_lane)
#     else:
#         bottom_lane = random.choice(ypositionsB)
#         car.goto(270, bottom_lane)
