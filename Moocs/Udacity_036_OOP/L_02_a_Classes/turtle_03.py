import turtle


def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")


	anjan = turtle.Turtle()
	anjan.speed(2)
	anjan.forward(100)
	anjan.right(90)
	anjan.forward(100)
	anjan.right(135)
	anjan.forward(150)

	window.exitonclick()

draw_square()