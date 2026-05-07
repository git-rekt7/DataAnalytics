# Fahrenheit to Celsius conversion script
# Formula, C = (F-32) ÷ 1.8

F_Temp = float(input("Enter a temperature in Fahrenheit: "))

C_Temp = (F_Temp - 32) * (5/9)
print(f"{F_Temp:.2f} Fahrenheit is equal to {C_Temp:.2f} Celsius")