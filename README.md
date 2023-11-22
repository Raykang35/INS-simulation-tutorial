# INS-simulation-tutorial

Optimization material structure using VASP, we need 4 files as input.
(1) INCAR (The central input file of VASP, which determines what to do and how to do it.)
(2) POSCAR (Crystal structure)
(3) POTCAR (Pseudopotential)
(4) KPOINTS (Mesh grid)
Using NERSC (HPC), we need a run file to submit the calculation.

After simulation, we will get lots of files
(1) CONTCAR (Updated geometry data at the end of a run)
(2) OUTCAR (Gives detailed output of a VASP run, including a summary of the used input parameters; Information about the electronic steps, KS-eigenvalues; Stress tensors; Forces on the atoms; 
Local charges and magnetic moments; Dielectric properties)
(3) OSZICAR (Chosen SCF algorithm; Convergence of the total energy, charge- and spin densities; Free energies; Magnetic moments of the cell)
(4) XDATCAR
(5) DOSCAR
