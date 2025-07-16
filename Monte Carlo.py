import random
import matplotlib.pyplot as plt
plt.style.use('dark_background')

INTERVAL = 1000

circle_points = 0
square_points = 0

# Lists to store x, y values for points inside and outside the circle
inside_circle_x = []
inside_circle_y = []
outside_circle_x = []
outside_circle_y = []

# Total Random numbers generated= possible x
# values * possible y values
for i in range(INTERVAL ** 2):
    # Randomly generated x and y values from a
    # uniform distribution
    # Range of x and y values is -1 to 1
    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)

    # Distance between (x, y) from the origin
    origin_dist = rand_x ** 2 + rand_y ** 2

    # Checking if (x, y) lies inside the circle
    if origin_dist <= 1:
        circle_points += 1
        inside_circle_x.append(rand_x)
        inside_circle_y.append(rand_y)
    else:
        outside_circle_x.append(rand_x)
        outside_circle_y.append(rand_y)

    square_points += 1

# Estimating value of pi,
# pi= 4*(no. of points generated inside the
# circle)/ (no. of points generated inside the square)
pi = 4 * circle_points / square_points

# Plotting the points
plt.figure(figsize=(8, 8))
plt.scatter(inside_circle_x, inside_circle_y, color='blue', label='Inside Circle')
plt.scatter(outside_circle_x, outside_circle_y, color='red', label='Outside Circle')
plt.title('Monte Carlo Simulation for Pi Estimation')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Printing the final estimation of Pi
print("Final Estimation of Pi=", pi)
