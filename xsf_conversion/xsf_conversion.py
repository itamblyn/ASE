#!/usr/bin/env python

import numpy as np
import ase
import ase.io.vasp
from ase import Atoms
from ase.structure import nanotube
from ase.visualize import view

trajectory = ase.io.read('OUTCAR',index=':',format='vasp-out')

#index = 1
#energy = -10
#cell 

def aenet_xsf_writer(index, energy, cell, Z, symbols, positions, forces):
    outputFile = open('structure' + str(index).zfill(4) + '.xsf','w')
    outputFile.write('# total energy = ' + str(energy) + ' eV \n\n')
    outputFile.write('CRYSTAL\n')
    outputFile.write('PRIMVEC\n')
    outputFile.write(" ".join(str(x) for x in cell[0]) + '\n')
    outputFile.write(" ".join(str(x) for x in cell[1]) + '\n')
    outputFile.write(" ".join(str(x) for x in cell[2]) + '\n')
    outputFile.write('PRIMCORD\n')
    outputFile.write(str(len(Z)) + ' 1\n')

    data = np.hstack((positions, forces))

    for i in range(len(symbols)):
        data_string = " ".join(str(x) for x in data[i])
        outputFile.write(str(symbols[i]) + ' ' + data_string +'\n')
 
    outputFile.close()
    return

index = 0    

for snapshot in trajectory:

    symbols = snapshot.get_chemical_symbols()
    Z = snapshot.get_atomic_numbers()
    energy = snapshot.get_potential_energy()
    forces = snapshot.get_forces()
    positions = snapshot.get_positions()
    cell = snapshot.get_cell()
    aenet_xsf_writer(index, energy, cell, Z, symbols, positions, forces)
    index += 1
