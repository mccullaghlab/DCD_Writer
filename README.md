# Summary 
Python code, using MDAnalysis, to take in a .dcd file and write a new .dcd file. Useful for turncating large .dcd files down to smaller file sizes by removing solvent/unwanted atoms. 

# USAGE:
```python
./dcd_writer.py <system_name> <pdb/prmtop/psf file> <trajectory file> <production number>
```
  Use dcd_writer.py script when production run completed successfully.
  
  <system name> corresponds to some descriptor of the simulation to be used in the naming of the new .dcd file.
  
  <pdb/prmtop/psf file> is the initial pdb, prmtop, or pdb file that contains all atoms.
  
  <trajectory file> is the .dcd file desired to be truncated
  
  <production number> a second description for naming of the new .dcd file 

```python  
./dcd_writer.fix.py <system_name> <pdb/prmtop/psf file> <trajectory file> <production number> <final frame number>
```
  Use dcd_writer.fix.py script when production run has terminated prematurely.

  <final frame number> corresponds to the last frame written to the restart files. 

## NOTES:
  MDAnalysis must be successfully installed on your local computer.
  
  Must alter the first line of the scripts to point towards the python command on the local computer.
  
  
  
