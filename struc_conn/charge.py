import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=True, type=str, help="REAX connectivity file")
#parser.add_argument('-tr', '--traj', required=True, type=str, help="REAX connectivity file")
#parser.add_argument('-cn','--CN', required=True,type= float, help="Coordination number")
parser.add_argument('-t','--type', required=True,type= float, help="Coordination number")

args = parser.parse_args()
datafile = args.input
atom_type = args.type


with open(datafile) as f:
	for line in f:
		parts = line.split()
		if len(parts) == 3 and int(parts[0]) == atom_type:
			print(parts[2])

