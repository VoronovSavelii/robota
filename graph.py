import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 20)

def f(x):
    return x**3

print(f(x))
y = f(x)

plt.plot(x, y)
plt.show()