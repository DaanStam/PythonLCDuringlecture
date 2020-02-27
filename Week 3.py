import turtle

window = turtle.Screen()
window.bgcolor("lightblue")
window.title("Hello, Tess!")


leonardo = turtle.Turtle()
leonardo.color("yellow")
leonardo.pensize(8)

donatello = turtle.Turtle()
donatello.color("red")
donatello.pensize(5)

leonardo.forward(50)
leonardo.circle(300)

donatello.forward(30)
donatello.circle(300)

window.exitonclick()