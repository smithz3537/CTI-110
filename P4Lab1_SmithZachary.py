
# Name: Zachary Smith
# Assignment: P4LAB1
# Date: 10/25/2026
# Description: Draws a house using turtle graphics and loops.

# Pseudocode:
# 1. Import the turtle library.
# 2. Create a turtle and change the background and turtle colors.
# 3. Use a for loop to draw a square for the house.
# 4. Move the turtle to the top of the square.
# 5. Use a while loop to draw a triangle for the roof.
# 6. Finish the drawing and keep the window open.

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("My Turtle House")

# Create the turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("purple")
t.speed(5)

# Draw the square (house body) using a for loop
t.fillcolor("gold")
t.begin_fill()

for side in range(4):
    t.forward(200)
    t.left(90)

t.end_fill()

# Move turtle to the top-left corner of the square
t.penup()
t.goto(0, 200)
t.setheading(0)
t.pendown()

# Draw the triangle (roof) using a while loop
t.fillcolor("firebrick")
t.begin_fill()

count = 0

while count < 3:
    t.forward(200)
    t.left(120)
    count += 1

t.end_fill()

# Hide turtle and keep the window open
t.hideturtle()
turtle.done()
