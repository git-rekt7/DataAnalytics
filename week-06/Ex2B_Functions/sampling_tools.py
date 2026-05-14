# Sampling Tools
# Meta
import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector'
]

print(random.choice(products)) # Returns a random product including duplicates
print(random.sample(products, 3)) # Returns 3 random products
random.shuffle(products) # shuffles the list
print(products) # Prints shuffled list ^

transaction_number = random.randint(50, 300)
print(f"Today we had {transaction_number} transactions!")