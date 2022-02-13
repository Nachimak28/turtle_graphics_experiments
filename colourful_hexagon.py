import turtle
from tqdm import tqdm


iterations = 1000
angle = 59


screen = turtle.Screen()
# screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
screen.bgcolor('black')

# initialize turtle object
coloured_hexagon = turtle.Turtle(visible=False)
coloured_hexagon.color('white')
# turtle tracer set to 0,0 to disable screen refreshing (more iterations make it slow)
turtle.tracer(0, 0)

# declare color constants
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# start drawing
for i in tqdm(range(1, iterations+1)):
    coloured_hexagon.pencolor(colors[i%6])
    coloured_hexagon.width(i/100+1)
    coloured_hexagon.forward(i)
    coloured_hexagon.left(angle)


# updates the whole figure at once
turtle.update()
ts = turtle.getscreen()

# to save the turtle images - can be opened with Ps or GIMP
ts.getcanvas().postscript(file=f"coloured_hexagon_{iterations}_iterations.eps")
turtle.done()

# exit screen
screen.mainloop()