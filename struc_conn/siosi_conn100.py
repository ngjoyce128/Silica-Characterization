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

def siosi():
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
				f_indx += 1
				
				siosiID = [] # list of IDs of all Si-O bonds
				with open(datafile) as f:
					for line in f:
						linecount2 += 1
						part = line.split()
						if part[0].isdigit():
							if float(part[1]) == 2:
								if float(part[2]) == 2:	
									siosiID.append([part[0],part[3],part[4]])
								elif float(part[2]) == 3:	
									siosiID.append([part[0],part[3],part[4]])
									siosiID.append([part[0],part[3],part[5]])
									siosiID.append([part[0],part[4],part[5]])
								elif float(part[2]) == 4:
									siosiID.append([part[0],part[3],part[4]])
									siosiID.append([part[0],part[3],part[5]])
									siosiID.append([part[0],part[3],part[6]])
									siosiID.append([part[0],part[4],part[5]])
									siosiID.append([part[0],part[4],part[6]])
									siosiID.append([part[0],part[5],part[6]])
					
#print(len(siosiID))
						if linecount2 % frame_size_bond == 0:
							siosi= []
							for i in range(len(siosiID)):
								O = siosiID[i][0]
								Si1 = siosiID[i][1]
								Si2 = siosiID[i][2]
								iSi1 = ID.index(Si1)
								iSi2 = ID.index(Si2)
								iO = ID.index(O)
	
								dx1 = xyz[iSi1][1] - xyz[iO][1]
								dy1 = xyz[iSi1][2] - xyz[iO][2]
								dz1 = xyz[iSi1][3] - xyz[iO][3]
								xx1 = np.round(dx1/lx, decimals = 0)
								yy1 = np.round(dy1/ly, decimals = 0)
								zz1 = np.round(dz1/lz, decimals = 0)
								dxSiO1 = dx1 - (lx*xx1)
								dySiO1 = dy1 - (ly*yy1)
								if typ == "bulk":
									dzSiO1 = dz1 - (lz*zz1)
								else:
									dzSiO1 = dz1
		
								dSiO1 = math.sqrt(dxSiO1**2 + dySiO1**2 + dzSiO1**2)
	
								dx2 = xyz[iSi2][1] - xyz[iO][1]
								dy2 = xyz[iSi2][2] - xyz[iO][2]
								dz2 = xyz[iSi2][3] - xyz[iO][3]
								xx2 = np.round(dx2/lx, decimals = 0)
								yy2 = np.round(dy2/ly, decimals = 0)
								zz2 = np.round(dz2/lz, decimals = 0)
								dxSiO2 = dx2 - (lx*xx2)
								dySiO2 = dy2 - (ly*yy2)
								if typ == "bulk":
									dzSiO2 = dz2 - (lz*zz2)
								else:
									dzSiO2 = dz2
		
								dSiO2 = math.sqrt(dxSiO2**2 + dySiO2**2 + dzSiO2**2)
		# cos(angle) = dot_product (dx1*dx2 + dy1*dy2 + dz1*dz2)/ mag_product (dSiO1*dSiO2)
								dot_product = dxSiO1*dxSiO2 + dySiO1*dySiO2 + dzSiO1*dzSiO2
								mag_product = dSiO1*dSiO2
								angle = math.degrees(math.acos(dot_product/mag_product))
								siosi.append(angle)
							#	print(angle)	

							#print(siosi)
							#print(len(siosi), np.mean(siosi))
				xyz.clear()
				ID.clear()
				#siosi.clear()
				siosiID.clear()
	for i in range(len(siosi)):
		print(siosi[i])
	return
siosi()
#data = siosi("tail100.lammpstrj","bond_tail100_BO")
