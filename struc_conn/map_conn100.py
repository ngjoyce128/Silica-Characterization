import math
import numpy as np
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-tr', '--traj', required=True, type=str, help="REAX connectivity file")
parser.add_argument('-c','--cutoff', required = True, type = float, help = 'cutoff distance')
parser.add_argument('-f','--frame_size_traj', required = True, type = int, help = '# of lines for each frame')
parser.add_argument('-t','--type', required = True, type = str, help = 'bulk or slab')

args = parser.parse_args()
frame_size_traj = args.frame_size_traj
typ = args.type
traj = args.traj
d_cutoff = args.cutoff



lx = np.loadtxt(traj, skiprows = 5, max_rows = 1, usecols = 1)
ly = np.loadtxt(traj, skiprows = 6, max_rows = 1, usecols = 1)
lz = np.loadtxt(traj, skiprows = 7, max_rows = 1, usecols = 1)

lx *= 2
ly *= 2
lz *= 2

def map_connectivity(datafile):
	si = []
	o = []
	linecount = 0
	with open(datafile) as f:
		for line in f:
			linecount += 1
			part = line.split()
			if len(part) == 5:
				if float(part[0]) == 1:
					si.append([part[1],float(part[2]),float(part[3]),float(part[4])])
				elif float(part[0]) == 2:
					o.append([part[1],float(part[2]),float(part[3]),float(part[4])])
			if linecount % 585 == 0:

				print("Step: ", int(linecount/585))  #just need these lines to resemblance the actual bonds.reaxc file
				print("Connectivity map")
				print("RDF based")
				print("Start")
				print("Start")
				print("Start")
				print("Start")
				print("Start")
				for i in range(len(si)):
					dx = [si[i][1] - o[j][1] for j in range(len(o))]
					dy = [si[i][2] - o[j][2] for j in range(len(o))]
					dz = [si[i][3] - o[j][3] for j in range(len(o))]
					xx = np.round(dx/lx, decimals = 0)
					yy = np.round(dy/ly, decimals = 0)
					zz = np.round(dz/lz, decimals = 0)
					dxSiO = dx - (lx*xx)
					dySiO = dy - (ly*yy)
					if typ == 'bulk':						
						dzSiO = dz - (lz*zz)
					else:
						dzSiO = dz
					dSiO = [math.sqrt(dxSiO[j]**2 + dySiO[j]**2 + dzSiO[j]**2) for j in range(len(o))]
					count = 0
					Ol = []
					for k in range(len(dSiO)):
						if dSiO[k] <= d_cutoff:
							count += 1	
							Ol.append(o[k][0])

					print(si[i][0],1,count,*Ol, sep='\t')


				for i in range(len(o)):
					dx1 = [o[i][1] - si[j][1] for j in range(len(si))]
					dy1 = [o[i][2] - si[j][2] for j in range(len(si))]
					dz1 = [o[i][3] - si[j][3] for j in range(len(si))]
					xx1 = np.round(dx1/lx, decimals = 0)
					yy1 = np.round(dy1/ly, decimals = 0)
					zz1 = np.round(dz1/lz, decimals = 0)
					dxOSi = dx1 - (lx*xx1)
					dyOSi = dy1 - (ly*yy1)
					if typ == 'bulk':						
						dzOSi = dz1 - (lz*zz1)
					else:
						dzOSiO = dz1
					dzOSi = dz1 - (lz*zz1)
					dOSi = [math.sqrt(dxOSi[j]**2 + dyOSi[j]**2 + dzOSi[j]**2) for j in range(len(si))]
					count1 = 0
					Sil = []
					for k in range(len(dOSi)):
						if dOSi[k] <= d_cutoff:
							count1 += 1	
							Sil.append(si[k][0])
					print(o[i][0],2,count1,*Sil, sep='\t')
				count = 0
				count1 = 0
				si.clear()
				o.clear()
				Ol.clear()
				Sil.clear()
	return

data = map_connectivity("final.lammpstrj")
				

