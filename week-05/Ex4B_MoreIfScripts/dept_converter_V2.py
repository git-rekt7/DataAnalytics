# Department Converter Version Dos


def department_name(dept_code):
    match dept_code:
        case 1:
            return "Marketing"
        case 5:
            return "Human Resources"
        case 10:
            return "Accounting"
        case 12:
            return "Legal"
        case 18:
            return "IT"
        case 20:
            return "Customer Relations"
        case _:
            return "Unknown"

    
# Simple test list



test = [1, 5, 10, 12, 18, 20, 27]

for code in test:
    print(f"Department code {code}: {department_name(code)}")
