import matplotlib.pyplot as plt
import numpy as np
import math

# vector of 100 x values between - pi and pi
x_values = np.linspace(-math.pi,math.pi,100)

# add text
plt.title('Sine wave')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# change ticks, window limits etc.
plt.xticks([-math.pi, 0, math.pi], ['- ' + '\u03C0', '0', '\u03C0'])
plt.xlim(-3.5, 3.5)
plt.ylim(-1.25, 1.25)

# plot graph and show label
plt.plot(x_values, np.sin(x_values), color='red', label='Sine')
plt.legend()


plt.show()
