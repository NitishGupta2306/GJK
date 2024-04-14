from Shape import Shape
from sklearn.preprocessing import normalize

#global variables:
origin = (0.0, 0.0)
d = tuple()

def GJK(ShapeA: Shape, ShapeB: Shape):

    # First simplex point using Minkowski Difference.
    simplex = [supportPoint(ShapeA, ShapeB)]

    # Original direction is the difference between the center points of the shapes.
    d = (ShapeA.center_point[0] - ShapeB.center_point[0], 
        ShapeA.center_point[1] - ShapeB.center_point[1])

    # New direction towards origin.
    d = (origin[0] - simplex[0][0], origin[1] - simplex[0][1])

    while True:
        # Point A is always the new point added.
        A = supportPoint(ShapeA, ShapeB)
        dot_product = sum(x * y for x, y in zip(A, d))

        # New point does not cross the origin. Making it impossible to enclose the origin.
        if dot_product < 0:
            return False
        simplex.append(A)

        if len(simplex) == 2:
            LineCase(simplex)
        else:
            TriangleCase(simplex)


def supportPoint(ShapeA: Shape, ShapeB: Shape):
 #Minkowski Difference for Two-dimensional Shapes.
    negated_d = (-d[0], -d[1])
    return (ShapeA.furthest_point_from(d)[0] - ShapeB.furthest_point_from(negated_d)[0] ,
            ShapeA.furthest_point_from(d)[1] - ShapeB.furthest_point_from(negated_d)[1])

def LineCase(simplex: list):
    A, B = simplex[1], simplex[0]

    vector_AB = (B[0] - A[0], B[1] - A[1]), 
    vector_A0 = (A[0] - origin[0], A[1] - origin[1])

    # (AB x A0) x AB gives us the perpendicular towards the origin.
    d = TripleProduct(vector_AB, vector_A0)
    
    # Line case always returns False as we can not enclose the origin with a line.
    return False

def TriangleCase(simplex: list):
    A, B, C = simplex[2], simplex[1], simplex[0]

    vector_AB = (B[0] - A[0], B[1] - A[1]), 
    vector_AC = (C[0] - A[0], C[1] - A[1]),
    vector_A0 = (A[0] - origin[0], A[1] - origin[1])

    


def TripleProduct(vector_AB: tuple, vector_A0: tuple):
    x1, y1 = vector_AB[1][0] - vector_AB[0][0], vector_AB[1][1] - vector_AB[0][1]
    x2, y2 = vector_A0[1][0] - vector_A0[0][0], vector_A0[1][1] - vector_A0[0][1]
    
    AB_A0 = x1 * y2 - x2 * y1
    
    x3,y3 = AB_A0[1][0] - AB_A0[0][0], AB_A0[1][1] - AB_A0[0][1]

    AB_A0_AB = x3 * y2 - x2 * y3
    return AB_A0_AB




            
    
 






# Test Cases

#Test Case 1: Circle inside of Square. Small value set.
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

ShapeB = Shape([
    (5, 5),
    (5, -5),
    (-5, -5),
    (-5, 5)])

GJK(ShapeA, ShapeB)