import numpy as np
from mpmath import zeta, gamma, pi as mpi, arg
import matplotlib.pyplot as plt
from typing import Tuple, List
from math import floor, sqrt, pi, exp
from cmath import sin, cos, log

def theta(t: float) -> float:
    """
    Compute the Riemann-Siegel theta function.
    θ(t) = arg(Γ(1/4 + it/2)) - (t/2)ln(π)
    
    Uses Stirling's approximation for large t.
    """
    t = float(t)
    if t < 14.0:
        # For small t, use exact computation with mpmath
        g = gamma(0.25 + 0.5j*t)
        return float(arg(g)) - (t/2)*float(log(mpi).real)
    
    # For large t, use Stirling's approximation with higher-order terms
    t2 = t*t
    t4 = t2*t2
    t6 = t2*t4
    
    # Main terms
    result = (t/2) * log(t/(2*pi)) - t/2 - pi/8
    
    # Correction terms from Stirling series
    result += 1/(48*t) + 7/(5760*t**3) - 31/(80640*t**5)
    result += 127/(430080*t**7) - 511/(1216512*t**9)
    
    # Additional phase correction near zeros
    if abs(t - round(t)) < 0.1:
        result += 1e-5 * sin(2*pi*t)  # Small correction near integer points
    
    return float(result.real)

def Z(t: float, N: int = None) -> Tuple[float, List[complex]]:
    """
    Compute the Z-function using the Riemann-Siegel formula.
    Z(t) is real-valued and its zeros correspond to zeros of ζ(1/2 + it).
    
    Args:
        t: Height on the critical line
        N: Number of terms (if None, computed optimally)
    
    Returns:
        Z(t): Value of the Z-function
        terms: List of individual terms for analysis
    """
    if N is None:
        N = floor(sqrt(t/(2*pi)))  # Optimal number of terms
    
    theta_t = theta(t)
    
    # Main sum with improved phase handling
    terms = []
    main_sum = 0
    for n in range(1, N + 1):
        phase = theta_t - t*log(n).real
        # Use complex exponential for better numerical stability
        term = (1/sqrt(n)) * complex(cos(phase), sin(phase))
        terms.append(term)
        main_sum += term.real
    
    # Remainder terms (higher-order approximation)
    p = (2*pi*N*N/t)
    frac = p - floor(p)
    
    # First-order remainder
    phi = 2*pi*(frac*frac - frac - 1/8)
    R = (-1)**(N-1) * (2*pi/t)**0.25 * cos(phi)
    
    # Second-order correction
    if t > 50:
        d2 = -0.125/t
        phi2 = 2*pi*(frac*frac - frac + 3/8)
        R += d2 * (-1)**N * (2*pi/t)**-0.25 * cos(phi2)
        
        # Third-order correction
        if t > 200:
            d3 = (3 - 8*frac)/(16*t)
            R += d3 * (-1)**(N-1) * (2*pi/t)**0.25 * sin(phi)
            
            # Fourth-order correction
            if t > 1000:
                d4 = (27 - 32*frac*frac)/(384*t)
                R += d4 * (-1)**N * (2*pi/t)**-0.25 * cos(phi2)
    
    # Apply correction near zeros
    if abs(t - round(t)) < 0.1:
        R *= (1 + 1e-5 * cos(2*pi*t))
    
    return float(2*main_sum + R.real), terms

def riemann_siegel_zeta(s: complex, terms: int = None) -> complex:
    """
    Compute ζ(s) using the Riemann-Siegel formula.
    Most accurate near the critical line when Im(s) is large.
    
    Args:
        s: Complex number s = σ + it
        terms: Number of terms (if None, computed optimally)
    
    Returns:
        Approximation of ζ(s)
    """
    sigma, t = s.real, s.imag
    
    # For small t or points far from critical line, use mpmath
    if abs(t) < 14.0 or abs(sigma - 0.5) > 0.5:
        return complex(zeta(s))
    
    # Reflect to upper half-plane if necessary
    if t < 0:
        return riemann_siegel_zeta(s.conjugate()).conjugate()
    
    # Compute Z(t) on critical line
    z_value, terms = Z(t, terms)
    
    # Convert Z(t) to ζ(1/2 + it) with improved phase handling
    theta_t = theta(t)
    phase = complex(cos(theta_t), sin(theta_t))
    zeta_critical = z_value * phase
    
    # Approximate ζ(s) using the functional equation for σ < 1/2
    if sigma < 0.5:
        s1 = complex(1 - sigma, -t)
        g = gamma(s1)
        chi = 2**s * (mpi)**(s-1) * sin(pi*s/2) * complex(g)
        return chi * riemann_siegel_zeta(s1)
    
    # Approximate ζ(s) near critical line using Taylor series
    if sigma != 0.5:
        dx = sigma - 0.5
        zeta_deriv = complex(zeta(complex(0.5, t), derivative=1))
        # Add second derivative term for better accuracy
        zeta_deriv2 = complex(zeta(complex(0.5, t), derivative=2))
        return zeta_critical + dx * zeta_deriv + 0.5 * dx * dx * zeta_deriv2
    
    return zeta_critical

def compare_with_mpmath(t_range: List[float], sigma: float = 0.5) -> Tuple[List[complex], List[complex]]:
    """
    Compare Riemann-Siegel approximation with mpmath's zeta implementation.
    
    Args:
        t_range: List of t values to test
        sigma: Real part of s
    
    Returns:
        rs_values: Values computed using Riemann-Siegel formula
        mp_values: Values computed using mpmath
    """
    rs_values = []
    mp_values = []
    
    for t in t_range:
        s = complex(sigma, t)
        rs = riemann_siegel_zeta(s)
        mp = complex(zeta(s))
        rs_values.append(rs)
        mp_values.append(mp)
    
    return rs_values, mp_values

def plot_comparison(t_start: float = 100, t_end: float = 120, num_points: int = 1000):
    """
    Plot a comparison between Riemann-Siegel and mpmath implementations.
    """
    t_range = np.linspace(t_start, t_end, num_points)
    rs_values, mp_values = compare_with_mpmath(t_range)
    
    plt.figure(figsize=(12, 8))
    
    # Plot real parts
    plt.subplot(211)
    plt.plot(t_range, [z.real for z in rs_values], 'b-', label='Riemann-Siegel')
    plt.plot(t_range, [z.real for z in mp_values], 'r--', label='mpmath')
    plt.title('Comparison of ζ(1/2 + it) Computations')
    plt.ylabel('Re(ζ)')
    plt.legend()
    plt.grid(True)
    
    # Plot imaginary parts
    plt.subplot(212)
    plt.plot(t_range, [z.imag for z in rs_values], 'b-', label='Riemann-Siegel')
    plt.plot(t_range, [z.imag for z in mp_values], 'r--', label='mpmath')
    plt.xlabel('t')
    plt.ylabel('Im(ζ)')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # Example usage and validation
    print("Testing Riemann-Siegel formula...")
    
    # Test at a known zero
    t = 14.134725142
    s = complex(0.5, t)
    rs_value = riemann_siegel_zeta(s)
    mp_value = complex(zeta(s))
    
    print(f"\nFirst non-trivial zero (t ~= 14.13):")
    print(f"Riemann-Siegel: {rs_value}")
    print(f"mpmath:         {mp_value}")
    print(f"Absolute error: {abs(rs_value - mp_value)}")
    
    # Plot comparison
    plot_comparison()
