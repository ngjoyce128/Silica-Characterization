import math
import numpy as np
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=True, type=str, help="REAX connectivity file")
parser.add_argument('-tr', '--traj', required=True, type=str, help="REAX connectivity file")
parser.add_argument('-f1','--frame_size_bond', required = True, type = int, help = '# of lines for each frame')
parser.add_argument('-f2','--frame_size_traj', required = True, type = int, help = '# of lines for each frame')
parser.add_argument('-t','--type', required = True, type = str, help = 'bulk or slab')

args = parser.parse_args()
datafile = args.input
frame_size_bond = args.frame_size_bond
frame_size_traj = args.frame_size_traj
traj = args.traj
typ = args.type


def sio():
	xyz = [] #list of[ID,x,y,z]
	ID = []
	linecount1 = 0
	linecount2 = 0
	linex = 0
	liney = 0
	linez = 0
	lx = 0
	ly = 0
	lz = 0
	f_indx = 0


	with open(traj) as f:
		for line in f:
			linex = 6 + f_indx*frame_size_traj
			liney = 7 + f_indx*frame_size_traj
			linez = 8 + f_indx*frame_size_traj
			linecount1 += 1
			part = line.split()
			
			if linecount1 == linex:
				lx = 2*float(part[1])
			elif linecount1 == liney:
				ly = 2*float(part[1])
			elif linecount1 == linez:
				lz = 2*float(part[1])


			if len(part) == 5:
				xyz.append([part[1], float(part[2]), float(part[3]), float(part[4])])
				ID.append(part[1])
	
			if linecount1 % frame_size_traj == 0:
				#print(lx,ly,lz)
				f_indx += 1
				sioID = [] # list of IDs of all Si-O bonds
				with open(datafile) as f:
					for line in f:
						linecount2 += 1
						part = line.split()
						if part[0].isdigit():
							if float(part[1]) == 1:
								if float(part[2]) == 2:	
									sioID.append([part[0],part[3]])
									sioID.append([part[0],part[4]])
								elif float(part[2]) == 3:	
									sioID.append([part[0],part[3]])
									sioID.append([part[0],part[4]])
									sioID.append([part[0],part[5]])	
								elif float(part[2]) == 4:	
									sioID.append([part[0],part[3]])
									sioID.append([part[0],part[4]])
									sioID.append([part[0],part[5]])
									sioID.append([part[0],part[6]])	
								elif float(part[2]) == 5:	
									sioID.append([part[0],part[3]])
									sioID.append([part[0],part[4]])
									sioID.append([part[0],part[5]])
									sioID.append([part[0],part[6]])
									sioID.append([part[0],part[7]])
								elif float(part[2]) == 6:	
									sioID.append([part[0],part[3]])
									sioID.append([part[0],part[4]])
									sioID.append([part[0],part[5]])
									sioID.append([part[0],part[6]])
									sioID.append([part[0],part[8]])
			
						if linecount2 % frame_size_bond == 0:								
							sio = []
							for i in range(len(sioID)):
								Si = sioID[i][0]
								O = sioID[i][1]
								iSi = ID.index(Si)
								iO = ID.index(O)
								dx = xyz[iSi][1] - xyz[iO][1]
								dy = xyz[iSi][2] - xyz[iO][2]
								dz = xyz[iSi][3] - xyz[iO][3]
								xx = np.round(dx/lx, decimals = 0)
								yy = np.round(dy/ly, decimals = 0)
								zz = np.round(dz/lz, decimals = 0)
								dxSiO = dx - (lx*xx)
								dySiO = dy - (ly*yy)
								if typ == "bulk":
									dzSiO = dz - (lz*zz)
								else:
									dzSiO = dz
				
								dSiO = math.sqrt(dxSiO**2 + dySiO**2 + dzSiO**2)
								sio.append(dSiO)
#								print(dSiO)
								#print(sio)
								#print(len(sio))
				xyz.clear()
				ID.clear()
				sioID.clear()
				#sio.clear()
	for i in range(len(sio)):
		print(sio[i])
	return
sio()
#data = sio("tail100.lammpstrj","bond_tail100_BO")
