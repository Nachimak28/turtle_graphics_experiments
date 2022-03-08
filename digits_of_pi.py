import turtle
from tqdm import tqdm
from matplotlib import cm

iterations = 100000
# iterations = 10000
# iterations = 500
length = 4
theta = 36

def generate_n_digits_of_pi(n):
    """Generate n digits of Pi."""
    k,a,b,a1,b1 = 2,4,1,12,4
    pbar = tqdm(total=n)
    while n > 0:
        p,q,k = k * k, 2 * k + 1, k + 1
        a,b,a1,b1 = a1, b1, p*a + q*a1, p*b + q*b1
        d,d1 = a/b, a1/b1
        while d == d1 and n > 0:
            yield int(d)
            n -= 1
            a,a1 = 10*(a % b), 10*(a1 % b1)
            d,d1 = a/b, a1/b1
        pbar.update(1)
    pbar.close()

pi_decimal_digit_sequence = [str(n) for n in list(generate_n_digits_of_pi(iterations))]
joined_digits = "".join(pi_decimal_digit_sequence)

screen = turtle.Screen()
# screen.screensize(2000, 2000)
# screen.setworldcoordinates(1500, 1500, -1, -1)
# screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
# screen.setworldcoordinates(screen.window_width() - 1, screen.window_height() - 1, -1, -1)
screen.setworldcoordinates(screen.window_width() - 1, screen.window_height() - 1, -screen.window_width() + 1, -screen.window_height() + 1)
# screen.setworldcoordinates((screen.window_width() - 1), (screen.window_height() - 1)//2, -100, -100)
# screen.setworldcoordinates(0, 0, -10, -10)
screen.bgcolor('black')
screen.colormode(255)

# initializing the turtle object
pi_tracer = turtle.Turtle(visible=False)
pi_tracer.color('white')

# turtle tracer set to 0,0 to disable screen refreshing (more iterations make it slow)
turtle.tracer(0, 0)

pi_tracer.width(2)
# pi_tracer.left(60)
# pi_tracer.forward(length)

# pi_tracer.left(3*36)
# pi_tracer.forward(length)

colour_space = cm.get_cmap('hsv', 10)
colors = [colour_space(x, bytes=True)[:3] for x in range(10)]

for i in tqdm(joined_digits):
    pi_tracer.pencolor(colors[int(i)])
    pi_tracer.left(theta * int(i))
    pi_tracer.forward(length)
# for i in tqdm(sierpinski_sequence):
#     if i == '+':
#         sierpinski_triangle.width(2)
#         sierpinski_triangle.right(angle)
#         sierpinski_triangle.forward(length)
#     elif i == '-':
#         sierpinski_triangle.width(2)
#         sierpinski_triangle.left(angle)
#         sierpinski_triangle.forward(length)

# updates the whole figure at once
turtle.update()
ts = turtle.getscreen().getcanvas()
# ts = getscreen().getcanvas()
# ts.xview_moveto(-500)
# ts.yview_moveto(-500)

# to save the turtle images - can be opened with Ps or GIMP
ts.postscript(file=f"ditis_of_pi_{iterations}_decimal_places.eps")
turtle.done()

# exit screen
screen.mainloop()