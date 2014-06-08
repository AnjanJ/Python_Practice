import turtle


def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	Aj = turtle.Turtle()
	Aj.shape("turtle")
	Aj.color("black")
	Aj.speed(2)
	Aj.forward(100)
	Aj.right(90)
	Aj.forward(100)
	Aj.right(90)
	Aj.forward(100)
	Aj.right(90)
	Aj.forward(100)
	Aj.right(90)
	


def draw_circle():
	anjan = turtle.Turtle()
	anjan.speed(2)
	anjan.circle(100)
	


def draw_triangle():
	anjan = turtle.Turtle()
	anjan.speed(2)
	anjan.forward(100)
	anjan.right(90)
	anjan.forward(100)
	anjan.right(135)
	anjan.forward(150)

	window.exitonclick()

draw_square()
draw_circle()
draw_triangle()