# Exception Basics

# Value Error
try:
    x = int("not_a_number")  # Returns ValueError
except ValueError as e:
    print("Stupid ValueError:", e)
else:
    print("Conversion successful:", x)
finally:
    print("Type a number next time")

# Name Error
try:
    print(undefined_variable)  # Returns NameError
except NameError as e:
    print("Stupid NameError:", e)
else:
    print("exists")
finally:
    print("Define your variables nerd")

# Type Error

try:
    result = "5" + 10  # Returns TypeError
except TypeError as e:
    print("Stupid TypeError:", e)
else:
    print("Result:", result)
finally:
    print("Let's use the right type next time")

# Syntax Error
try:
    exec("if True print('Missing colon')")  # Returns SyntaxError
except SyntaxError as e:
    print("Stupid SyntaxError:", e)
else:
    print("success!")
finally:
    print("Pay closer attention to your syntax")



