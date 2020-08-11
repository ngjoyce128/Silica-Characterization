import numpy as np
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=True, type=str, help="REAX connectivity file")
parser.add_argument('-f','--frame_size', required = True, type = int, help = '# of lines for each frame')

args = parser.parse_args()
datafile = args.input
frame_size = args.frame_size


def cn(datafile):
	linecount = 0
	#Si_CN = []
	#O_CN = []
	countSi3 = 0
	countSi4 = 0
	countSi5 = 0
	countO1 = 0
	countO2 = 0
	countO3 = 0
	percentSi = 100/192
	percentO = 100/384
	with open(datafile) as f:
		for line in f:
			linecount += 1
			part = line.split()
			if part[0].isdigit():
				if float(part[1]) == 1:	
					if float(part[2]) == 3:
						countSi3 += 1
					elif float(part[2]) == 4:
						countSi4 += 1
					elif float(part[2]) == 5:
						countSi5 += 1

	
				elif float(part[1]) == 2:
					if float(part[2]) == 1:
						countO1 += 1
					elif float(part[2]) == 2:
						countO2 += 1
					elif float(part[2]) == 3:
						countO3 += 1
			
			if linecount % frame_size == 0:
				pSi3 = countSi3*percentSi		
				pSi4 = countSi4*percentSi		
				pSi5 = countSi5*percentSi		
				pO1 = countO1*percentO		
				pO2 = countO2*percentO	
				pO3 = countO3*percentO		
				print(pSi3,pSi4,pSi5,pO1,pO2,pO3, sep="\t")
				#print(np.mean(Si_CN), np.mean(O_CN), sep='\t')
				
				countSi3 = 0
				countSi4 = 0
				countSi5 = 0
				countO1 = 0
				countO2 = 0
				countO3 = 0
	return

cn(datafile)

#data = cn("bond_tail100_BO")

				
