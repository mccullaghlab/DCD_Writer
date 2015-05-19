#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

# USAGE:
# ./nucleic.ions.dcd.py system_descriptor prmtop_file traj_file production_number
# load in the prmtop file and whole trajectory file; writes a new trajectory not including water;

# PREAMBLE:

import MDAnalysis
import sys

system = sys.argv[1]
prmtop = sys.argv[2]
traj = sys.argv[3]
prod_num = sys.argv[4]

# SUBROUTINES:

# MAIN PROGRAM:

# set the universe object
u = MDAnalysis.Universe('%s' %(prmtop), '%s' %(traj))

# set atom selection for all atoms of interest (in this case: residues that are not WAT)
nucleic_ions = u.selectAtoms('not resname WAT')

# Writer object that spans the whole trajectory and writes an abbreviated trajectory only including atoms described by atom selection
with MDAnalysis.Writer('%s.nucleic.prod.%s.dcd' %(system, prod_num), nucleic_ions.numberOfAtoms()) as V:
	for ts in u.trajectory:
		V.write(nucleic_ions)

# NOTES: 
# time values for the new dcd files will not be accurate.

