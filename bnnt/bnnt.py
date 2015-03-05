#!/usr/bin/env python

import numpy as np
from ase import io
from ase import Atoms
from ase.structure import nanotube
from ase.visualize import view

BCN = False
BN = False 
cbond = 1.4606961810497532
lxoverride = 25.


def convert_BCN(tube):

    i = 0
    while i < len(tube):
        tube[i+0].symbol = 'B'
        tube[i+1].symbol = 'C'
        tube[i+2].symbol = 'N'
        i += 3
    return tube

def convert_BN(tube):

    i = 0
    while i < len(tube):
        tube[i+0].symbol = 'B'
        tube[i+1].symbol = 'N'
        i+=2
    return tube

tube = nanotube(6, 6, length=6, bond=cbond, symbol='C')
lx, ly, lz = tube.get_cell()[0][0], tube.get_cell()[1][1], tube.get_cell()[2][2]

print 'Set lx and ly to ', lxoverride

tube.set_cell([lxoverride,lxoverride,lz], scale_atoms=False)

if BCN == True: convert_BCN(tube)
if BN == True: convert_BN(tube)

tube.center()

io.write('POSCAR.1', tube, sort=True)

tube2 = nanotube(11, 11, length=6, bond=cbond, symbol='C')

lx, ly, lz = tube2.get_cell()[0][0], tube2.get_cell()[1][1], tube2.get_cell()[2][2]
print 'Set lx and ly to ', lxoverride
tube2.set_cell([lxoverride,lxoverride,lz], scale_atoms=False)
tube2.center()

if BCN == True: convert_BCN(tube2)
if BN == True: convert_BN(tube2)

io.write('POSCAR.2', tube2, sort=True)

tube.extend(tube2)

io.write('POSCAR.joined', tube, sort=True)


view(tube)

