# Interactive Riemann Zeta Function Visualization

This project provides an interactive visualization of the Riemann zeta function in the complex plane. Users can explore different regions of the function by adjusting parameters in real-time using interactive sliders.

## Features

- Interactive visualization of the Riemann zeta function
- Real-time parameter adjustment using sliders:
  - Adjust the range of imaginary values (t)
  - Modify the real part of s
- Automatic plot rescaling
- Grid lines and axis markers for better orientation
- Initial focus on the critical line (Re(s) = 1/2)

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- mpmath

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/riemann_zeta_project.git
cd riemann_zeta_project
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python riemann_zeta.py
```

Use the sliders at the bottom of the plot to:
- Adjust the range of t values (imaginary part)
- Change the real part of s

The plot will update automatically as you move the sliders.

## Mathematical Background

The Riemann zeta function ζ(s) is a fundamental function in number theory. The visualization focuses on the complex values of this function, with particular interest in the critical line where Re(s) = 1/2, which is related to the famous Riemann Hypothesis.

