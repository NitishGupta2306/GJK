from math import sqrt
class Shape():
    # Points are an array of (x, y) tuples.
    def __init__(self, points):
        # All vectors are normalized.
        self.points = points
        self.normalized_points = self.normalize()
        self.center_point = self.center()
    
    def center(self):
        """
        Returns the center of the shape.
        """
        x_sum = 0
        y_sum = 0
        for point in self.normalized_points:
            x_sum += point[0]
            y_sum += point[1]
        return (x_sum / len(self.normalized_points), y_sum / len(self.normalized_points))

    def normalize(self):
        min_x = min(point[0] for point in self.points)
        max_x = max(point[0] for point in self.points)
        min_y = min(point[1] for point in self.points)
        max_y = max(point[1] for point in self.points)

        normalized_points = []
        for point in self.points:
            x = (point[0] - min_x) / (max_x - min_x)
            y = (point[1] - min_y) / (max_y - min_y)
            normalized_points.append((x, y))

        return normalized_points

    def furthest_point_from(self, d):
        max_distance = float('-inf')
        furthest_point = None

        for point in self.points:
            distance = sqrt((point[0] - d[0]) ** 2 + (point[1] - d[1]) ** 2)
            if distance > max_distance:
                max_distance = distance
                furthest_point = point

        return furthest_point
