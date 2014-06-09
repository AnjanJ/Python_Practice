import turtle

def draw_square(name_of_tutrrle):

	for i in range(1,5):
		name_of_tutrrle.forward(100)
		name_of_tutrrle.right(90)

def draw_cir():
	window = turtle.Screen()
	window.bgcolor("red")
	anjan = turtle.Turtle()
	for i in range(1,37):
		draw_square(anjan)
		anjan.right(10)
	window.exitonclick()

draw_cir()

