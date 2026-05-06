# Sample problem: How do you calculate the total due at a restaurant given the food cost,
# tax, and tip?

# Define known values
food_cost = 79.25
tax = 6.54
tip = float(input("How much will you tip? "))

# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results
# print ("The total due is " + str(total_due))
#                            ^^ String is needed here so that the variable can be concatenated.

print("food cost is " + str(food_cost) + " and tax is " + str(tax))
# print("Tip is " + str(tip))
print("Tip is " + format(tip, ".2f"))
print(f"Total due is {total_due}")

#Used f-string for total due print statement
