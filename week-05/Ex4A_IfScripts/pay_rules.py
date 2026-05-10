# Pay Rules

# Here's where I define the variables
pay_rate = float(input("What is your pay rate? "))
hours_worked = float(input("How many hours did you work? "))

# This is the part where I calculate the gross pay

if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hrs = hours_worked - 40
    overtime_pay = overtime_hrs * pay_rate * 1.5
    gross = regular_pay + overtime_pay
else:
    gross = hours_worked * pay_rate

# Print statement
print(f"GROSS PAY = {gross}")