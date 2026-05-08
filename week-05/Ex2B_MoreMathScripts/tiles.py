# This script determines the amount of tile boxes needed

# meta
import math

length = float(input("Enter the length of the room (in feet): "))
width = float(input("Enter the width of the room(in feet): "))

# Tiles
TilePack = 12
Xtra = 0.10

# Tiles & Area Calculationss
Area = (length * width)
TilesNeeded =  Area * (1 + Xtra)

# The Boxes...
Boxes = math.ceil(TilesNeeded / TilePack)

# Display Results


# Display results
print(f"\nRoom area: {Area:.2f} square feet")
print(f"Tiles needed (with 10% extra): {TilesNeeded:.2f}")
print(f"Total boxes to buy: {Boxes}")
