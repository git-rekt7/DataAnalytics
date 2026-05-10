# Greeting

# Present hour (Military Time)
present_hour = float(input("what time is it? "))


# Print Statement
if present_hour < 23 or present_hour < 4:
    print("What are you doing up so late??")
elif present_hour < 10:
    print("Good Morning!")
elif present_hour < 17:
    print("Good day!")
else:
    print("Good evening!")