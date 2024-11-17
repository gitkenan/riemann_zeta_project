import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpmath import zetazero, zeta

# Create the figure and axis for the plot
fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(bottom=0.25)  # Make room for the sliders

# Initial parameters
t_range_init = 30.0
re_s_init = 0.5
num_points = 400

# Generate initial plot
t_values = np.linspace(-t_range_init, t_range_init, num_points)
s_values = re_s_init + 1j * t_values
zeta_values = [complex(zeta(complex(s))) for s in s_values]
real_parts = [z.real for z in zeta_values]
imaginary_parts = [z.imag for z in zeta_values]

# Create the initial plot
line, = ax.plot(real_parts, imaginary_parts, label='Riemann Zeta Function', color='blue')
ax.set_title(f'Riemann Zeta Function (Re(s) = {re_s_init:.2f})')
ax.set_xlabel('Real Part')
ax.set_ylabel('Imaginary Part')
ax.axhline(0, color='black', lw=0.5, ls='--')
ax.axvline(0, color='black', lw=0.5, ls='--')
ax.grid(True)
ax.legend()

# Create sliders
ax_t_range = plt.axes([0.15, 0.1, 0.65, 0.03])
ax_re_s = plt.axes([0.15, 0.05, 0.65, 0.03])

s_t_range = Slider(ax_t_range, 't range', 5, 100, valinit=t_range_init)
s_re_s = Slider(ax_re_s, 'Re(s)', -2, 2, valinit=re_s_init)

def update(val):
    # Get current slider values
    t_range = s_t_range.val
    re_s = s_re_s.val
    
    # Update the plot
    t_values = np.linspace(-t_range, t_range, num_points)
    s_values = re_s + 1j * t_values
    zeta_values = [complex(zeta(complex(s))) for s in s_values]
    real_parts = [z.real for z in zeta_values]
    imaginary_parts = [z.imag for z in zeta_values]
    
    # Update line data
    line.set_data(real_parts, imaginary_parts)
    
    # Update title
    ax.set_title(f'Riemann Zeta Function (Re(s) = {re_s:.2f})')
    
    # Adjust plot limits if necessary
    ax.relim()
    ax.autoscale_view()
    
    # Redraw canvas
    fig.canvas.draw_idle()

# Register the update function with the slider
s_t_range.on_changed(update)
s_re_s.on_changed(update)

plt.show()
