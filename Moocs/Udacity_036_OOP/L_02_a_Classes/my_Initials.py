import turtle


def draw_intials():
	window = turtle.Screen()
	window.bgcolor("red")

	
	draw = turtle.Turtle()
	draw.shape("turtle")
	draw.speed(1)
	draw.left(90)
	draw.forward(100)
	draw.right(90)
	draw.forward(25)
	draw.right(90)
	draw.forward(100)
	#Aj.right(90)
	draw.back(50)
	draw.right(90)
	draw.forward(25)
	draw.home()
	draw.penup()
	#draw.setpos(180)
	draw.forward(100)
	draw.pendown()
	draw.forward(50)
	draw.left(90)
	draw.forward(100)
	draw.left(90)
	draw.forward(35)
	draw.back(70)
	draw.forward(35)


	window.exitonclick()

draw_intials()