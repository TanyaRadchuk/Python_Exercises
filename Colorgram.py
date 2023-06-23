import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
color_list = [(225, 233, 238), (237, 34, 109), (153, 24, 65),
              (240, 73, 34), (7, 147, 92), (218, 170, 46), (179, 158, 44),
              (25, 123, 190), (44, 190, 232), (83, 20, 77), (244, 220, 47),
              (252, 223, 1), (125, 192, 84), (183, 39, 104), (207, 63, 24),
              (56, 172, 103), (170, 24, 19), (205, 133, 166), (4, 106, 45), (27, 176, 211),
              (237, 163, 193), (241, 167, 157), (162, 212, 180), (103, 1, 1), (141, 212, 231),
              (0, 81, 25), (158, 192, 227)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots +1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
