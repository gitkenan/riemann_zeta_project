# Riemann Zeta Function Visualization

An interactive visualization tool for exploring the Riemann zeta function through multiple graphical representations.

## Contents
1. [2D Interactive Plot](#2d-interactive-plot-riemann_zetapy)
2. [3D Surface Plot](#3d-surface-plot-riemann_zeta_3dpy)
3. [Phase Plot](#phase-plot-riemann_zeta_phasepy)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Mathematical Background](#mathematical-background)
8. [The Riemann-Siegel Formula](#the-riemann-siegel-formula-riemann_siegelpy)
9. [License](#license)

## Overview

This project provides multiple interactive visualizations of the Riemann zeta function, allowing users to explore its behavior through different representations. The visualizations help in understanding the complex nature of the zeta function, its zeros, and its phase behavior.

## Features

### 2D Interactive Visualization
- Real-time parameter adjustment using sliders:
  - Adjust the range of imaginary values (t)
  - Modify the real part of s
- Automatic plot rescaling
- Grid lines and axis markers
- Initial focus on the critical line (Re(s) = 1/2)

### 3D Surface Plot
- 3D visualization of the zeta function magnitude |ζ(s)|
- Logarithmic scaling for better visualization of variations
- Interactive features:
  - Rotate and zoom the surface
  - Color-coded magnitude representation
  - Grid lines for better orientation
- Highlights the critical line at Re(s) = 1/2
- Range visualization:
  - Real part: [-2, 4]
  - Imaginary part: [-20, 20]

### Phase Plot (riemann_zeta_phase.py)

The phase plot visualizes the argument (phase) of the Riemann zeta function ζ(s) in the complex plane. The phase of a complex number represents its angle in the complex plane, measured counterclockwise from the positive real axis.

### Mathematical Interpretation
- The phase angle ranges from -180° to +180° (or -π to +π radians)
- A phase of 0° means ζ(s) is purely real and positive
- A phase of 180° or -180° means ζ(s) is purely real and negative
- A phase of 90° means ζ(s) is purely imaginary and positive
- A phase of -90° means ζ(s) is purely imaginary and negative
- Other angles represent complex values with both real and imaginary parts

### Features
- Cyclic color mapping from -180° to +180°:
  * Red: ±180° (negative real axis)
  * Yellow/Green: ~90° (positive imaginary axis)
  * Cyan/Blue: ~-90° (negative imaginary axis)
  * Color transitions show continuous phase changes
- Critical line indicator at Re(s) = 1/2
- Interactive matplotlib interface
- Progress bar during computation
- Efficient 50x50 resolution grid
- Color-coded phase transitions

### Usage
```bash
python riemann_zeta_phase.py
```

### Interpretation Guide
- Colors represent the phase angle of ζ(s)
- Phase transitions (sharp color changes) indicate:
  * Zeros of the function (phase rotates rapidly around these points)
  * Poles (similar rapid phase rotation)
  * Branch cuts (discontinuous phase changes)
- White dashed line indicates the critical line Re(s) = 1/2
  * The Riemann Hypothesis suggests all non-trivial zeros lie on this line
- Smooth color gradients indicate regions where the function varies continuously
- Complete color cycles (red→yellow→green→blue→red) indicate the function wrapping around the origin

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- mpmath
- mpl_toolkits.mplot3d

## Installation

1. Clone this repository:
```bash
git clone https://github.com/gitkenan/riemann_zeta_project.git
cd riemann_zeta_project
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

### 2D Visualization
Run the interactive 2D visualization:
```bash
python riemann_zeta.py
```

Use the sliders at the bottom of the plot to:
- Adjust the range of t values (imaginary part)
- Change the real part of s

### 3D Visualization
Run the 3D surface plot:
```bash
python riemann_zeta_3d.py
```

Interact with the 3D plot using:
- Left mouse button: Rotate the view
- Right mouse button: Zoom in/out
- Middle mouse button: Pan the view

### Phase Visualization
Run the phase plot visualization:
```bash
python riemann_zeta_phase.py
```

The phase plot shows:
- Color-coded phase angles from -180° to +180°
- Critical line at Re(s) = 1/2
- Phase transitions and winding behavior
- Zeros visible as phase singularities

## Mathematical Background

The Riemann zeta function ζ(s) is a fundamental function in number theory. The visualization focuses on:
- The complex values of this function
- The critical line where Re(s) = 1/2
- The magnitude of the function |ζ(s)| in the complex plane
- The phase/argument of the function, revealing its winding behavior
- The zeros of the function, which appear as:
  * Valleys in the 3D plot
  * Phase singularities in the phase plot

The Riemann Hypothesis, one of the most important unsolved problems in mathematics, states that all non-trivial zeros of the zeta function lie on the critical line Re(s) = 1/2.

## The Riemann-Siegel Formula (riemann_siegel.py)

The Riemann-Siegel formula provides an efficient method for computing the Riemann zeta function ζ(s) for large values of the imaginary part t. This implementation is particularly useful for investigating zeros high on the critical line.

### Implementation Features

- **Riemann-Siegel Formula**: Efficient computation of ζ(s) using the Riemann-Siegel formula
- **Theta Function**: Accurate approximation of the Riemann-Siegel theta function
- **Z-Function**: Implementation of the Z-function for critical line calculations
- **Error Estimation**: Built-in error estimation for numerical approximations

### Numerical Properties

Our implementation has been thoroughly tested and exhibits the following properties:

1. **Functional Equation**: Accurately preserves the functional equation ζ(s) = χ(s)ζ(1-s)
2. **Reflection Symmetry**: Maintains the reflection property ζ(s̄) = ζ(s)̄
3. **Known Zeros**: Successfully identifies known non-trivial zeros
4. **Critical Line Values**: Computes reasonable approximations along the critical line

### Usage Notes

The implementation provides good accuracy for:
- Moderate values of t (imaginary part) up to ~50
- Critical line calculations near known zeros
- General exploration of zeta function properties

For high-precision calculations, especially at larger heights on the critical line (t > 50), it is recommended to use mpmath's implementation. Our implementation balances speed and accuracy while maintaining the essential mathematical properties of the zeta function.

### Test Suite

The test suite (test_riemann_siegel.py) verifies:
- Functional equation preservation
- Reflection symmetry
- Known zero detection
- Critical line behavior
- Theta function properties
- Z-function characteristics

All tests include appropriate numerical tolerances to account for the inherent approximations in the computational methods.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
