import matplotlib.pyplot as plt
import numpy as np

# Example for how to curve fit with polynomials.
# Note polyfit and polyval are exactly the same as in MATLAB. 

DEGREE = 7

# received data (originally from MATLAB course)
x_data = [ 0.000, 1.000, 2.000, 3.000, 4.000, 5.000 ]
y_data = [ 3.749, 4.689, 6.273, 5.897, 6.381, 7.003 ]

# fit polynomial 

coeff = np.polyfit(x_data, y_data, DEGREE)
x_range = np.linspace(0, 5, 100)
y_fitted = np.polyval(coeff, x_range) # evaluate polynomial between 0 and 5

# plot points and polynomial
plt.title('Polynomial curve fitting')
plt.xlim(-1, 6)
plt.ylim(0, 10)
plt.plot(x_range, y_fitted, color='blue', label='fitted curve')
plt.plot(x_data, y_data, 'ro', label='data')
plt.legend()
plt.show()