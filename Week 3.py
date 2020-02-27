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
leonardo.left(120)
leonardo.forward(50)
leonardo.left(120)
leonardo.forward(50)
leonardo.right(120)
leonardo.forward(100)

donatello.forward(300)
donatello.left(90)
donatello.forward(200)
donatello.circle(300)

window.exitonclick()