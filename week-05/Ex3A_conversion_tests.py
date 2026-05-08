# Description: This script tests various numeric
# conversion techniques
# Author: Corey Allen

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '


#   interger conversion for A
# interger = int(a)
# print(interger)
#       ERROR

print("\n Conversion Results")
print("\n ~~~~~~~~~~~~~~~~~~~")

# interger conversion for B
interger_b = int(b)
print(f"Interger Value for B: {interger_b}")
# prints 55

# interger conversion for C
# interger_c = int(c)
# print(interger_c)
#       ERROR 

# interger conversion for D
# interger_d = int(d)
# print(interger_d)
#       ERROR

# float conversion
# float conversion for A
float_a = float(a)
print(f"Float Conversion for A: {float_a}")
# returns a as float

float_b = float(b)
print(f"Float Value for B: {float_b}")
# returns b as float (55.0)

# float_c = float(c)
# print(float_c)
#       ERROR

# float_d = float(d)
# print(float_d)
#       ERROR

# Variable a float & interger


Flint = int(float(a))
print(f"Float & Interger value: {Flint}")
# returns the value as a float and interger

# Sliced variable
Sliced = (a[:3])
print(f"The variable a has been sliced into: {Sliced}")
# returns a slice of the variable a

# Stripped Vars
StrippedA = (a.strip())
print(f"Stripped version of variable a {StrippedA}")

StrippedD = (d.strip())
print(f"Stripped version of variable d {StrippedD}")