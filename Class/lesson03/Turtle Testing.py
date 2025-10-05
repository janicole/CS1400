from turtle import * # This imports all the methods from the turtle module

window = Screen() # Creates a window object so we can see the results
my_turtle = Turtle() # Creates a turtle object to use to draw

# Your code to tell turtle what to do to make the drawing goes here!
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)


# This code asks the window to stay up until we click on it
# This makes it so we can actually see our drawing
# exitonclick is a method for the Screen object
window.exitonclick()