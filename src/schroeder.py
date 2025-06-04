#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
# import numpy as np
import math

import scipy.constants as scc
from scipy.constants import physical_constants

amu = 1.660539e-27 # kg
k_eV, _, _ = physical_constants["Boltzmann constant in eV/K"]

def lQ(T: float, m: float) -> float:
    return scc.h / math.sqrt(2 * math.pi * m * scc.k * T )

def mu(T: float, Z_int: float, P: float, v_Q: float) -> float:
    return - scc.k * T * math.log((scc.k * T * Z_int)/(P *v_Q))

def calc(name: str, T: float, P: float, Z_int: float, m: int, epsilon_ev: float) -> float:

    print(80*"=")
    print(name)
    print(80*"=")
    l_Q = lQ(T, m)
    v_Q = l_Q ** 3

    print(f"lQ = {l_Q}")
    print(f"vQ = {v_Q}")
    _mu = mu(T, Z_int, P, v_Q)
    mu_ev = _mu/scc.electron_volt
    print(f"k_eV = {k_eV} eV")

    print(f"mu = {_mu} J = {mu_ev} eV")

    print(f"epsilon_ev = {epsilon_ev} eV")
    print(f"mu_ev = {mu_ev} eV")

    print(f"epsilon_ev - mu_ev = {epsilon_ev - mu_ev} eV")
    gibbs = math.exp(-(epsilon_ev - mu_ev)/(k_eV * T))
    print(f"gibbs = {gibbs}")

   #  print(math.exp(0.1 * scc.electron_volt/ (scc.k * T)))
    
def main() -> int:
    T = 310 # K
    P = 20265 # 0.2 atm

    # Oxigen
    calc("O_2", T, P, 3. * 72.1, 32 * amu, -0.7)

    # Carbon Monoxide
    calc("CO", T, P, 1. * 108.7, 28 * amu, -0.85)

    return 0



if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit