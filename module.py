import math

# Step 1: Ask user for input
num = float(input("Enter a number: "))

# Step 2: Calculations using math module
square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

# Step 3: Display results
print(f"Square root of {num} is:", square_root)
print(f"Natural logarithm of {num} is:", natural_log)
print(f"Sine of {num} radians is:", sine_value)