import matplotlib
#matplotlib.use('Qt5Agg')
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Datos de ejemplo (mediciones de laboratorio)
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])

# Regresión lineal
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print(f"Pendiente: {slope:.4f} ± {std_err:.4f}")
print(f"Intercepto: {intercept:.4f}")
print(f"R²: {r_value**2:.4f}")

# Gráfica
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red', label='Datos experimentales')
plt.plot(x, slope * x + intercept, color='blue', label=f'Ajuste: y = {slope:.2f}x + {intercept:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión Lineal')
plt.legend()
plt.grid(True)
plt.savefig('grafica.png', dpi=150)
plt.show()
