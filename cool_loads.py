#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 08:41:02 2021

@author: cghiaus
"""

import psychro as psy
# constants
c = 1e3                     # J/kg K, air specific heat
l = 2496e3                  # J/kg, water vapor latent heat
ρ = 1.2                     # kg/m3, air density

# Building dimensions
length = 20                 # m
width = 30                  # m
height = 3.5                # m

# Occupants
persons = 100               # number
sens_heat_person = 60       # W / person
latent_heat_person = 40     # W / person

load_m2 = 15                # W/m2, auxiliary electrical laods
solar_m2 = 150              # W/m2 of window area, solar gains
ACH = 1                     # room_volume/h, Air Changes per Hour
U_wall = 0.4                # W/K, overall heat transfer coeff. walls & ceiling
U_window = 3.5              # W/K, overall heat transfer coeff. windows

# Outdoor and indoor conditions
θo, φo = 32, 0.5            # outdoor temperature & relative humidity
θI, φI = 26, 0.5            # indoor temperature & relative humidity
wo = psy.w(θo, φo)
wI = psy.w(θI, φI)

# Surfaces
floor_area = length * width
room_volume = length * width * height
surface_envelope = 2 * (length + width) * height
surface_window = 0.3 * surface_envelope
surface_wall = 0.7 * surface_envelope
surface_exchg = surface_wall + floor_area

# Overall heat coefficient
UA = U_wall * surface_exchg + U_window * surface_window

# Outdoor air infiltration mass flow rate
mi = ACH * room_volume / 3600 * ρ

# Heat gains
solar_gains = solar_m2 * surface_window
electrical_load = load_m2 * floor_area
Qsa = persons * sens_heat_person + solar_gains + electrical_load
Qla = persons * latent_heat_person

# Heat loads of the thermal zone
QsTZ = (UA + mi * c) * (θo - θI) + Qsa  # sensible
QlTZ = mi * l * (wo - wI) + Qla         # latent

# Supply (dry) air mass flow rate
θS = θI - 15                            # °C supply air temperature
m = QsTZ / c / ((θI - θS))

print(f'QsTZ = {QsTZ:.0f} W \t - sensible heat load of the thermal zone')
print(f'QlTZ = {QlTZ:.0f} W \t - latent heat load of the thermal zone')
print(f'UA = {UA:.0f} W/K \t - overall heat coefficient ')
print(f'mi = {mi:.2f} kg/s \t - outdoor air infiltration mass flow rate')
print(f'Qsa = {Qsa:.0f} W \t - sensible auxiliary heat')
print(f'Qla = {Qla:.0f} W \t - latent auxiliary heat')
print(f'm = {m:.1f} kg/s \t - mass flow rate of (dry) supply air')
