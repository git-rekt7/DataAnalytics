# Show Major

# Student Variables
student_name = input("What is your name? ")
student_major = input("What is your major code? ")

# Major and office location if statements
if student_major == "ENG":
    major_name = "English"
    office_location = "Kerr Hall, Room 201"
elif student_major == "CSCI":
    major_name = "Computer Science"
    office_location = "Sheppard Hall, Room 314"
elif student_major == "BIOL":
    major_name = "Biology"
    office_location = "Science Bldg, Room 310"
elif student_major == "HIST":
    major_name = "History"
    office_location = "Kerr Hall, Room 114"
elif student_major == "MKT":
    major_name = "Marketing"
    office_location = "Westly Hall, Room 310"
else:
    major_name = "Unknown"
    office_location = ""

# Output
print(f"Student Name: {student_name}")
print(f"Student Major: {major_name}")
print(f"The office is located at/in: {office_location}")