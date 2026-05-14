# Meta
import random
import math
import statistics

# Variables
vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

#                   RANDOM SAMPLE 75
print("\n RANDOM SAMPLE 75")
print("\n ~~~~~~~~~~~~~~~~~~~")
print(f"The sum of 75 values is: {sum(vals_sample)}") # sum of 75 values 
print(f"The average of 75 values is: {statistics.mean(vals_sample):.2f}") # Mean of random val sample
print(f"The median of 75 values is: {statistics.median(vals_sample)}") # Median of random sample

#                   RANDOM SAMPLE 200
print("\n RANDOM SAMPLE 200")
print("\n ~~~~~~~~~~~~~~~~~~~")
print(f"Average of 200 Values is: {statistics.mean(vals_choices):.2f}")
print(f"Median of 200 Values is: {statistics.median(vals_choices):.2f}")
print(f"Mode of 200 Values is: {statistics.mode(vals_choices):.2f}")
print(f"Standard deviation of 200 Values is: {statistics.stdev(vals_choices):.2f}")
print(f"Variance of 200 Values is: {statistics.variance(vals_choices):.2f}")



#                   CIRCLE ROUNDED UP
r = random.uniform(0, 10) # random radius


area = pi * r**2 # area of circle

# round to nearest integer
r_rounded = math.ceil(r)
area_rounded = math.ceil(area)

print("\n CIRCLE ROUNDED UP")
print("\n ~~~~~~~~~~~~~~~~~~~~")
print("Radius:", r_rounded)
print("Area:", area_rounded)

#                   CIRCLE ROUNDED DOWN
r = random.uniform(0, 10) # random radius


area = pi * r**2 # area of circle

# round to nearest integer
r_rounded = math.floor(r)
area_rounded = math.floor(area)

print("\n CIRCLE ROUNDED DOWN")
print("\n ~~~~~~~~~~~~~~~~~~~~")
print("Radius:", r_rounded)
print("Area:", area_rounded)

