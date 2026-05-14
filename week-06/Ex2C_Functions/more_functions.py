# Moar Functions

# defining mailing label
def display_mailing_label(name,address,city,state,zip):
    return f"{name}\n{address}\n{city}, {state} {zip}"

print(display_mailing_label(
    "George Jenkins",
    "55 Nunya Road",
    "Utopia",
    "Mars",
    "89809"
))

# defining add numbers function
def add_numbers(*numbers):
    total = sum(numbers)
    
    # String formatting
    expression = " + ".join(str(num) for num in numbers)
    
    print(f"{expression} = {total}")  

add_numbers(5, 10, 70)
add_numbers(8, 9, 10)
add_numbers(9, 2, 5)

# Defines display receipt function
def display_receipt(total_due, amount_paid):
    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"Total Due: ${total_due:.2f}")
        print(f"Amount Paid: ${amount_paid:.2f}")
        print(f"Change Due: ${change:.2f}")
    else:
        remaining = total_due - amount_paid
        print(f"Total Due: ${total_due:.2f}")
        print(f"Amount Paid: ${amount_paid:.2f}")
        print(f"Remaining Balance: ${remaining:.2f}")

# Receipt display
display_receipt(60.76, 70.00)
print()
display_receipt(60.76, 60.76)
print()
display_receipt(60.76, 4.00)

