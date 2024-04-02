def quietAtoms(climax_file, atoms, output_file='output.aclimax', set_to_one=False):
    """Sets the Neutron cross-section of the atoms passed to zero
    
    If you want to have just one atom, please type in the number of that atom.
    but if you want to several atoms together, please type in the number of others, for instance, 1 2 3 4 5
    if you want 2 and 3, please type in 1 4 5!
    
    Args:
        climax_file (str): name of the (o)aclimax file to be manipulated
        atoms ([list<int>, int]): atom numbers whose cross section will be set to zero. If only one atom is provided, all except that atom are quieted.
        output_file(str, optional): name of the output file. ouput.aclimax is default
    """
    if isinstance(atoms, int):
        atoms = [atoms]

    in_file = open(climax_file, 'r')
    lines = in_file.readlines()
    in_file.close()

    new_lines = []
    for line in lines: 
        parts = line.split()
        if len(parts) >= 8:
            if len(atoms) > 1:
                if int(parts[0]) in atoms:
                    for i in range(7, len(parts)):
                        line = line.replace(parts[i], '0.000000')
            else:
                if int(parts[0]) not in atoms:
                    for i in range(7, len(parts)):
                        line = line.replace(parts[i], '0.000000')
                elif set_to_one:
                    for i in range(7, len(parts)):
                        line = line.replace(parts[i], '1.000000')
        new_lines.append(line)
    out_file = open(output_file, 'w')
    out_file.writelines(new_lines)
    out_file.close()

def runOclimax(climax_file, output_file='output.csv'):
    """Runs oclimax on the given (o)aclimax file and writes the output to output_file

    Args:
        climax_file (str): the (o)aclimax file you want to run
        output_file (str, optional): The name of the output file. Defaults to 'output.csv'.
    """
    import os
    import glob
    os.system("oclimax run {}".format(climax_file))
    csv_files = glob.glob('*.csv')
    for file in csv_files:
        if 'vis' in file:
            os.rename(file, output_file)
 




#############################################################################

atom = int(input("Atoms "))
outputfile = input("please type in the name of the output file ")
climax_file = 'out.oclimax'
aclimax_file = "output.aclimax"
quietAtoms(climax_file = climax_file , atoms = atom)
runOclimax(climax_file = aclimax_file , output_file = f"output{outputfile}.csv")