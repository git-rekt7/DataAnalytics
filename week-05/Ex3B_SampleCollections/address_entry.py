# Address Entry

# name = "Cotswald Arthurr"
address = "3600 Psycho Path"
city = "Hell"
state = "Michigan"
zip = "48169"

# Full name dictionary
full_name = {
    "first name": "Cotswald",
    "last name": "Arthurr"
}

# Printing address using multi-line f-string.
# print(f"Hello! my name is {name} and I live at {address} in {city}, {state}. The zipcode is {zip}")# Full name dictionary

# Printing address using dictionary
print(
    f"Hello! my name is {full_name['first name']} {full_name['last name']} "
    f"and I live at {address} in {city}, {state}. "
    f"The zipcode is {zip}"
)


# Updated Dictionary

full_name.update({"Honorific": "King" })

# Updated Print Statement
print(
    f"(UPDATED)Hello! my name is {full_name['Honorific']} {full_name['first name']} {full_name['last name']} "
    f"and I live at {address} in {city}, {state}. "
    f"The zipcode is {zip}"
)