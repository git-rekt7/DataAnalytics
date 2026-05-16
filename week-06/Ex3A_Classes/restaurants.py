# Restaurants 

class Restaurant:
    ''' Represents a restaurant, its open status, and what kind of food it serves '''
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
    
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def rest_closed(self):
        print(f"{self.rest_name} is closed.") # created closed as a little bonus

# Three instances of restaurant

restaurant1 = Restaurant("Salmonella Subz", "sandwiches")

restaurant2 = Restaurant("B.S. Biscuits", "breakfast")

restaurant3 = Restaurant("E.Coli Eclairs", "dessert")

# Call statements

# Salmonella Subz, sanitation rating C-
print("\n   Salmonella Subz")
print("   ~~~~~~~~~~~~~~~")
restaurant1.describe_rest()
restaurant1.rest_open()

# B.S. Biscuits, they just aren't that great
print("\n   B.S. Biscuits")
print("   ~~~~~~~~~~~~~~~")
restaurant2.describe_rest()
restaurant2.rest_open()

# E.Coli Eclairs closed due to...outbreak
print("\n   E.Coli Eclairs")
print("   ~~~~~~~~~~~~~~~")
restaurant3.describe_rest()
restaurant3.rest_closed()
