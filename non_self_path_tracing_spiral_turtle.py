import turtle
from tqdm import tqdm

# initializing a screen
nt = turtle.Screen()

# initialize turtle object
non_tracing_spiral = turtle.Turtle(visible=False)

# number of iterations
iterations = 10000
# change in theta value
degree_change = 1.02
# length of forward movement
length = 3

# progress bar
pbar = tqdm(total = iterations+1)

# turtle tracer set to 0,0 to disable screen refreshing (more iterations make it slow)
turtle.tracer(0, 0)

# main turtle loop
i = 0
degrees = 0
while i <= iterations:
    non_tracing_spiral.forward(length)
    degrees += degree_change
    non_tracing_spiral.left(degrees)
    i += 1
    pbar.update(1)

# updates the whole figure at once
turtle.update()
ts = turtle.getscreen()

# to save the turtle images - can be opened with Ps or GIMP
ts.getcanvas().postscript(file=f"non_tracing_spiral_{iterations}_iterations.eps")
turtle.done()

# exit screen
nt.mainloop()

