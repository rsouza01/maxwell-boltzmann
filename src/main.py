#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
import math

import scipy.constants as scc

# Define the function to be plotted
def func(x):
    return np.exp(-x)

def maxwell_distr(v, m, T):
    return (m/(2 * np.pi * scc.k * T)) **(3./2.) * 4 * np.pi * v**2 * np.exp(-m * v**2 / (2 * scc.k * T))


# def maxwell_speed_distribution(v, T, m):
#     k_B = 1.380649e-23  # Boltzmann constant in J/K
#     return (m / (2 * np.pi * k_B * T))**(3/2) * 4 * np.pi * v**2 * np.exp(-m * v**2 / (2 * k_B * T))


def main() -> int:

    atomic_weight = 28
    T = [
        {"temp" : 300, "color": 'blue'},
        {"temp" : 600, "color": 'red'},
    ]

    m = atomic_weight * scc.atomic_mass
    
    # Generate x values from 0 to 100
    v = np.linspace(0, 1700, 1700)

    plt.figure(figsize=(10, 6))
    
    for temp in T:
        temperature = temp["temp"]
        color = temp["color"]
        y = maxwell_distr(v, m, temperature)
        plt.plot(v, y, label=f'T={temperature}', color=f'{color}')

    # Add labels and title
    plt.xlabel('v (m/s)')
    plt.ylabel('D(v) (s/m)')
    plt.legend()
    plt.grid(True)

    # Save the plot as a .png file
    plt.savefig('nitrogen_distr.png')

    return 0



if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit