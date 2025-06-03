#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
# import numpy as np
import math

import scipy.constants as scc

def lQ(T: float, m: float) -> float:
    return scc.h / math.sqrt(2 * math.pi * m * scc.k * T )

def mu(T: float, Z_int: float, P: float, v_Q: float) -> float:
    return - scc.k * T * math.log((scc.k * T * Z_int)/(P *v_Q))

amu = 1.660539e-27 # kg

def main() -> int:

    T = 310 # K
    Z_int = 3. * 72.1 # Ze * q_rot
    P = 20265 # 0.2 atm
    m = 32 * amu # O2

    l_Q = lQ(T, m)
    v_Q = l_Q ** 3

    print(f"lQ = {l_Q}")
    print(f"vQ = {v_Q}")
    print(f"mu = {mu(T, Z_int, P, v_Q)} J = {mu(T, Z_int, P, v_Q) / scc.electron_volt} eV")
    return 0



if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit