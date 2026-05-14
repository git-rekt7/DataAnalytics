# quick_multiplier

# Doubler Variable
doubler = lambda n: n * 2

print("\n DOUBLER")
print("\n ~~~~~~~~")
print(f"This is the doubler used on number 8: {doubler(8)}")
print(f"This is the doubler used on number -4: {doubler(-4)}")
print(f"This is the doubler used on phrase banana: {doubler('banana')}")

# Tripler Variable
tripler = lambda n: n * 3

print("\n TRIPLER")
print("\n ~~~~~~~~")
print(f"This is the tripler used on number 8: {tripler(8)}")
print(f"This is the tripler used on number -4: {tripler(-4)}")
print(f"This is the tripler used on phrase banana: {tripler('banana')}")

# Multiplier function to use with different numbers
def multiplier(factor):
    return lambda n: n * factor

# Various Multipliers
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

# Multiplier Print Statements
print("\n VARIOUS MULTIPLIERS USED ON NUMBER EIGHT")
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"This is the quadrupler used on number 8: {quadrupler(8)}")
print(f"This is the quintupler used on number 8: {quintupler(8)}")
print(f"This is the sextupler used on number 8: {sextupler(8)}")
print(f"This is the octupler used on number 8: {octupler(8)}")
print(f"This is the nonupler used on number 8: {nonupler(8)}")
print(f"This is the decupler used on number 8: {decupler(8)}")





