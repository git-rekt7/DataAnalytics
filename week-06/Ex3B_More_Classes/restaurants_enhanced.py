
# Restaurants 

class Restaurant:
    ''' Represents a restaurant, its open status, and what kind of food it serves '''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def add_number_served(self, number):
        self.number_served += number

    def customer_rating(self, rating):
        # Rating between 1 and 5
        if 1 <= rating <= 5:
            self.customer_ratings.append(rating)

            # Average
            average = sum(self.customer_ratings) / len(self.customer_ratings)

            print(f"Your rating was {rating}. The average rating for {self.rest_name} is {average:.2f}")
        else:
            print("Please enter a rating between 1 and 5.")

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def rest_closed(self):
        print(f"{self.rest_name} is closed.")


# Three instances of restaurant

restaurant1 = Restaurant("Salmonella Subz", "sandwiches")
restaurant2 = Restaurant("B.S. Biscuits", "breakfast")
restaurant3 = Restaurant("E.Coli Eclairs", "dessert")


# Call statements

print("\n   Salmonella Subz")
print("   ~~~~~~~~~~~~~~~")
restaurant1.describe_rest()
restaurant1.rest_open()
restaurant1.add_number_served(7)
print(f" Salmonella Subz served {restaurant1.number_served} customers today.")

print("\n   B.S. Biscuits")
print("   ~~~~~~~~~~~~~~~")
restaurant2.describe_rest()
restaurant2.rest_open()
restaurant2.add_number_served(4)
print(f" B.S. Biscuits served {restaurant2.number_served} customers today.")

print("\n   E.Coli Eclairs")
print("   ~~~~~~~~~~~~~~~")
restaurant3.describe_rest()
restaurant3.rest_closed()
restaurant3.add_number_served(0)
print(f" E.Coli Eclairs served {restaurant3.number_served} customers today.")

# Ratings
rating = int(input("How would you rate your experience? (1-5): "))
restaurant1.customer_rating(rating)


