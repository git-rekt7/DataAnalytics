# If Basics

x = 100
y = 20

# if x/y is 5...
if x / y == 5:
    print("x divided by y is 5")
    x = 1
else:
    print("Are the variables set up correctly?")

# if x * y is y... 
if x * y == y:
    print("now x times y is y")
    x = 1
else:
    print(f"Whoops, x = {x}")

# X less than Y
if x < y:
    print("x is less than y")
    x = x * 2
else:
    print("uh oh, x is not less than y")

# X greater than Y
if x > y:
    print("How is x greater than y??")
else:
    print ("x is NOT greater than y")

# Final print statement
print("\nFINAL VALUES")
print("\n~~~~~~~~~~~~~")
print(f"The final value of x is {x} and the final value of y is {y}")