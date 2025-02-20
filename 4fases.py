import numpy as np
import matplotlib.pyplot as plt

# Parámetros
E1 = 1
E2 = 2
x = y = np.linspace(-2 * np.pi, 2 * np.pi, 512)
X, Y = np.meshgrid(x, y)

a = E1**2 + E2**2
b = 2 * E1 * E2

N = 3
phi = 2 * np.pi * X / N

# Fases
alpha1 = 0
alpha2 = np.pi / 2
alpha3 = np.pi
alpha4 = 3 * np.pi / 2

# Intensidades
I1 = a + b * np.cos(phi + alpha1)
I2 = a + b * np.cos(phi + alpha2)
I3 = a + b * np.cos(phi + alpha3)
I4 = a + b * np.cos(phi + alpha4)

# Gráfica de Phi en 3D
plt.figure(1)
ax1 = plt.subplot(111, projection='3d')
surf1 = ax1.plot_surface(X, Y, phi, cmap='viridis', linewidth=0, antialiased=False)
plt.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)
ax1.set_title('Phi (3D)')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Phi')
plt.show()

# Cálculo de phi_w (phi envuelto)
rsin = I4 - I2
rcos = I1 - I3
phi_w = np.arctan2(rsin, rcos)

# Gráfica de Phi envuelto en 3D
plt.figure(2)
ax2 = plt.subplot(111, projection='3d')
surf2 = ax2.plot_surface(X, Y, phi_w, cmap='viridis', linewidth=0, antialiased=False)
plt.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)
ax2.set_title('Phi envuelto (3D)')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Phi envuelto')
plt.show()

# Desenvolvimiento de phi
phi_uy = np.unwrap(phi_w, axis=0)
phi_u = np.unwrap(phi_uy, axis=1)

# Gráfica de phi_u (2D)
plt.figure(3)
plt.contourf(X, Y, phi_u, levels=50, cmap='viridis')
plt.colorbar()
plt.title('Phi desarrollado (2D)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Gráficas de las intensidades
plt.figure(4)

plt.subplot(2, 2, 1)
plt.imshow(I1, extent=(-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi), cmap='gray')
plt.title('I₁ (α=0)')
plt.axis('square')

plt.subplot(2, 2, 2)
plt.imshow(I2, extent=(-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi), cmap='gray')
plt.title('I₂ (α=π/2)')
plt.axis('square')

plt.subplot(2, 2, 3)
plt.imshow(I3, extent=(-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi), cmap='gray')
plt.title('I₃ (α=π)')
plt.axis('square')

plt.subplot(2, 2, 4)
plt.imshow(I4, extent=(-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi), cmap='gray')
plt.title('I₄ (α=3π/2)')
plt.axis('square')

plt.tight_layout()
plt.show()