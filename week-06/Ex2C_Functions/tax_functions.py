# Tax Functions

# Social Security
def get_soc_sec_tax(gross_pay):
    tax_rate = 0.062
    return gross_pay
# Medicare Tax
def get_medicare_tax(gross_pay):
    tax_rate = 0.0145
    return gross_pay

def get_federal_tax(gross_pay, withholding_code):
    if withholding_code == 0:
        tax_rate = 0.23
    elif withholding_code == 1:
        tax_rate = 0.21
    elif withholding_code == 2:
        tax_rate = 0.195
    elif withholding_code == 3:
        tax_rate = 0.185
    else: # 4 or more
        tax_rate = 0.18

    return gross_pay * tax_rate

#               Person One
print("\n PERSON ONE")
print("\n ~~~~~~~~~~~")
print(get_federal_tax(750, 0))

#               Person Two
print("\n PERSON TWO")
print("\n ~~~~~~~~~~~")
print(get_federal_tax(1550, 2))

#               Person Three
print("\n PERSON THREE")
print("\n ~~~~~~~~~~~")
print(get_federal_tax(1100, 5))

    
