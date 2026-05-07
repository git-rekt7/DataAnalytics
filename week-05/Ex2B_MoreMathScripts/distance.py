# Calculating Distance with Python

# Meta
import math

# X and Y values
x1 = float(input("Enter the first x value: "))
y1 = float(input("Enter the first y value: "))
x2 = float(input("Enter a second x value: "))
y2 = float(input("Enter a second y value: "))


# Ordered pairs (as tuples)
ordered_pair1 = (x1, y1)
ordered_pair2 = (x2, y2)



# Distance math
distance = math.dist(ordered_pair1, ordered_pair2)
# Result
print(f"The distance between the two points is {distance:.2f} units.")