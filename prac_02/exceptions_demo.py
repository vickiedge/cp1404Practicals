"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? decimal or fraction entered..anything other than integer
2. When will a ZeroDivisionError occur? denominator entered is zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    #fraction = numerator / denominator
    if denominator != 0:
        fraction = numerator / denominator
    elif denominator == 0:
        fraction = 0.0
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
#except ZeroDivisionError:
    #print("Cannot divide by zero!")
print("Finished.")