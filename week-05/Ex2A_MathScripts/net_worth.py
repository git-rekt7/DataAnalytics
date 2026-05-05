# 1.
# a) For this example, Mr Jensen owns a beautiful lake home, a puppy mill, and a 2026 Hyuandai Sonata (fancy)
# These would be considered his assets, although the Sonata is actively depreciating.
# Mr Jensen's debt consists of a student loans to an almost ivy league university and an average amount of credit card debt.


# Assets
LakeHome = 1000000
PuppyMill = 500000
Sonata = 39495

# Debt
StudentLoan = 38000
CreditDebt = 6540


# MATHEMATICS

Assets = (LakeHome + PuppyMill + Sonata)
print(f"Your total assets equal: {Assets:,}")

Debts = (StudentLoan + CreditDebt)
print(f"Your total debts equal: {Debts:,}")

NetWorth = (Assets - Debts)
print(f"Your Net Worth is: {NetWorth:,}")
