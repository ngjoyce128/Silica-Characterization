import os
datafile = "log.lammps"
cwd = os.getcwd()
#print(cwd)

count = 0
O = []


with open(datafile) as f:
	for line in f:
		count += 1

					


print(cwd, count, sep='\t')
