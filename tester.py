# class Shape:
#     def __init__(self, points):
#         self.points = points

#     def center_point(self):
#         num_points = len(self.points)
#         sum_x = sum(point[0] for point in self.points)
#         sum_y = sum(point[1] for point in self.points)
#         center_x = sum_x / num_points
#         center_y = sum_y / num_points
#         return (center_x, center_y)

# # Define the ShapeA object
# ShapeB = Shape([
#     (5, 5),
#     (5, -5),
#     (-5, -5),
#     (-5, 5)])

# # Get the center point
# center = Shape.center_point()
# print("Center point:", center)

import matplotlib.pyplot as plt

class Shape:
    def __init__(self, points):
        self.points = points

    def plot(self, label=None):
        # Separate x and y coordinates
        x_values = [point[0] for point in self.points]
        y_values = [point[1] for point in self.points]
        
        # Plot the points
        plt.plot(x_values, y_values, marker='o', linestyle='-', label=label)

# Define ShapeA
ShapeA = Shape([
    (5.0, 0.0),
    (4.045084971874737, 2.938926261462366),
    (1.5450849718747373, 4.755282581475767),
    (-1.5450849718747366, 4.755282581475767),
    (-4.045084971874737, 2.938926261462366),
    (-5.0, 1.2246467991473532e-15),
    (-4.045084971874737, -2.938926261462365),
    (-1.5450849718747358, -4.755282581475767),
    (1.5450849718747364, -4.755282581475767),
    (4.045084971874736, -2.938926261462365)
])

# Define ShapeB
ShapeB = Shape([
    (5, 5),
    (5, -5),
    (-5, -5),
    (-5, 5)
])

# Plot both shapes
plt.figure(figsize=(6, 6))

ShapeA.plot(label='ShapeA')
ShapeB.plot(label='ShapeB')

plt.title('Plot of Shapes')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.axis('equal')  # Set equal scale for x and y axes
plt.legend()
plt.show()