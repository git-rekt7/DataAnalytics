# Min Max

# Value Assignment

a = input("PICK A NUMBER: ")
b = input("PICK ANOTHER NUMBER: ")
c = input("PICK ONE MORE NUMBER: ")

# What's the smallest number?

if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# What's the largest number?

if a >= b and a >= c:
    largest = a
elif b >= a and b >=c:
    largest = b
else:
    largest = c

# Output

print(f"The smallest number is: {smallest}")
print(f"The largest number is: {largest}")