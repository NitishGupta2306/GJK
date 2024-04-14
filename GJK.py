from Shape import Shape
from sklearn.preprocessing import normalize
import numpy as np


#global variables:
origin = (0.0, 0.0)

def GJK(ShapeA: Shape, ShapeB: Shape):

    # Original direction is the difference between the center points of the shapes.
    d = [ShapeB.center_point[0] - ShapeA.center_point[0], 
        ShapeB.center_point[1] - ShapeA.center_point[1]]
    
    # First simplex point using Minkowski Difference.
    simplex = [supportPoint(ShapeA, ShapeB, d)]

    # New direction towards origin.
    d = [origin[0] - simplex[0][0], origin[1] - simplex[0][1]]

    while True:
        # Point A is always the new point added.
        A = supportPoint(ShapeA, ShapeB, d)
        dot_product = sum(x * y for x, y in zip(A, d))

        # New point does not cross the origin. Making it impossible to enclose the origin.
        if dot_product < 0:
            return False
        simplex.append(A)

        if simplexHandler():
            return True

def supportPoint(ShapeA: Shape, ShapeB: Shape, d):
 #Minkowski Difference for Two-dimensional Shapes.
    negated_d = [-x for x in d]
    return (ShapeA.furthest_point_from(d)[0] - ShapeB.furthest_point_from(negated_d)[0] ,
            ShapeA.furthest_point_from(d)[1] - ShapeB.furthest_point_from(negated_d)[1])

def simplexHandler(simplex: list):
    if len(simplex) == 2:
       return LineCase(simplex)
    return TriangleCase(simplex)

def LineCase(simplex: list):
    A, B = simplex[1], simplex[0]

    vector_AB = (B[0] - A[0], B[1] - A[1]), 
    vector_A0 = (A[0] - origin[0], A[1] - origin[1])

    # (AB x A0) x AB gives us the perpendicular towards the origin.
    d = TripleProduct(vector_AB, vector_A0, vector_AB)
    
    # Line case always returns False as we can not enclose the origin with a line.
    return False

def TriangleCase(simplex: list):
    A, B, C = simplex[2], simplex[1], simplex[0]

    vector_AB = (B[0] - A[0], B[1] - A[1]), 
    vector_AC = (C[0] - A[0], C[1] - A[1]),
    vector_A0 = (A[0] - origin[0], A[1] - origin[1])

    perpendicular_AB = TripleProduct(vector_AC,vector_AB,vector_AC)
    perpendicular_AC = TripleProduct(vector_AB,vector_AC,vector_AC)

    dot_product_AB = sum(x * y for x, y in zip(perpendicular_AB, vector_A0))
    dot_product_AC = sum(x * y for x, y in zip(perpendicular_AC, vector_A0))

    if dot_product_AB > 0:
        # Origin outside of triangle. In region beyond AB.
        simplex.remove(C)
        d = perpendicular_AB
        return False
    if dot_product_AC > 0:
        # Origin outside of triangle. In region beyond AC.
        simplex.remove(B)
        d = perpendicular_AC
        return False

    return True

def TripleProduct(vector1: tuple, vector2: tuple, vector3):
    x1, y1 = vector1[1][0] - vector1[0][0], vector1[1][1] - vector1[0][1]
    x2, y2 = vector2[1][0] - vector2[0][0], vector2[1][1] - vector2[0][1]
    x3, y3 = vector3[1][0] - vector3[0][0], vector3[1][1] - vector3[0][1]
    
    V1xV2 = x1 * y2 - x2 * y1
    
    x4,y4 = V1xV2[1][0] - V1xV2[0][0], V1xV2[1][1] - V1xV2[0][1]

    V1xV2xV3 = x4 * y3 - x3 * y4
    return V1xV2xV3

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

print(GJK(ShapeA, ShapeB))
