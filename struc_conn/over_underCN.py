import numpy as np 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=True, type=str, help="REAX connectivity file")
parser.add_argument('-tr', '--traj', required=True, type=str, help="REAX connectivity file")
parser.add_argument('-cn','--CN', required=True,type= float, help="Coordination number")
parser.add_argument('-t','--type', required=True,type= float, help="Coordination number")
args = parser.parse_args()
datafile = args.input
traj = args.traj
cn = args.CN
atom_type = args.type

ID_z = []
ID = []
with open(traj) as f:
	for line in f:
		parts = line.split()
		if parts[0].isdigit() and len(parts) == 5:
			if float(parts[0]) == atom_type:
				ID_z.append([parts[1],parts[4]])
				ID.append(parts[1])
				#print(parts[1], parts[4])

with open(datafile) as f:
	count = 0
	for line in f:
		parts = line.split()
		if parts[0].isdigit() and float(parts[1]) == atom_type and float(parts[2]) == cn:
			count += 1
			iAtom = ID.index(parts[1])
			print(ID_z[iAtom][1])
#print(count)
			

