import matplotlib.pyplot as plt
import numpy as np
from math import e

# Implementa f(x)= 0
eq = lambda x: e **  (x - x ** 2) - np.arctan(x ** 2)

x = np.linspace(-2, 2, 1000)
y = eq(x)
plt.plot(x, y, label=r'$f(x) = e^{x - x^{2}} - \arctan(x^2)$')

plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid()
plt.show()
