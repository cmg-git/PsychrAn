#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 10:42:54 2021

@author: cghiaus
"""

import sympy as sym

# create a "symbol" called x
a, b, C, Mv, Mda, p, x, θ = sym.symbols('a, b, C, Mv Mda p x θ')

# a = 17.269_388_2    # over water
# b = 273.16 - 35.86
# C = 610.78

# ps = 610.78 * sym.exp(a * θ / (θ + b))    # [Pa] eq (6)

ps = C * sym.exp(a * θ / (θ + b))    # [Pa] eq (6)
w = ps / (p - ps)

wsp = sym.simplify(sym.diff(w, θ))
print(wsp)
