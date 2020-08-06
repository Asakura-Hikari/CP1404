try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("You cannot divide by zero, please enter another number: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
When will a ValueError occur?
when input are not a number
When will a ZeroDivisionError occur?
when denominator is 0

Could you change the code to avoid the possibility of a ZeroDivisionError?
If you could figure out the answer to question 3, then make this change now.
"""
