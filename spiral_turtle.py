import turtle
from tqdm import tqdm
# 180 spiral
# spiral_180 = turtle.Turtle()

# for i in tqdm(range(1, 181)):
#     spiral_180.forward(10)
#     spiral_180.left(i)

# turtle.done()



# 360 spiral
# spiral_360 = turtle.Turtle()

# for i in tqdm(range(1, 361)):
#     spiral_360.forward(20)
#     spiral_360.left(i)

# turtle.done()


# 360 spiral
spiral_360 = turtle.Turtle(visible=False)

for i in tqdm(range(1, 361)):
    spiral_360.forward(20)
    spiral_360.left(1)

turtle.done()