import os
datafile = "bond_tail"
cwd = os.getcwd()
#print(cwd)

count = 0
O = []


with open(datafile) as f:
	for line in f:
		parts = line.split()
		if parts[0].isdigit():
			if float(parts[1]) == 2:
				O.append(parts[0])

with open(datafile) as f:
	for line in f:
		parts = line.split()
		if parts[0].isdigit():
			if float(parts[1]) == 2 and float(parts[2]) == 1:
				if parts[3] in O:
					count += 1
					


print(cwd, count, sep='\t')
