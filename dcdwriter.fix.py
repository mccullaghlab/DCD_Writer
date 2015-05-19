#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

# USAGE:
# ./nucleic.ions.dcd.fix.py system_descriptor prmtop_file traj_file production_number final_frame
# load in the prmtop file and whole trajectory file; writes a new trajectory not including water; stops at frame corresponding to last restart file written to. 

# PREAMBLE:

import numpy as np 
import MDAnalysis
import sys

system = sys.argv[1]
prmtop = sys.argv[2]
traj = sys.argv[3]
prod_num = sys.argv[4]
stop = int( sys.argv[5])

# SUBROUTINES:

# MAIN PROGRAM:

# set the universe object
u = MDAnalysis.Universe('%s' %(prmtop), '%s' %(traj))

# set atom selection for all atoms that are NOT part of residues WAT (water)
nucleic_ions = u.selectAtoms('not resname WAT')

# Writer object that spans the whole trajectory and writes an abbreviated trajectory only including atoms described by atom select
with MDAnalysis.Writer('%s.nucleic.prod.%s.dcd' %(system, prod_num), nucleic_ions.numberOfAtoms()) as V:
	for ts in u.trajectory[0:stop]:
		V.write(nucleic_ions)


# NOTES: 
# time values for the new dcd files will not be accurate.

