# Interactive Riemann Zeta Function Visualization

A comprehensive visualization tool for exploring the Riemann zeta function in both 2D and 3D representations.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
  - [2D Interactive Visualization](#2d-interactive-visualization)
  - [3D Surface Plot](#3d-surface-plot)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [2D Visualization](#2d-visualization)
  - [3D Visualization](#3d-visualization)
- [Mathematical Background](#mathematical-background)
- [License](#license)

## Overview

This project provides interactive visualizations of the Riemann zeta function, allowing users to explore its behavior in both 2D and 3D representations. The visualizations help in understanding the complex nature of the zeta function and its zeros.

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

## Mathematical Background

The Riemann zeta function ζ(s) is a fundamental function in number theory. The visualization focuses on:
- The complex values of this function
- The critical line where Re(s) = 1/2
- The magnitude of the function |ζ(s)| in the complex plane
- The zeros of the function, which appear as valleys in the 3D plot

The Riemann Hypothesis, one of the most important unsolved problems in mathematics, states that all non-trivial zeros of the zeta function lie on the critical line Re(s) = 1/2.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
