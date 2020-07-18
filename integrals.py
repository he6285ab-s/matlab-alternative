import scipy.integrate as integrate
from math import exp

# Basic example with definite integral

# Arguments to the integrate.quad function are:
# function to integrate, lower bound, upper bound
# example with integral of x^2 from 0 to 3, should give 9
result_1 = integrate.quad(lambda x: x**2, 0, 3)
print(f'{result_1[0]:1.2f}') # prints 9


# Could also define function and use as parameter
def func(x):
    return exp(0.5*x)

# should give 2 * (exp(1) - exp(0)), approx. 3.4366
result_2 = integrate.quad(func, 0, 2)
print(result_2[0]) # prints the correct answer