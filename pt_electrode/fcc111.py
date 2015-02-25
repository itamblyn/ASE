#!/usr/bin/env python

import numpy
from ase import io
from ase import Atoms
from ase.visualize import view
from ase.lattice.surface import fcc111

#lattice_constant = 4.01  # http://www.hindawi.com/journals/apc/2011/305634/ GGA-PBE
lattice_constant = 3.975 # vasp, Pt@PBE
                         #  experiment is 3.92 
#lattice_constant = 4.1839615096998237
#lattice_constant = 4.06 # this is what I get for the 18e psp from Paratec

slab = fcc111('Pt', size=(4,4,9),a=lattice_constant, vacuum=0.0, orthogonal=True)
print 'used ', lattice_constant
io.write('slab.vasp', slab)
print 'Warning, Z-component of poscar seems to be incorrect'
io.write('slab.xyz', slab)

x1 = 4*(lattice_constant*(1./2)**.5) 
x2 = 4*(lattice_constant*(1./2)**.5)*numpy.cos(60*numpy.pi/180)
y2 = 4*(lattice_constant*(1./2)**.5)*numpy.sin(60*numpy.pi/180)

print 'Angstrom '
print str(round(x1,6)),            0.00, 0.00
print str(round(x2,6)), str(round(y2,6)), 0.00

print 'Bohr'
print str(round(x1/.529177,6)),            0.00, 0.00
print str(round(x2/.529177,6)), str(round(y2/.529177,6)), 0.00

