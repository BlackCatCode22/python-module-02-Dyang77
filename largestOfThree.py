# Get three integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Nested if statements to find the largest number
if num1 > num2:
        if num1 > num3:
            largest = num1
        else:
            largest = num3
else:
        if num2 > num3:
            largest = num2
        else:
            largest = num3

# Output the largest number
print(f"The largest number is: {largest}")
