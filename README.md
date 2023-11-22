# INS-simulation-tutorial

Optimization material structure using VASP, we need 4 files as input. 

1. INCAR (The central input file of VASP, which determines what to do and how to do it.)
2. POSCAR (Crystal structure)
3. POTCAR (Pseudopotential)
4. KOINTS (Mesh grid)
Using NERSC (HPC), we also need a run file to submit the calculation.

After simulation, we will get lots of files
1. CONTCAR (Updated geometry data at the end of a run)
2. OUTCAR (Gives detailed output of a VASP run, including a summary of the used input parameters; Information about the electronic steps, KS-eigenvalues; Stress tensors; Forces on the atoms; Local charges and magnetic moments; Dielectric properties)
3. OSZICAR (Chosen SCF algorithm; Convergence of the total energy, charge- and spin densities; Free energies; Magnetic moments of the cell)
4. XDATCAR (Contains updated ionic positions of each ionic step)
5. DOSCAR (Contains the total and integrated DOS and optionally the local partial DOS)
6. WAVECAR (Contains the wave function coefficients)


The next step is creating displacements using phonopy (https://phonopy.github.io/phonopy/), depends on the size of molecules, we will get different number of POSCARs.
1. command: phonopy -d --dim="x y z" -c POSCAR. x, y, z are supercell sizes. We will get POSCARs and phonopy_disp.yaml (contains information used to create supercells with displacements)
2. Then we rename the POSCARs and put into subfolders, command: for i in {001..#}; do mkdir $i; mv POSCAR-$i $i/POSCAR; done. We also need to copy all the other input files into each folder.
3. Change the # of NSW into 0.
4.   

