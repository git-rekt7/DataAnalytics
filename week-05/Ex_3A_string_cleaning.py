# STRING CLEANING

# Variables
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,000"
salary_2 = "$74,000"

# Lowercase Names
print("\nLowercase")
print("\n~~~~~~~~~~~")
print(f"First name in lowercase: {name_1.lower()}")
print(f"Second name in lowercase: {name_2.lower()}")
print(f"Third name in lowercase: {name_3.lower()}")

# Titlecase Names
print("\nTitlecase")
print("\n~~~~~~~~~~~")
print(f"First name in titlecase: {name_1.title()}")
print(f"Second name in titlecase: {name_2.title()}")
print(f"Third name in titlecase: {name_3.title()}")


# Replace
print("\nReplace")
print("\n~~~~~~~~~~~")
Replaced_sal1 = salary_1.replace("$", " ")
Replaced_sal2 = salary_2.replace("$"," ")
print(f"You are now witnessing the replaced salaries without $ :{Replaced_sal1}, {Replaced_sal2}")

# Replace to Interger

Replaced_Int = int(salary_1.replace("$", "").replace(",", ""))
print(f"Salary without comma: {Replaced_Int}")
print(f"Type confirmation of replaced integer: {type(Replaced_Int)}")



