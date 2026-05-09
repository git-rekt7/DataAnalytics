# Candy Store

candy = ("Hi-Chew", "Starburst", "Peelerz")
flavors = ("Bleak Berry", "Melancholy Melon", "Lackluster Lemon", "Apple Abomination")

# set of candy & flavor combinations
candy_combos = set()

# Tuple becomes Index
# index_candy = candy[i]
# index_flavor = flavors[i]

for i in range(min(len(candy), len(flavors))):
    index_candy = candy[i]
    index_flavor = flavors[i]
candy_combos.add(f"{index_candy} + {index_flavor}")

print(f"Today's candy options: {candy_combos}")

# Output remains the same "Peelerz + Lackluster Lemon"


