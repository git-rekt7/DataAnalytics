# Ranked List

# List of 80's punk rock bands

good_bands = [
    "Adrenalin OD",
    "Germs",
    "Dr.Know",
    "Gauze",
    "Concrete Sox"
]

# List printed in reverse order

for index, band in enumerate(reversed(good_bands), start=1):
    if index == 1:
        print(f"{index}. {band} <- top pick!")
    else:
        print(f"{index}. {band}")
