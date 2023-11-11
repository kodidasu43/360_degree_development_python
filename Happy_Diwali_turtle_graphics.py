import turtle

# Initialize the turtle
t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()

# Set the window size and background color
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

# Define the colors for the text
colors = ["gold", "orange", "red", "yellow", "green", "blue", "indigo", "violet","gold", "orange", "red", "yellow",]

# Write the text "Happy Diwali"
for i, char in enumerate("Happy Diwali"):
    t.goto(-320 + i * 50, 150)
    t.pendown()
    t.pencolor(colors[i])
    t.write(char, font=("Arial", 50, "bold"))
    t.penup()

# # Draw a rangoli design
# t.goto(-200, -150)
# t.pendown()
# t.pencolor("white")
# t.pensize(5)

# for i in range(6):
    # for j in range(6):
        # t.forward(30)
        # t.right(60)
        # t.forward(30)
        # t.right(60)
        # t.forward(30)
        # t.right(60)
        # t.forward(30)
        # t.right(60)

# t.penup()

# Draw firecrackers
for i in range(5):
    t.goto(-300 + i * 100, -250)
    t.pendown()
    t.pencolor("red")
    t.pensize(3)

    for j in range(5):
        t.forward(10)
        t.right(45)
        t.forward(10)
        t.left(90)

    t.penup()

# Keep the window open until it is closed by the user
screen.mainloop()