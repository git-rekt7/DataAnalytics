# Complex Taxes (ughhh)

#               Borrowed from Pay Rules
# Here's where I define the variables
pay_rate = float(input("What is your pay rate? "))
hours_worked = float(input("How many hours did you work? "))

# This is the part where I calculate the gross pay

if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hrs = hours_worked - 40
    overtime_pay = overtime_hrs * pay_rate * 1.5
    weekly_gross = regular_pay + overtime_pay
else:
    weekly_gross = hours_worked * pay_rate

# Weekly to Annual revenue
annual_gross = weekly_gross * 52 # 52 weeks in year

# Filing status
filing_status = 'single'

# Tax Calculation
if filing_status == "single":
    if annual_gross <= 50000:
        tax_rate = 0.20
    else:
        tax_rate = 0.25
elif filing_status == "joint":
    if annual_gross <= 80000:
        tax_rate = 0.18
    else:
        tax_rate = 0.22
else:
    tax_rate = 0
    print("Invalid filing status")

fed_tax = annual_gross * tax_rate

# Output
print("\n OUTPUT")
print("\n~~~~~~~~")
print(f"You worked {hours_worked} this period.")
print(f"Gross weekly pay is ${weekly_gross:,.2f}")
print(f"Annual gross income is ${annual_gross:,.2f}")
print(f"Filing Status: {filing_status}")
print(f"You owe: ${fed_tax:,.2f} in federal taxes.")