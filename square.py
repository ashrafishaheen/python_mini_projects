import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
def draw_win():
    window = turtle.Screen()
    window.bgcolor("red")
    #create the turtle brad -draws a sqaure
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.pencolor("yellow")
    brad.fillcolor("black")
    brad.speed(0.5)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #draw the circle here
    
    #ash = turtle.Turtle()
    #ash.shape("arrow")
    #ash.color("yellow")
    #ash.circle(100)
    
    window.exitonclick()

draw_win()

