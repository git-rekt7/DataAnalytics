# calculating interest using the rule of seventy two

CurrentSavings = 55000
Interest = .10
Years = 4

NewSavings = CurrentSavings * (1 + Interest) ** Years
print(f"your current savings is {CurrentSavings}. At a {Interest:.0%} interest rate, your savings account will be worth ${NewSavings:.2f} in {Years} years")