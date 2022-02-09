# substitutiion system
# X = Y + X + Y
# Y = X - Y - X
# angle of turning right - 60 degrees
# - (minus) = Turn left 60 degrees
# + (plus) = Turn right 60 degrees

import turtle
from tqdm import tqdm



replacement_mapping = {
    'X': 'Y+X+Y',
    'Y': 'X-Y-X'
}

iterations = 7
angle = 60
length = 5

def generate_sierpinski_sequence(original_string, iterations=3):
    output_string = original_string[:]
    for i in range(iterations):
        new_string = ''
        for char in output_string:
            if char == '+' or char == '-':
                new_string += char
            else:
                new_string += replacement_mapping[char]
        output_string = new_string
    return output_string


sierpinski_sequence = generate_sierpinski_sequence(original_string='X', iterations=iterations)

# generating the turtle graphic
# initializing a screen
screen = turtle.Screen()
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
screen.bgcolor('black')

# initialize turtle object
sierpinski_triangle = turtle.Turtle(visible=False)
sierpinski_triangle.color('white')
# turtle tracer set to 0,0 to disable screen refreshing (more iterations make it slow)
turtle.tracer(0, 0)
# first step
sierpinski_triangle.width(2)
sierpinski_triangle.left(60)
sierpinski_triangle.forward(length)

for i in tqdm(sierpinski_sequence):
    if i == '+':
        sierpinski_triangle.width(2)
        sierpinski_triangle.right(angle)
        sierpinski_triangle.forward(length)
    elif i == '-':
        sierpinski_triangle.width(2)
        sierpinski_triangle.left(angle)
        sierpinski_triangle.forward(length)

# updates the whole figure at once
turtle.update()
ts = turtle.getscreen()

# to save the turtle images - can be opened with Ps or GIMP
ts.getcanvas().postscript(file=f"sierpinski_triangle_{iterations}_iterations.eps")
turtle.done()

# exit screen
screen.mainloop()