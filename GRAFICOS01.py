import matplotlib.pyplot as plt
import numpy as np
from math import e

# Implementa f(x)= 0
y_ana = lambda x: (e ** x) - x - 3

x = np.linspace(-4, 4, 400)
y = y_ana(x)
plt.plot(x, y, label=r'$f(x) = e^{x} - x - 3$')

plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid()
plt.show()




# Implementa f(x)= 0
y_ana = lambda x: np.cos(8 * x) - x

x = np.linspace(-1, 1, 400)
y = y_ana(x)
plt.plot(x, y, label=r'$f(x) = \cos(8x) - x$')

plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid()
plt.show()





# Implementa f(x)= 0
y_ana = lambda x: np.tan(x) - (1 / x)

x = np.linspace(-1.5, 1.5, 100)
y = y_ana(x)
plt.plot(x, y, label=r'$f(x) = \tan(x) - \dfrac{1}{x}$')

plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid()
plt.show()
