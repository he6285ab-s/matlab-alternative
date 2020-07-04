import cmath, math

# complex numbers typically written as 
x = 1 + 1j

print(cmath.phase(x)) # prints pi/4 (atan(1))
print(abs(x)) # prints sqrt(2)

print("Square root of -4:", cmath.sqrt(-4))