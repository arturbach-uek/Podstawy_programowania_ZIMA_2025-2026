###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#

import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

## Draw figures
pen.penup()
pen.goto(-200, 100)
pen.pendown()
figures.draw_square(pen, 100)

pen.penup()
pen.goto(50, 100)
pen.pendown()
figures.draw_square(pen, 70)

pen.penup()
pen.goto(-200, -50)
pen.pendown()
figures.draw_triangle(pen, 100)

pen.penup()
pen.goto(50, -50)
pen.pendown()
figures.draw_triangle(pen, 70)

pen.penup()
pen.goto(-200, -200)
pen.pendown()
figures.draw_rectangle(pen, 120, 60)

pen.penup()
pen.goto(50, -200)
pen.pendown()
figures.draw_rectangle(pen, 150, 40)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
