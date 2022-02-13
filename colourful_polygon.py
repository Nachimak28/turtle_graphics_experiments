import turtle
from tqdm import tqdm
from matplotlib import cm

iterations = 360
number_of_sides_of_polygon = 6
angle = (iterations//number_of_sides_of_polygon) - 1


screen = turtle.Screen()
# screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
screen.bgcolor('black')
screen.colormode(255)

# initialize turtle object
coloured_hexagon = turtle.Turtle(visible=False)
coloured_hexagon.color('white')
# turtle tracer set to 0,0 to disable screen refreshing (more iterations make it slow)
turtle.tracer(0, 0)

# declare color constants
colour_space = cm.get_cmap('hsv', number_of_sides_of_polygon)
colors = [colour_space(x, bytes=True)[:3] for x in range(number_of_sides_of_polygon)]

# start drawing
for i in tqdm(range(1, iterations+1)):
    coloured_hexagon.pencolor(colors[i%number_of_sides_of_polygon])
    coloured_hexagon.width(i/100+1)
    coloured_hexagon.forward(i)
    coloured_hexagon.left(angle)


# updates the whole figure at once
turtle.update()
ts = turtle.getscreen()

# to save the turtle images - can be opened with Ps or GIMP
ts.getcanvas().postscript(file=f"coloured_polygon_{iterations}_iterations_number_of_sides_{number_of_sides_of_polygon}.eps")
turtle.done()

# exit screen
screen.mainloop()