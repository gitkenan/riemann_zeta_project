# Interactive Riemann Zeta Function Visualization

A comprehensive visualization tool for exploring the Riemann zeta function through multiple representations: 2D interactive plots, 3D surface plots, and phase diagrams.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
  - [2D Interactive Visualization](#2d-interactive-visualization)
  - [3D Surface Plot](#3d-surface-plot)
  - [Phase Plot (Argand Diagram)](#phase-plot-argand-diagram)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [2D Visualization](#2d-visualization)
  - [3D Visualization](#3d-visualization)
  - [Phase Visualization](#phase-visualization)
- [Mathematical Background](#mathematical-background)
- [License](#license)

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

### Phase Plot (Argand Diagram)
- Visualization of the argument/phase of ζ(s)
- Cyclic color mapping from -180° to +180°
- Features:
  - Custom color scheme for clear phase transitions
  - Critical line indicator
  - High-resolution phase mapping
  - Informative color bar
- Range coverage:
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
  - Valleys in the 3D plot
  - Phase singularities in the phase plot

The Riemann Hypothesis, one of the most important unsolved problems in mathematics, states that all non-trivial zeros of the zeta function lie on the critical line Re(s) = 1/2.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
