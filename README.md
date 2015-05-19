# Summary 
Python code, using MDAnalysis, to take in a .dcd file and write a new .dcd file. Useful for turncating large .dcd files down to smaller file sizes by removing solvent/unwanted atoms. 

# USAGE:
```python
./dcd_writer.py <system_name> <pdb/prmtop/psf file> <trajectory file> <production number>
```
  Use dcd_writer.py script when a MD simulation ran successfully/completely.
  
  `<system name>` corresponds to some descriptor of the simulation to be used in the naming of the new .dcd file.
  
  `<pdb/prmtop/psf file>` is the initial pdb, prmtop, or psf file that contains all atoms.
  
  `<trajectory file>` is the .dcd file desired to be truncated.
  
  `<production number>` a second description for naming of the new .dcd file. 

```python  
./dcd_writer.fix.py <system_name> <pdb/prmtop/psf file> <trajectory file> <production number> <final frame number>
```
  Use dcd_writer.fix.py script when the production run has terminated prematurely. More often than not, the trajectory of your simulation will have been written to the .dcd file more recently than the restart file. You will use the restart file to restart the next batch of simulations. Therefore, your .dcd file will contain too many frames (frames that should not be analyized). For analysis purposes, you should remove the extra frames from the .dcd file. Use the dcd_writer.fix.py script to do so. 
  
  This code has very similar usage as the dcd_writer.py script, but includes a 5th command line option to specify the frame at which the restart file was written to. This frame is the last frame to be included in the new .dcd file. 

  `<final frame number>` corresponds to the last frame written to the restart files. 

## NOTES:
  MDAnalysis must be installed on your local computer.
  
  You must alter the first line of the scripts to point towards the python command on the local computer.
  
  The dcd_writer does not pass on time values from the old trajectory to the new trajectory. Be aware of this and keep track of frame numbers/steps and the corresponding time values. 
  
# Atom Selection:
Using the sample scripts provided, the solvent (water) is removed from a trajectory. The molecules/atoms to be INCLUDED in the new .dcd file are specified in the following line:
```python
solute = u.selectAtoms('not resname WAT')
```
The `'not resname WAT'` atom selection tells MDAnalysis to focus on residues that are not resname WAT. This atom selection can be changed. The atom selection keywords are very similar to the VMD atom selection keywords used in developing representations. 
  
