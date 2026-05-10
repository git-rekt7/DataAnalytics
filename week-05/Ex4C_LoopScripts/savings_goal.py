# Savings Goal

# Initial Value
account_bal = 100.0
savings_goal = 500.0
weekly_savings = 50.0
treat = 10.0

# Loops until savings goal is met
while account_bal < savings_goal:
    account_bal += weekly_savings

    # If you have saved atleast 75% of the goal, time4treats!!
    if account_bal >= savings_goal * 0.75:
        account_bal -= treat
        print(f"So close! after treating myself, my balance is up to {account_bal:.2f}")

    # If you have saved more than half of the goal
    elif account_bal > savings_goal * 0.5:
        print(f"Almost there! This week my balance is up to {account_bal:.2f}")

    # If you haven't saved either...
    else:
        print(f"This week my balance increased to {account_bal:.2f}")

# When you hit your goal...
print(f"Goal met! My current balance is {account_bal:.2f}")



