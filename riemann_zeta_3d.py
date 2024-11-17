import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpmath import zeta
import matplotlib.colors as colors

def compute_zeta_magnitude(re_s, im_s):
    """Compute the magnitude of the zeta function for a complex number s."""
    try:
        return float(abs(zeta(complex(re_s, im_s))))
    except:
        return np.nan

# Create a grid of points
re_points = np.linspace(-2, 4, 100)  # Real part range
im_points = np.linspace(-20, 20, 100)  # Imaginary part range
RE, IM = np.meshgrid(re_points, im_points)

# Initialize the magnitude array
Z = np.zeros_like(RE)

# Compute zeta function magnitude for each point
print("Computing zeta function values...")
for i in range(len(re_points)):
    for j in range(len(im_points)):
        Z[j, i] = compute_zeta_magnitude(RE[j, i], IM[j, i])

# Create the 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface with logarithmic scaling for better visualization
norm = colors.LogNorm(vmin=Z[~np.isnan(Z)].min(), vmax=Z[~np.isnan(Z)].max())
surf = ax.plot_surface(RE, IM, Z, 
                      cmap='viridis',
                      norm=norm,
                      linewidth=0,
                      antialiased=True)

# Customize the plot
ax.set_xlabel('Re(s)')
ax.set_ylabel('Im(s)')
ax.set_zlabel('|ζ(s)|')
ax.set_title('Magnitude of Riemann Zeta Function')

# Add a color bar
fig.colorbar(surf, ax=ax, label='|ζ(s)|')

# Adjust the view angle for better visualization
ax.view_init(elev=30, azim=45)

# Add text about the critical line
ax.text2D(0.02, 0.98, 'Critical Line: Re(s) = 1/2', 
          transform=ax.transAxes,
          color='red')

# Show grid
ax.grid(True)

plt.show()
