# INS-simulation-tutorial

Optimization material structure using VASP, we need 4 files as input. 

1. INCAR (The central input file of VASP, which determines what to do and how to do it.)
2. POSCAR (Crystal structure)
3. POTCAR (Pseudopotential) `cat /global/common/software/m2734/ray/potentials_vasp/X/POTCAR>> POTCAR` X is the element. There is new POTCAR file `/global/common/software/nersc/pm-2022q2/sw/vasp/pseudopotentials/PBE/potpaw_PBE/<the element>/POTCAR>> POTCAR`
4. KPOINTS (Mesh grid)

We can use vaspkit to generate input files (https://vaspkit.com/index.html), GNU-parallel (https://www.gnu.org/software/parallel/sphinx.html)

Using NERSC (HPC), we also need a run file to submit the calculation.

After simulation, we will get lots of files
1. CONTCAR (Updated geometry data at the end of a run)
2. OUTCAR (Gives detailed output of a VASP run, including a summary of the used input parameters; Information about the electronic steps, KS-eigenvalues; Stress tensors; Forces on the atoms; Local charges and magnetic moments; Dielectric properties)
3. OSZICAR (Chosen SCF algorithm; Convergence of the total energy, charge- and spin densities; Free energies; Magnetic moments of the cell)
4. XDATCAR (Contains updated ionic positions of each ionic step)
5. DOSCAR (Contains the total and integrated DOS and optionally the local partial DOS)
6. WAVECAR (Contains the wave function coefficients)
7. vasprun.xml (Main output file in xml format)
8. EIGENVAL (Contains Kohn-Sham eigenvalues for each k point after the end of the calculation)
9. IBZKPT (Contains k-point coordinates and weights)
10. CHGCAR (Stores the charge density and the PAW one-center occupancies and can be used for restarting VASP calculations)


The next step is creating displacements using phonopy (https://phonopy.github.io/phonopy/), depends on the size of molecules, we will get different number of POSCARs. By doing this step, we will get set of forces.
1. Copy CONTCAR file from optimization step, `cp ../CONTCAR .`. Then, rename to POSCAR `mv CONTCAR POSCAR`
2. command: `phonopy -d --dim="x y z" -c POSCAR`. x, y, z are supercell sizes. We will get POSCARs and phonopy_disp.yaml (contains information used to create supercells with displacements)
3. Then we rename the POSCARs and put into subfolders, command: `for i in {001..#}; do mkdir $i; mv POSCAR-$i $i/POSCAR; done` We also need to copy all the other input files (INCAR, POTCAR, KPOINTS, and run file) into each folder, `parallel "cd {} && cp ../run ." ::: {001..nnn}`.
4. Change the # of NSW (the number of maximum ionic steps) into 0. We can also reduce KPOINTS grid.
5. Submit all the calculations in each folder, command: `for i in {001..#}; do cd $i; sbatch runfile; cd ..; done` or `parallel "cd {} && sbatch run" ::: {001..nnn}`

Now, we have force constants from all calculations from previous step. Let's do the post process
1. command: `phonopy -f {001..#}/vasprun.xml` to create FORCE_SETS.
2. Mesh sampling calculation, prepare the file "mesh.conf".
3. ```
   ATOM_NAME = C O H
   DIM = 2 2 2
   MP = 8 8 8
   EIGENVECTORS = .TRUE.
   ```
4. `phonopy -p mesh.conf` to calculate phonons and DOS. We will get "phonopy.yaml" and "mesh.yaml" file.

Last, use OCLIMAX to draw INS spectrum.
`python3.9 /global/common/software/m2734/ray/oclimax.py`


Second part: 
Open babel transfer file command `obabel -i <input_file_extension> input_file -o <output_file_extension> -O output_file`

References
1. https://www.vasp.at/wiki/index.php/The_VASP_Manual
2. J. Chem. Theory Comput. 2019, 15, 3, 1974–1982
