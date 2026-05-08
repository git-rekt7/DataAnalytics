# There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost
# $250 per day to rent (including the driver’s pay). How many vans do you need? How
# much will it cost to rent vans? What is the cost if you split it per person?

# Meta
import math

# VANS (Off the Road!)
Seats = 15
CostPerVan = 250

# Python for the stupid tourists
StupidTourists = int(input("How many will be going on the tour? "))

# How many vans will be needed?
VansNeeded = math.ceil(StupidTourists / Seats)

# Total cost
TotalCost = VansNeeded * CostPerVan

# Cost per person
CostPerPerson = TotalCost / StupidTourists

# Output
print("\nStupid Tour Rental Breakdown")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Number of stupid tourists: {StupidTourists}")
print(f"Vans required to shuttle the idiots: {VansNeeded}")
print(f"Total Rental Cost: ${TotalCost}")
print(f"Cost per idiot: ${CostPerPerson:.2f}")
