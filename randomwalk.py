# from random import choice
# import seaborn as sns
# import matplotlib.pyplot as plt
from datetime import datetime

# class RandomWalk():
#     def __init__(self, num_points=5000):
    
#         """Initialize attributes of a walk."""
#         self.num_points = num_points

#         # All walks start at (0, 0).
#         self.x_values = [0]
#         self.y_values = [0]
        
#         '''To make random decisions, we’ll store possible choices in a list and
#         use choice() to decide which choice to use each time a decision is made u.
#         We then set the default number of points in a walk to 5000—large enough
#         to generate some interesting patterns but small enough to generate walks
#         quickly v. Then at w we make two lists to hold the x- and y-values, and we
#         start each walk at point (0, 0).
#         Choosing Directions
#         We’ll use fill_walk(), as shown here, to fill our walk with points and determine
#         the direction of each step.'''

#     def fill_walk(self):
#         """Calculate all the points in the walk."""
#         # Keep taking steps until the walk reaches the desired length.
#         while len(self.x_values) < self.num_points:
            
#             # Decide which direction to go and how far to go in that direction.
#             x_direction = choice([1, -1])
#             x_distance = choice([0, 1, 2, 3, 4])
#             x_step = x_direction * x_distance
            
#             y_direction = choice([1, -1])
#             y_distance = choice([0, 1, 2, 3, 4])
#             y_step = y_direction * y_distance
            
#             # Rejecting moves that go nowhere.
#             if x_step == 0 and y_step == 0:
#                 continue
            
#             # Calculate the next x and y values.
#             next_x = self.x_values[-1] + x_step
#             next_y = self.y_values[-1] + y_step
#             self.x_values.append(next_x)
#             self.y_values.append(next_y)


# rw = RandomWalk()
# rw.fill_walk()

# sns.scatterplot( x = rw.x_values, y = rw.y_values, s = 15)
# plt.show()

# print([a for a in range(10) if a % 2])
# def my(n1, n2):
#     return n1 + n2

# my(1,2,3)

print(datetime(1970, 1, 1).strftime('%Y-%d-%B'))