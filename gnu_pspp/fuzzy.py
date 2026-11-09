import numpy as np
import matplotlib.pyplot as plt

# Compact 1-line logic for Triangular MF
triangular = lambda x, a, b, c: max(min((x - a) / (b - a), (c - x) / (c - b)), 0)

a, b, c = 2, 5, 8
x_values = np.linspace(0, 10, 500)
y_values = [triangular(x, a, b, c) for x in x_values]

plt.plot(x_values, y_values, color="blue", linewidth=2, label="Triangular MF")
plt.title("Triangular Membership Function")
plt.grid(True)
plt.legend()
plt.show()