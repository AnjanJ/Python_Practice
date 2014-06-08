import turtle


def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	#Aj.shape("turtle")
	#Aj.color("black")
	#Aj.speed(2)
	Aj = turtle.Turtle()
	Aj.forward(100)
	Aj.right(90)
	Aj.forward(100)
	Aj.right(90)
	Aj.forward(100)
	Aj.right(90)
	Aj.forward(100)
	Aj.right(90)

	window.exitonclick()

draw_square()