import matplotlib.pyplot as plt
import numpy as np

# Python interpretation of MATLAB exercise given in 
# introduction to programming course

def mandelbrot(start, end, size=1000):
    """Draws the mandelbrot with matrix size*size, starting
    from start in bottom top left, ending at end in bottom right."""

    r = np.linspace(start.real, end.real, size)
    z = np.linspace(start.imag, end.imag, size)

    x, y = np.meshgrid(r, z) # create gradual arrays for real and img. numbers

    brot = []
    for i in range(size): # add their convergence index to Mandelbrot matrix
        brot.append([])
        for j in range(size):
            brot[i].append(converge(np.complex(x[i][j], y[i][j])))

    # Show the Mandelbrot matrix
    plt.title("Das Brot")
    plt.imshow(brot)
    plt.colorbar()
    plt.axis('off')
    plt.show()

def converge(c):
    """Calculates number of iterations, maximum 100, to determine convergence."""
    temp = c
    for i in range(0, 100):
        if (abs(temp) > 2):
            return i
        temp = temp**2 + c
    return 100

# Example values given in course:
# -0.7+0.7j, -0.5+0.6j
# -1.4+0.48j, -1.1+0.24j
# -1.8+0.03j, -1.5-0.03j
# -0.18-1.02j, -0.14–1.05j

# e.g.
mandelbrot(-0.7+0.7j, -0.5+0.6j)







 


