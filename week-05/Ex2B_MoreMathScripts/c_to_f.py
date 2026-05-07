# Celsius to Fahrenheit conversion script
# Formula, F = (C*9/5) + 32

C_Temp = float(input("Enter a temperature in Celsius: "))

F_Temp = (C_Temp * 9/5) + 32
print(f"{C_Temp:.2f} Celsius is equal to {F_Temp:.2f} Fahrenheit")