import math

side_1 = 10
side_2 = 15

squared_side_1 = side_1 ** 2
squared_side_2 = side_2 ** 2

hypotenuse_length = math.sqrt(squared_side_1 + squared_side_2)
print("The hypotenuse_length of a right triangle is", hypotenuse_length)

triangle_square = 1 / 2 * (side_1 * side_2)
print("The square of a right triangle is", triangle_square)