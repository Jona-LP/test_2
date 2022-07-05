# Modulos necesarios.
import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np
from math import e

# Implementa dy/dx = f(x,y).
f = lambda x, y: ((e ** x) * np.sin(x)) - (5 * y) 

# Implementa solucion analitica
y_ana = lambda x: ((186 / 37) * (e ** (-5 * x))) + (6 * ((e ** x) / 37) * np.sin(x)) - (((e ** x) / 37) * np.cos(x))

# Computa error entre sol. analitica y sol. numerica
error = lambda x, y: np.abs(x - y)

# Listas vacias para alojar puntos utilizados al graficar.
x_points = []
y_points = []

# Implementa Metodo de Euler.
def euler(x, y, h, N):
    for i in range(N):
        y = y + (h * f(x, y))
        x = x + h
        y_points.append(y)
        x_points.append(x)
    print(f"x = {round(x, 8)}, y(x) = {y}")
    print(f"Error Absoluto en t=Nh: {error(y_ana(x), y)}.")

"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!! PANEL DE CONTROL !!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Ejecute la funcion euler() indicando los parametros

PARAMETROS
x = Valor inicial de x
y = Valor inicial de y
h = Variacion de x
N = Numero maximo de iteraciones
"""
euler(x = 0, y = 5, h = 0.01, N = 314)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!! GRAFICOS !!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

x = np.linspace(0, 4, 314)
y = y_ana(x)
plt.plot(x, y, "r" ,label="Solución Analítica")

plt.plot(x_points, y_points, "b", label="Método de Euler")

plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid()
plt.show()
