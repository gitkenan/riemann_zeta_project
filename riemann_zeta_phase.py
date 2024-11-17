import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta
import matplotlib.colors as colors

def compute_zeta_phase(re_s, im_s):
    """Compute the phase (argument) of the zeta function for a complex number s."""
    try:
        z = complex(zeta(complex(re_s, im_s)))
        return np.angle(z, deg=True)  # Returns angle in degrees
    except:
        return np.nan

def create_phase_plot(re_range=(-2, 4), im_range=(-20, 20), resolution=200):
    """Create a phase plot of the Riemann zeta function."""
    # Create a grid of points
    re_points = np.linspace(re_range[0], re_range[1], resolution)
    im_points = np.linspace(im_range[0], im_range[1], resolution)
    RE, IM = np.meshgrid(re_points, im_points)
    
    # Initialize the phase array
    phase = np.zeros_like(RE)
    
    # Compute zeta function phase for each point
    print("Computing zeta function phases...")
    for i in range(len(re_points)):
        for j in range(len(im_points)):
            phase[j, i] = compute_zeta_phase(RE[j, i], IM[j, i])
    
    return RE, IM, phase

def plot_phase(RE, IM, phase):
    """Create the phase plot with custom styling."""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create a custom cyclic colormap
    colors_list = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta', 'red']
    n_bins = 100
    cmap = colors.LinearSegmentedColormap.from_list('phase_colormap', colors_list, N=n_bins)
    
    # Plot the phase
    im = ax.imshow(phase, 
                  extent=[RE.min(), RE.max(), IM.min(), IM.max()],
                  cmap=cmap,
                  aspect='auto',
                  vmin=-180,
                  vmax=180)
    
    # Add colorbar
    cbar = plt.colorbar(im)
    cbar.set_label('Phase (degrees)')
    
    # Add the critical line
    critical_line = 0.5
    ax.axvline(x=critical_line, color='white', linestyle='--', alpha=0.5, 
               label='Critical Line (Re(s) = 1/2)')
    
    # Customize the plot
    ax.set_xlabel('Re(s)')
    ax.set_ylabel('Im(s)')
    ax.set_title('Phase Plot of Riemann Zeta Function')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    return fig, ax

def main():
    # Create the phase plot
    RE, IM, phase = create_phase_plot()
    
    # Plot the results
    fig, ax = plot_phase(RE, IM, phase)
    
    # Add text box with information
    info_text = (
        'Phase Plot of ζ(s)\n'
        '----------------\n'
        'Shows argument/phase of\n'
        'the zeta function in the\n'
        'complex plane.\n'
        'Color represents phase angle\n'
        'from -180° to +180°'
    )
    plt.text(0.02, 0.98, info_text,
             transform=ax.transAxes,
             verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
