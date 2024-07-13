# In Python there are three numeric Types:
# int, float and complex
# EG

# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
integer = 1
print(type(integer))


# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
# Floats can also be scientific numbers with an "e" to indicate the power of 10.
floating_Point_Number = 1.5
print(type(floating_Point_Number))


# Complex numbers are written with a "j" as the imaginary part
complex_Number = 1j
print(type(complex_Number))


# Python Does not have a Random method biult in but it does have a random module
import random # Should be done at the top, but it doesn't matter

print(random.randrange(1, 10))