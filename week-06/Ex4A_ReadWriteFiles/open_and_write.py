# Open and write
import os
print(os.getcwd()) # Returns the current working directory my file was saved too.

# f = open("about_me.txt", "w")
# f.write("Check 123...This thing on?")    Commented out to avoid rewrite
# f.close()

# New line
with open("about_me.txt", "a") as f:
    f.write("My perfect night includes a beautiful view and my closest friends. \n")

print("File is writing")

# First read 50

with open("about_me.txt", "r") as f:
    # print(f.read(50))# Reads the first 50 characters from about_me.txt
    # print(f.read(50))# Reads the second set of 50 characters
    
   # print(f.readline(10))
    # print(f.readline())

    # Loop statement 2 read more lines
    # for i in range(1, 5):
        # print(f.readline())

    # Read first 50 characters
    first_chunk = f.read(50)

    # Store lines from a loop using readline()
    lines_from_loop = []
    for i in range(1, 5):
        line = f.readline()
        lines_from_loop.append(line)

    # c) Read remaining lines (up to 100)
    remaining_lines = f.readlines(100)


# Print results
print("First chunk (50 chars):")
print(first_chunk)

print("\nLines from loop:")
print(lines_from_loop)

print("\nRemaining lines:")
print(remaining_lines)


print(f"First 50 characters: {first_chunk}")

print(f"Next four lines, list by line: {lines_from_loop}")

print(f"Next 100 characters, list by line then, rounded up to complete lines: {remaining_lines}")
