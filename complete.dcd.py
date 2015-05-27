#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

# USAGE:
# ./complete.dcd.py system_descripter pdb_file

# PREAMBLE:

import numpy as np
import MDAnalysis
import sys

system = sys.argv[1]				# system descripter
pdb = sys.argv[2]				# input the location of the pdb file

file_loc = 'nucleic/a14-AP3.nucleic.prod'	# variable used to abbreviate the Universe declaration.

# SUBROUTINES:

# MAIN PROGRAM:

# set the universe object
u = MDAnalysis.Universe('%s' %(pdb), [ <list_of_dcd_files>, '%s.40.dcd' %(file_loc)], delta=2.0)  # delta=2.0ps; sets the timestep between every frame in the dcd to 2ps. Might need to change this is if your dcdWrite or timestep changes...

# Writer object that spans the whole trajectory and writes an abbreviated trajectory only including atoms described by atom select
with MDAnalysis.Writer('%s.nucleic.20-40.dcd' %(system), len(u.atoms)) as W:
	for ts in u.trajectory:
		W.write(u)

# NOTES: 
# time step between dcd frames is 2 ps.


