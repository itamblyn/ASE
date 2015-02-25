#!/usr/bin/env python

import numpy
from ase import io
from ase import Atoms
from ase.visualize import view
from ase.lattice.surface import fcc111

vasp_GW_project = 4.1839615096998237 # this is the lattice const I used for most MD
vasp_Au_vdWDF = 4.25
vasp_Au_ariel = 4.16089

experiment = 4.08

lattice_const = vasp_GW_project

slab = fcc111('Au', size=(5,5,6),a=lattice_const, vacuum=0.0, orthogonal=False)
view(slab)
print 'used ', lattice_const
io.write('slab.cube', slab)
io.write('slab.xyz', slab)


x1 = 5*(lattice_const*(1./2)**.5) 
x2 = 5*(lattice_const*(1./2)**.5)*numpy.cos(60*numpy.pi/180)
y2 = 5*(lattice_const*(1./2)**.5)*numpy.sin(60*numpy.pi/180)

print 'Angstrom '
print str(round(x1,6)),            0.00, 0.00
print str(round(x2,6)), str(round(y2,6)), 0.00

print 'Bohr'
print str(round(x1/.529177,6)),            0.00, 0.00
print str(round(x2/.529177,6)), str(round(y2/.529177,6)), 0.00
