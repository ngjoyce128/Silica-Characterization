
ID_z = [[],[]]
with open('final.lammpstrj') as f:
	for line in f:
		parts = line.split()
		if len(parts) == 5 and parts[0].isdigit():
			#ID_z.append([parts[1], float(parts[4])])
			ID_z[0].append(parts[1])
			ID_z[1].append(parts[4])

with open('final_stress') as f:
	for line in f:
		parts = line.split()
		if len(parts) == 8 and parts[0].isdigit():
			sp = -float(parts[4]) + 0.5*(float(parts[2]) + float(parts[3]))
			iAtom = ID_z[0].index(parts[1])
			print(ID_z[1][iAtom], sp)
