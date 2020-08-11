import csv
import math
import itertools
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
typ = args.type
traj = args.traj

siosi2 = []
osio2 = []
siosi3 = []
osio3 = []
siosi4 = []
osio4 = []
siosi5 = []
osio5 = []
siosi6 = []
osio6 = []
siosi7 = []
osio7 = []


f2 = open("Ring2","w")
f3 = open("Ring3","w")
f4 = open("Ring4","w")
f5 = open("Ring5","w")
f6 = open("Ring6","w")
f7 = open("Ring7","w")

f22 = open("siosi2","w")
f33 = open("siosi3","w")
f44 = open("siosi4","w")
f55 = open("siosi5","w")
f66 = open("siosi6","w")
f77 = open("siosi7","w")

f222 = open("osio2","w")
f333 = open("osio3","w")
f444 = open("osio4","w")
f555 = open("osio5","w")
f666 = open("osio6","w")
f777 = open("osio7","w")

def ring():
	si = []
	sio = []
	o3 = []
	linecount = 0
	with open(datafile) as f:
		for line in f:
			linecount += 1
			part = line.split()
			if part[0].isdigit():
				if float(part[1]) == 1:
					si.append(part[0]) #list of ID of Si, for calculation of siosi & osio angles

					if float(part[2]) == 2:		#identify Si atom
						sio.append((part[0], (part[3], part[4])))
					elif float(part[2]) == 3:		#identify Si atom
						sio.append((part[0], (part[3], part[4], part[5])))

					elif float(part[2]) == 4:
						sio.append((part[0], (part[3], part[4], part[5], part[6])))

					elif float(part[2]) == 5:
						sio.append((part[0], (part[3], part[4], part[5], part[6], part[7])))

					elif float(part[2]) == 6:
						sio.append((part[0], (part[3], part[4], part[5],part[6],part[7],part[8])))


				elif float(part[1]) == 2 and float(part[2]) == 3:
					int_group = []
					asc_group = []
					asc_str = []
					int_group = [int(part[3]), int(part[4]), int(part[5])]
					asc_group = sorted(int_group, key = int)
					asc_str = [str(i) for i in asc_group]
					o3.append(asc_str)
				
#print("Si-O connection", sio)
#___________________________________________________________________________________
#All SiSi connections, iD in ascending order (makes it easier for later sorting)
			if linecount % frame_size_bond == 0:
				#print(o3)
				sisi = []
				for i in range(len(sio)):
					for j in range(i+1, len(sio)):
						if set(sio[i][1]) & set(sio[j][1]):
							if float(sio[i][0]) < float(sio[j][0]):
								sisi.append((sio[i][0],sio[j][0]))
							elif float(sio[j][0]) < float(sio[i][0]):
								sisi.append((sio[j][0],sio[i][0]))
#print("SiSi length:", len(sisi))
#print("Si-Si connection:", sisi)
#____________________________________________________________________________________
#TRY LOOKING FOR 2 MEMBER RING:
				r2 = [] # list of 2MR
				r2_1 = []
				count2 = 0
				for i in range(len(sio)):
					for j in range(i+1, len(sio)):
						if set(sio[i][1]) & set(sio[j][1]):
							m1 = set(sio[i][1]) & set(sio[j][1])
							if len(m1) == 2:    # if 2 Si atoms are connected by 2 O atoms
								count2 += 1
								r2.append((sio[i][0], sio[j][0]))
								r2_1.append([sio[i][0], sio[j][0]])
#				print(r2)
#print("2MR count: ", count2)
#print(r2)
#print(set(sisi[0]))
#__________________________________________________________________________________________________
				r = []  # list of connections of all possible, primitive rings
				count3 = 0
				count4 = 0                 #Imagine 4 sets i,j,k,l
				count5 = 0
				count6 = 0
				count7 = 0
				count8 = 0
#
#____________________________________________________________________________________________
#ALL POTENTIAL RINGS
				r3 =[]
				r3_2 = []	
				r4 = [] #all 4 point circles
				r4_1 = [] #reduced from duplicates from r4
				r4_2 = [] #reduced from 3MR, this is the list of 4 primitive membered rings, no duplicate
				r5 = []
				r5_1 = [] #reduced duplicates ( due to different paths) from r5
				r5_2 = [] #reduced from all 3MR
				r5_3 = [] # reduced from all 4MR, this should be the list of primitive 5MR
				r6 = []
				r6_1 = [] #reduced duplicates from r6
				r6_2 = [] #reduced from 3MR
				r6_3 = [] #reduced from 4MR
				r6_4 = [] #reduced from 5M
				r7 = []
				r7_1 = []
				r7_2 = []
				r7_3 = []
				r7_4 = []
				r7_5 = []
				r7_6 = []
				for i in range(len(sisi)):
					for j in range(len(sisi)):
						if set(sisi[i]) & set(sisi[j]) and set(sisi[j]) != set(sisi[i]):
							m1 = set(sisi[i]) & set(sisi[j])      # i& j = m1, remainder rj (j), ri (i)
							rj = set(sisi[j]) - m1
							ri = set(sisi[i]) - m1
							for k in range(len(sisi)):
								if set(sisi[j]) & set(sisi[k]) == rj and set(sisi[k]) != set(sisi[i]) and set(sisi[k]) != set(sisi[j])  :    #j&k = rj, remainder rk (k)
		
									rk = set(sisi[k]) - rj
									if ri == rk:  #coming back to the original atom, which is a full 3 membered ring
										r3.append([sisi[i], sisi[j], sisi[k]])

									for l in range( len(sisi)):	
										if set(sisi[k]) & set(sisi[l]) == rk and set(sisi[l]) != set(sisi[i]) and set(sisi[l]) != set(sisi[j]) and set(sisi[l]) != set(sisi[k]):
											rl = set(sisi[l]) - rk
											if ri == rl:
												r4.append([sisi[i], sisi[j], sisi[k], sisi[l]]) #potential 4MR

											for m in range(len(sisi)):
												if set(sisi[l]) & set(sisi[m]) == rl and set(sisi[m]) != set(sisi[i]) and set(sisi[m]) != set(sisi[j]) and set(sisi[m]) != set(sisi[k]) and set(sisi[m]) != set(sisi[l]) :
													rm = set(sisi[m]) - rl
													if rm == ri:
														r5.append([sisi[i],sisi[j],sisi[k],sisi[l],sisi[m]])

													for n in range(len(sisi)):
														if set(sisi[m]) & set(sisi[n]) == rm and set(sisi[n]) != set(sisi[i]) and set(sisi[n]) != set(sisi[j]) and set(sisi[n]) != set(sisi[k]) and set(sisi[n]) != set(sisi[l]) and set(sisi[n]) != set(sisi[m]):
															rn = set(sisi[n]) - rm
															if rn == ri:	
																r6.append([sisi[i],sisi[j],sisi[k],sisi[l],sisi[m],sisi[n]])

															for o in range(len(sisi)):	
																if set(sisi[n]) & set(sisi[o]) == rn and set(sisi[o]) != set(sisi[i]) and set(sisi[o]) != set(sisi[j]) and set(sisi[o]) != set(sisi[k]) and set(sisi[o]) != set(sisi[l]) and set(sisi[o]) != set(sisi[m]) and set(sisi[o]) != set(sisi[n]):
																	ro = set(sisi[o]) - rn
																	if ro == ri:
																		r7.append([sisi[i],sisi[j],sisi[k],sisi[l],sisi[m],sisi[n],sisi[o]])
#___________________________________________________________________________________________
#looking for primitive 3 MR
#print(len(r3))
#Now remove duplicate 
				r3_2 = []
				r3_3 = []
				r3_4 = []
				for i in range(len(r3)):
					for j in range(i+1, len(r3)):
						if sorted(r3[i]) == sorted(r3[j]):
							r3[j] = r3[i][:]
					if r3[i] not in r3_3:
						r3_3.append(r3[i])
				for i in r3_3:
					flat = list(itertools.chain(*i))
					set_flat = set(flat)
					lis = list(set_flat)
					a = []
					for j in lis:
						a.append(int(j))
					asc = sorted(a, key=int)
					asc_str = [str(k) for k in asc]					
					if asc_str not in o3:
						r3_2.append(i)
							
					
					


			#	for i in range(len(r3_4)):
			#		if r3_4[i] in o3:
			#			print(r3_4[i])
			#			r3_2.append(r3_4[i])
				#print(len(r3_2))
#r3_2 = list(set(r3))
#print(len(r3_2))

# Now determine if there's a 2 MR attached to those 3 MR
				for i in range(len(r3_2)):
					m = len(set(r3_2[i]) & set(r2))
					#print(m)
					count3 += 2**m
	#print(r3_2[i])
#	count_dbl = 0  # This counts no of 2 MR in EACH 3MR
#	for j in range(len(r3_2[i])):
#		if r3_2[i][j] in r2:
#			count_dbl += 1
	#print(count_dbl)
#	count3 += 2**count_dbl
#print("3MR count:", count3)

#____________________________________________________________________________________________
#4 MEMBER RING

#print("r 4", len(r4))
				for i in range(len(r4)):
					for j in range(i+1, len(r4)):
						if sorted(r4[i]) == sorted(r4[j]):
							r4[j] = r4[i][:]
					if r4[i] not in r4_1:
						r4_1.append(r4[i])
#print("r 4", len(r4))
#print("r 41", len(r4_1))
				for i in range(len(r4_1)):
#	for j in range(len(r3_2)):
					overlap43 = [len(set(r4_1[i]) & set(r3_2[j])) for j in range(len(r3_2))] #list of no of matched side of on 4MR with all the rest 3MR found above
#	print(intersect)
					if 2 not in overlap43 and 3 not in overlap43:
						r4_2.append(r4_1[i])
				#print(len(r4_2))

#					elif 2 in intersect:
				for i in range(len(r4_2)):
					m = len(set(r4_2[i]) & set(r2))
					#print(m)
					count4 += 2**m
#print("4MR count:", count4)

#________________________________________________________________________________________________________________________________________________________________
#5 MEMBER RING
#print("r 5",len(r5))

				for i in range(len(r5)):
					for j in range(i+1, len(r5)):
						if sorted(r5[i]) == sorted(r5[j]):
							r5[j] = r5[i][:]
					if r5[i] not in r5_1:
						r5_1.append(r5[i])
#print("r 51",len(r5_1))
#reduce from 3MR
				for i in range(len(r5_1)):
					overlap53 = [len(set(r5_1[i]) & set(r3_2[j])) for j in range(len(r3_2))]
					if 2 not in overlap53 and 3 not in overlap53:
						r5_2.append(r5_1[i])
#print("r 52", len(r5_2))

#reduce from 4MR
				for i in range(len(r5_2)):
					overlap54 = [len(set(r5_2[i]) & set(r4_2[j])) for j in range(len(r4_2))]
	#print(intersect54)
					if 3 not in overlap54 and 4 not in overlap54:
						r5_3.append(r5_2[i])
#print("r 53", len(r5_3))
#Now calculate number of 5 primitive MR
				for i in range(len(r5_3)):
					m = len(set(r5_3[i]) & set(r2))
					count5 += 2**m
#print("5MR count:", count5)
#_____________________________________________________________________________________________________________________________________________________________________
#6 MEMBER RING
#print("r6", len(r6))
#reduce duplicates (from different paths)
				for i in range(len(r6)):
					for j in range(i+1, len(r6)):
						if sorted(r6[i]) == sorted(r6[j]):
							r6[j] = r6[i][:]
					if r6[i] not in r6_1:
						r6_1.append(r6[i])
#print("r 61", len(r6_1))

#reduce from 3MR
				for i in range(len(r6_1)):
					overlap63 = [len(set(r6_1[i]) & set(r3_2[j])) for j in range(len(r3_2))]
					if 2 not in overlap63 and 3 not in overlap63:
						r6_2.append(r6_1[i])
#print("r 62: ", len(r6_2))
#reduce from 4MR
				for i in range(len(r6_2)):
					overlap64 = [len(set(r6_2[i]) & set(r4_2[j])) for j in range(len(r4_2))]
	#print(intersect64)sic-3.0.0-dev648-x86_64.tar.xz
					if 3 not in overlap64 and 4 not in overlap64:
						r6_3.append(r6_2[i])
#print("r 63: ", len(r6_3))
#reduce from 5MR
				for i in range(len(r6_3)):
					overlap65 = [len(set(r6_3[i]) & set(r5_3[j])) for j in range(len(r5_3))]
	#print(intersect65)
					if 3 not in overlap65 and 4 not in overlap65 and 5 not in overlap65:
						r6_4.append(r6_3[i])
#print("r 64: ", len(r6_4))
# count total 6MR
				#print(len(r6_4))
				for i in range(len(r6_4)):
					m = len(set(r6_4[i]) & set(r2))
					count6 += 2**m
#print("6MR count: ", count6)
#__________________________________________________________________________________________________________________________________________________________________________         
#7 MEMBER RING
#print("r7: ", len(r7))

#reduce duplicates (from different paths)
				for i in range(len(r7)):
					for j in range(i+1, len(r7)):
						if sorted(r7[i]) == sorted(r7[j]):
							r7[j] = r7[i][:]
					if r7[i] not in r7_1:
						r7_1.append(r7[i])
#print("r 71", len(r7_1))

#reduce from 3MR
				for i in range(len(r7_1)):
					overlap73 = [len(set(r7_1[i]) & set(r3_2[j])) for j in range(len(r3_2))]
					if 2 not in overlap73 and 3 not in overlap73:
						r7_2.append(r7_1[i])
#print("r 72: ", len(r7_2))
#reduce from 4MR
				for i in range(len(r7_2)):
					overlap74 = [len(set(r7_2[i]) & set(r4_2[j])) for j in range(len(r4_2))]
	#print(intersect64)
					if 3 not in overlap74 and 4 not in overlap74:
						r7_3.append(r7_2[i])
#print("r 73: ", len(r7_3))
#reduce from 5MR
				for i in range(len(r7_3)):
					overlap75 = [len(set(r7_3[i]) & set(r5_3[j])) for j in range(len(r5_3))]
	#print(intersect65)
					if 3 not in overlap75 and 4 not in overlap75 and 5 not in overlap75:
						r7_4.append(r7_3[i])
#print("r 74: ", len(r7_4))
#reduce from 6MR
				for i in range(len(r7_4)):
					overlap76 = [len(set(r7_4[i]) & set(r6_4[j])) for j in range(len(r6_4))]
	#print(intersect76)
					if 4 not in overlap76 and 5 not in overlap76 and 6 not in overlap76:
						r7_6.append(r7_4[i])
#print("r 75: ", len(r7_5))

# count total 7MR
				#print(len(r7_5))
				for i in r7_6:
					flat = list(itertools.chain(*i))
					set_flat = set(flat)
					lis = list(set_flat)
					for j in o3:
						if set(j).issubset(set(lis)) == False:
							if i not in r7_5:
								r7_5.append(i)
				for i in range(len(r7_5)):
					m = len(set(r7_5[i]) & set(r2))
					count7 += 2**m
#print("7MR count: ", count7)

#__________________________________________________________________________________________________________________________________________
#RING STATISTICS
				total_count = count2 + count3 + count4 + count5 + count6 + count7
				percent2 = 100*count2/total_count
				percent3 = 100*count3/total_count
				percent4 = 100*count4/total_count
				percent5 = 100*count5/total_count
				percent6 = 100*count6/total_count
				percent7 = 100*count7/total_count

#___________________________________________________________________________________________________________________________________________
#For total data analysis
				print(count2, count3, count4, count5, count6, count7, percent2, percent3, percent4, percent5, percent6, percent7, sep='\t')
#				np.savetxt("ringstats", count2, count3, count4, count5, count6, count7, percent2, percent3, percent4, percent5, percent6, percent7)
#				ff.write(count2 + count3 + count4 + count5 + count6 + count7 + percent2 + percent3 + percent4 + percent5 + percent6 + percent7 + '\n')
			#	print(len(r3_2), len(r4_1), len(r5_1), len(r6_1), len(r7_1), sep='\t')
				#print(r2)
				#with open('Ring2','w') as f:
					#if len(r2_1) == 1:
				for item in r2_1:
					flat = list(itertools.chain(*item))
					f2.write('\t'.join(map(str,item)) + '\n')
				f2.write('\n')
	
							

				#with open('Ring3','w') as f:
				for item in r3_2:
					flat = list(itertools.chain(*item))
					set_flat = set(flat)
					lis = list(set_flat)
					f3.write('\t'.join(map(str,lis)) + '\n')
				f3.write('\n')	
				#with open('Ring4','w') as f:
				for item in r4_2:
					flat = list(itertools.chain(*item))
					set_flat = set(flat)
					lis = list(set_flat)
					f4.write('\t'.join(map(str,lis)) + '\n')
				f4.write('\n')	

#				with open('Ring5','w') as f:
				for item in r5_3:
					flat = list(itertools.chain(*item))
					set_flat = set(flat)
					lis = list(set_flat)
					f5.write('\t'.join(map(str,lis))+ '\n')
				f5.write('\n')

				#with open('Ring6','w') as f:
				for item in r6_4:
					flat = list(itertools.chain(*item))
					set_flat = set(flat)
					lis = list(set_flat)
					f6.write('\t'.join(map(str,lis)) + '\n')
				f6.write('\n')	

				#with open('Ring7','w') as f:
				for item in r7_5:
					flat = list(itertools.chain(*item))
					set_flat = set(flat)
					lis = list(set_flat)
					f7.write('\t'.join(map(str,lis)) + '\n')
				f7.write('\n')	

#___________________________________________________________________________________________________________________________________________
#NOW LOOK FOR SIOSI & OSIO ANGLE



				siosi2_2 = [] # all angles of each ring - should have 5 angles (5 list of 3)
				for i in range(len(r2)):	
					#siosi2_3 = [] #one angle
					#for j in range(len(r2[i])):
					Si1 = r2_1[i][0] 
					Si2 = r2_1[i][1] 
				#	print(Si1,Si2)
					iSi1 = si.index(Si1)
					iSi2 = si.index(Si2) 
					O = list(set(sio[iSi1][1]) & set(sio[iSi2][1]))
					siosi = [[Si1,O[i],Si2] for i in range(len(O))] 
					#siosi2 = [Si1,O[1],Si2] 
					#	siosi2_3.append(siosi) # printO[0] to remove square bracket, this append all angles of EACH n MR
					siosi2_2.append(siosi)
				siosi2.append(siosi2_2)
					
				osio2_2 = [] # for each frame
				for i in range(len(siosi2_2)): #for each ring
					osio2_3 = []
					for j in range(len(siosi2_2[i])): #for each angle
						for k in range(j+1,len(siosi2_2[i])):	
							O1 = siosi2_2[i][j][1]
							O2 = siosi2_2[i][k][1]
							#if set(siosi2_2[i][j]) & set(siosi2_2[i][k]):
							m = list(set(siosi2_2[i][j]) & set(siosi2_2[i][k]))
							if float(O1) < float(O2):
								osio = [[O1,m[i],O2] for i in range(len(m))]
								#osio1 = [O1,m[0],O2]
								#osio2 = [O1,m[1],O2]
								for l in range(len(osio)):
									if osio[l] not in osio2_3:
										osio2_3.append(osio[l])
								#if osio2 not in osio2_3:
								#	osio2_3.append(osio2)
							else:
								osio = [[O2,m[i],O1] for i in range(len(m))]
								#osio1 = [O2,m[0],O1]
								#osio2 = [O2,m[1],O1]
								for l in range(len(osio)):
									if osio[l] not in osio2_3:
										osio2_3.append(osio[l])
								#if osio2 not in osio2_3:
								#	osio2_3.append(osio2)
					osio2_2.append(osio2_3)
				#print("osio2_2:",osio2_2)
				osio2.append(osio2_2)				
				#print("osio2", osio2)

#____________________________________________________________________________________________________________________________
				#print(r3_2)
				#print(np.shape(r3_2))

				siosi3_2 = [] # all angles of each ring - should have 5 angles (5 list of 3)
				for i in range(len(r3_2)):	
					siosi3_3 = [] #one angle
					for j in range(len(r3_2[i])):
						Si1 = r3_2[i][j][0] 
						Si2 = r3_2[i][j][1] 
						#print(Si1,Si2)
						iSi1 = si.index(Si1)
						iSi2 = si.index(Si2) 
						O = list(set(sio[iSi1][1]) & set(sio[iSi2][1]))
						#print(O)
						#if len(O) == 1:
	
						siosi = [[Si1,O[i],Si2] for i in range(len(O))]
						[siosi3_3.append(siosi[i]) for i in range(len(siosi))]
						#siosi = [Si1,O[0],Si2] 
						#siosi3_3.append(siosi)
						#print(O)
						#	siosi = [Si1,O[0],Si2]
						#	siosi3_3.append(siosi)
						#elif len(O) == 2:
						#	siosi1_3 = [Si1,O[0],Si2]
						##	siosi2_3 = [Si1,O[1],Si2]
						#	siosi3_3.append(siosi1_3) # printO[0] to remove square bracket, this append all angles of EACH n MR
						#	siosi3_3.append(siosi2_3)	
					siosi3_2.append(siosi3_3)
				
#				print(siosi5_2)
				siosi3.append(siosi3_2)
				#print(siosi3)
				#print(np.shape(siosi3))
					
				osio3_2 = [] # for each frame
				for i in range(len(siosi3_2)): #for each ring
					osio3_3 = []
					for j in range(len(siosi3_2[i])): #for each angle
						for k in range(j+1,len(siosi3_2[i])):
							if set(siosi3_2[i][j]) & set(siosi3_2[i][k]):
								m = list(set(siosi3_2[i][j]) & set(siosi3_2[i][k]))
								if float(siosi3_2[i][j][1]) < float(siosi3_2[i][k][1]):
									osio = [siosi3_2[i][j][1],m[0],siosi3_2[i][k][1]]
									if osio not in osio3_3:
										osio3_3.append(osio)
								else:
									osio = [siosi3_2[i][k][1],m[0],siosi3_2[i][j][1]]
									if osio not in osio3_3:
										osio3_3.append(osio)
					osio3_2.append(osio3_3)
#				print(osio5_2)
				osio3.append(osio3_2)				
				#print(osio3)
				#print(np.shape(osio3))
#____________________________________________________________________________________________________________________________

				siosi4_2 = [] # all angles of each ring - should have 5 angles (5 list of 3)
				for i in range(len(r4_2)):	
					siosi4_3 = [] #one angle
					for j in range(len(r4_2[i])):
						Si1 = r4_2[i][j][0] 
						Si2 = r4_2[i][j][1] 
				#	print(Si1,Si2)
						iSi1 = si.index(Si1)
						iSi2 = si.index(Si2) 
						O = list(set(sio[iSi1][1]) & set(sio[iSi2][1]))
						#if len[O] == 1:
						siosi = [[Si1,O[i],Si2] for i in range(len(O))]
						[siosi4_3.append(siosi[i]) for i in range(len(siosi))]
						#elif len[O] != 1:
						#siosi4_3.append(siosi) # printO[0] to remove square bracket, this append all angles of EACH n MR
					siosi4_2.append(siosi4_3)

#				print(siosi5_2)
				siosi4.append(siosi4_2)
					
				osio4_2 = [] # for each frame
				for i in range(len(siosi4_2)): #for each ring
					osio4_3 = []
					for j in range(len(siosi4_2[i])): #for each angle
						for k in range(j+1,len(siosi4_2[i])):
							if set(siosi4_2[i][j]) & set(siosi4_2[i][k]):
								m = list(set(siosi4_2[i][j]) & set(siosi4_2[i][k]))
								if float(siosi4_2[i][j][1]) < float(siosi4_2[i][k][1]):
									osio = [siosi4_2[i][j][1],m[0],siosi4_2[i][k][1]]
									if osio not in osio4_3:
										osio4_3.append(osio)
								else:
									osio = [siosi4_2[i][k][1],m[0],siosi4_2[i][j][1]]
									if osio not in osio4_3:
										osio4_3.append(osio)
					osio4_2.append(osio4_3)
#				print(osio5_2)
				osio4.append(osio4_2)				

				siosi5_2 = [] # all angles of each ring - should have 5 angles (5 list of 3)
				for i in range(len(r5_3)):	
					siosi5_3 = [] #one angle
					for j in range(len(r5_3[i])):
						Si1 = r5_3[i][j][0] 
						Si2 = r5_3[i][j][1] 
				#	print(Si1,Si2)
						iSi1 = si.index(Si1)
						iSi2 = si.index(Si2) 
						O = list(set(sio[iSi1][1]) & set(sio[iSi2][1]))
						siosi = [[Si1,O[i],Si2] for i in range(len(O))]
						[siosi5_3.append(siosi[i]) for i in range(len(siosi))]
						#siosi5_3.append(siosi) # printO[0] to remove square bracket, this append all angles of EACH n MR
					siosi5_2.append(siosi5_3)

#			print(siosi5_2)
				siosi5.append(siosi5_2)
					
				osio5_2 = [] # for each frame
				for i in range(len(siosi5_2)): #for each ring
					osio5_3 = []
					for j in range(len(siosi5_2[i])): #for each angle
						for k in range(j+1,len(siosi5_2[i])):
							if set(siosi5_2[i][j]) & set(siosi5_2[i][k]):
								m = list(set(siosi5_2[i][j]) & set(siosi5_2[i][k]))
								if float(siosi5_2[i][j][1]) < float(siosi5_2[i][k][1]):
									osio = [siosi5_2[i][j][1],m[0],siosi5_2[i][k][1]]
									if osio not in osio5_3:
										osio5_3.append(osio)
								else:
									osio = [siosi5_2[i][k][1],m[0],siosi5_2[i][j][1]]
									if osio not in osio5_3:
										osio5_3.append(osio)
					osio5_2.append(osio5_3)
#				int(osio5_2)
				osio5.append(osio5_2)				

#____________________________________________________________________________________________________________________________

				siosi6_2 = [] # all angles of each ring - should have 5 angles (5 list of 3)
				for i in range(len(r6_4)):	
					siosi6_3 = [] #one angle
					for j in range(len(r6_4[i])):
						Si1 = r6_4[i][j][0] 
						Si2 = r6_4[i][j][1] 
				#	print(Si1,Si2)
						iSi1 = si.index(Si1)
						iSi2 = si.index(Si2) 
						O = list(set(sio[iSi1][1]) & set(sio[iSi2][1]))
						siosi = [[Si1,O[i],Si2] for i in range(len(O))]
						[siosi6_3.append(siosi[i]) for i in range(len(siosi))]
						#siosi6_3.append(siosi) # printO[0] to remove square bracket, this append all angles of EACH n MR
					siosi6_2.append(siosi6_3)

#				print(siosi5_2)
				siosi6.append(siosi6_2)
					
				osio6_2 = [] # for each frame
				for i in range(len(siosi6_2)): #for each ring
					osio6_3 = []
					for j in range(len(siosi6_2[i])): #for each angle
						for k in range(j+1,len(siosi6_2[i])):
							if set(siosi6_2[i][j]) & set(siosi6_2[i][k]):
								m = list(set(siosi6_2[i][j]) & set(siosi6_2[i][k]))
								if float(siosi6_2[i][j][1]) < float(siosi6_2[i][k][1]):
									osio = [siosi6_2[i][j][1],m[0],siosi6_2[i][k][1]]
									if osio not in osio6_3:
										osio6_3.append(osio)
								else:
									osio = [siosi6_2[i][k][1],m[0],siosi6_2[i][j][1]]
									if osio not in osio6_3:
										osio6_3.append(osio)
					osio6_2.append(osio6_3)
#				print(osio5_2)
				osio6.append(osio6_2)				


#____________________________________________________________________________________________________________________________

				siosi7_2 = [] # all angles of each ring - should have 5 angles (5 list of 3)
				for i in range(len(r7_5)):	
					siosi7_3 = [] #one angle
					for j in range(len(r7_5[i])):
						Si1 = r7_5[i][j][0] 
						Si2 = r7_5[i][j][1] 
				#	print(Si1,Si2)
						iSi1 = si.index(Si1)
						iSi2 = si.index(Si2) 
						O = list(set(sio[iSi1][1]) & set(sio[iSi2][1]))
						siosi = [[Si1,O[i],Si2] for i in range(len(O))]
						[siosi7_3.append(siosi[i]) for i in range(len(siosi))]
						#siosi7_3.append(siosi) # printO[0] to remove square bracket, this append all angles of EACH n MR
					siosi7_2.append(siosi7_3)

#			print(siosi5_2)
				siosi7.append(siosi7_2)
			#	print(siosi7)
					
				osio7_2 = [] # for each frame
				for i in range(len(siosi7_2)): #for each ring
					osio7_3 = []
					for j in range(len(siosi7_2[i])): #for each angle
						for k in range(j+1,len(siosi7_2[i])):
							if set(siosi7_2[i][j]) & set(siosi7_2[i][k]):
								m = list(set(siosi7_2[i][j]) & set(siosi7_2[i][k]))
								if float(siosi7_2[i][j][1]) < float(siosi7_2[i][k][1]):
									osio = [siosi7_2[i][j][1],m[0],siosi7_2[i][k][1]]
									if osio not in osio7_3:
										osio7_3.append(osio)
								else:
									osio = [siosi7_2[i][k][1],m[0],siosi7_2[i][j][1]]
									if osio not in osio7_3:
										osio7_3.append(osio)
					osio7_2.append(osio7_3)
#				int(osio5_2)
				osio7.append(osio7_2)				
			#	print(osio7)

				count2 = 0
				count3 = 0
				count4 = 0
				count5 = 0
				count6 = 0
				count7 = 0
				percent2 = 0
				percent3 = 0
				percent4 = 0
				percent5 = 0
				percent6 = 0
				percent7 = 0
				r2.clear()
				r3.clear()
				r3_2.clear()
				r4.clear()
				r4_1.clear()
				r4_2.clear()
				r5.clear()
				r5_1.clear()
				r5_2.clear()
				r5_3.clear()
				r6.clear()
				r6_1.clear()
				r6_2.clear()
				r6_3.clear()
				r6_4.clear()
				r7.clear()
				r7_1.clear()
				r7_2.clear()
				r7_3.clear()
				r7_4.clear()
				r7_5.clear()
				r7_6.clear()
				sio.clear()
				sisi.clear()
				o3.clear()
				#siosi5_2.clear()
				#osio5_2.clear()
	return
ring()
#ring(datafile, frame_size)


#count = 0
def ringAngle():
	count = 0
	ID = []
	xyz = []
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
			count += 1
			part = line.split()
			if count == linex:
				lx = 2*float(part[1])
			elif count == liney:
				ly = 2*float(part[1])
			elif count == linez:
				lz = 2*float(part[1])

			if len(part) == 5:
				xyz.append([part[1], float(part[2]), float(part[3]), float(part[4])]) # ID, x, y, z ALL ATOMS
				ID.append(part[1])
			if count % frame_size_traj == 0:
				f_indx += 1
				i = int(count/585) - 1 #frame corresponging to list: frame 1, list ID 1 ....

#_______________________________________________________________________________________________________-_
				#for i in range(len(siosi2)):
				for j in range(len(siosi2[i])): # for each ring
					for k in range(len(siosi2[i][j])):
						Si1 = siosi2[i][j][k][0]
						O = siosi2[i][j][k][1]
						Si2 = siosi2[i][j][k][2]
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
				
						dot_product = dxSiO1*dxSiO2 + dySiO1*dySiO2 + dzSiO1*dzSiO2
						mag_product = dSiO1*dSiO2
						angle = math.degrees(math.acos(dot_product/mag_product))
						f22.write(str(angle)+'\n')

				for j in range(len(siosi3[i])): # for each ring
					for k in range(len(siosi3[i][j])):
						Si1 = siosi3[i][j][k][0]
						O = siosi3[i][j][k][1]
						Si2 = siosi3[i][j][k][2]
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
				
						dot_product = dxSiO1*dxSiO2 + dySiO1*dySiO2 + dzSiO1*dzSiO2
						mag_product = dSiO1*dSiO2
						angle = math.degrees(math.acos(dot_product/mag_product))
						f33.write(str(angle)+'\n')


				for j in range(len(siosi4[i])): # for each ring
					for k in range(len(siosi4[i][j])):
						Si1 = siosi4[i][j][k][0]
						O = siosi4[i][j][k][1]
						Si2 = siosi4[i][j][k][2]
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
			
						dot_product = dxSiO1*dxSiO2 + dySiO1*dySiO2 + dzSiO1*dzSiO2
						mag_product = dSiO1*dSiO2
						angle = math.degrees(math.acos(dot_product/mag_product))
					#siosi.append(angle)
						f44.write(str(angle)+'\n')




				for j in range(len(siosi5[i])): # for each ring
					for k in range(len(siosi5[i][j])):
						Si1 = siosi5[i][j][k][0]
						O = siosi5[i][j][k][1]
						Si2 = siosi5[i][j][k][2]
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
				
						dot_product = dxSiO1*dxSiO2 + dySiO1*dySiO2 + dzSiO1*dzSiO2
						mag_product = dSiO1*dSiO2
						angle = math.degrees(math.acos(dot_product/mag_product))
						f55.write(str(angle)+'\n')

				#for i in range(len(siosi6)):
				for j in range(len(siosi6[i])): # for each ring
					for k in range(len(siosi6[i][j])):
						Si1 = siosi6[i][j][k][0]
						O = siosi6[i][j][k][1]
						Si2 = siosi6[i][j][k][2]
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
			
						dot_product = dxSiO1*dxSiO2 + dySiO1*dySiO2 + dzSiO1*dzSiO2
						mag_product = dSiO1*dSiO2
						angle = math.degrees(math.acos(dot_product/mag_product))
						f66.write(str(angle)+'\n')
	
			#	for i in range(len(siosi7)):
				for j in range(len(siosi7[i])): # for each ring
					for k in range(len(siosi7[i][j])):
						Si1 = siosi7[i][j][k][0]
						O = siosi7[i][j][k][1]
						Si2 = siosi7[i][j][k][2]
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
			
						dot_product = dxSiO1*dxSiO2 + dySiO1*dySiO2 + dzSiO1*dzSiO2
						mag_product = dSiO1*dSiO2
						angle = math.degrees(math.acos(dot_product/mag_product))
						#siosi.append(angle)
						f77.write(str(angle)+'\n')

#________________________________________________________________________________________________________________________________
				#for i in range(len(osio2)):
					#print("osio2[i]",osio2[i])
				for j in range(len(osio2[i])):
					for k in range(len(osio2[i][j])):
						#print("osio2 i j k",osio2[i][j][k])
						O1 = osio2[i][j][k][0]
						#print("osio i j k 0", O1)
						Si = osio2[i][j][k][1]
						O2 = osio2[i][j][k][2]
						iO1 = ID.index(O1)
						iSi = ID.index(Si)
						iO2 = ID.index(O2)
							
						dx1 = xyz[iO1][1] - xyz[iSi][1]
						dy1 = xyz[iO1][2] - xyz[iSi][2]
						dz1 = xyz[iO1][3] - xyz[iSi][3]
						xx1 = np.round(dx1/lx, decimals = 0)
						yy1 = np.round(dy1/ly, decimals = 0)
						zz1 = np.round(dz1/lz, decimals = 0)
						dxOSi1 = dx1 - (lx*xx1)
						dyOSi1 = dy1 - (ly*yy1)
						if typ == "bulk":
							dzOSi1 = dz1 - (lz*zz1)
						else:
							dzOSi1 = dz1
						
						dOSi1 = math.sqrt(dxOSi1**2 + dyOSi1**2 + dzOSi1**2)

	
						dx2 = xyz[iO2][1] - xyz[iSi][1]
						dy2 = xyz[iO2][2] - xyz[iSi][2]
						dz2 = xyz[iO2][3] - xyz[iSi][3]
						xx2 = np.round(dx2/lx, decimals = 0)
						yy2 = np.round(dy2/ly, decimals = 0)
						zz2 = np.round(dz2/lz, decimals = 0)
						dxOSi2 = dx2 - (lx*xx2)
						dyOSi2 = dy2 - (ly*yy2)
						if typ == "bulk":
							dzOSi2 = dz2 - (lz*zz2)
						else:
							dzOSi2 = dz2
						
						dOSi2 = math.sqrt(dxOSi2**2 + dyOSi2**2 + dzOSi2**2)
						dot_product = dxOSi1*dxOSi2 + dyOSi1*dyOSi2 + dzOSi1*dzOSi2
						mag_product = dOSi1*dOSi2
						angle = math.degrees(math.acos(dot_product/mag_product))
						f222.write(str(angle)+'\n')

#				for i in range(len(osio3)):
				for j in range(len(osio3[i])):
					for k in range(len(osio3[i][j])):
						O1 = osio3[i][j][k][0]
						Si = osio3[i][j][k][1]
						O2 = osio3[i][j][k][2]
						iO1 = ID.index(O1)
						iSi = ID.index(Si)
						iO2 = ID.index(O2)
						
						dx1 = xyz[iO1][1] - xyz[iSi][1]
						dy1 = xyz[iO1][2] - xyz[iSi][2]
						dz1 = xyz[iO1][3] - xyz[iSi][3]
						xx1 = np.round(dx1/lx, decimals = 0)
						yy1 = np.round(dy1/ly, decimals = 0)
						zz1 = np.round(dz1/lz, decimals = 0)
						dxOSi1 = dx1 - (lx*xx1)
						dyOSi1 = dy1 - (ly*yy1)
						if typ == "bulk":
							dzOSi1 = dz1 - (lz*zz1)
						else:
							dzOSi1 = dz1
						
						dOSi1 = math.sqrt(dxOSi1**2 + dyOSi1**2 + dzOSi1**2)
	
						dx2 = xyz[iO2][1] - xyz[iSi][1]
						dy2 = xyz[iO2][2] - xyz[iSi][2]
						dz2 = xyz[iO2][3] - xyz[iSi][3]
						xx2 = np.round(dx2/lx, decimals = 0)
						yy2 = np.round(dy2/ly, decimals = 0)
						zz2 = np.round(dz2/lz, decimals = 0)
						dxOSi2 = dx2 - (lx*xx2)
						dyOSi2 = dy2 - (ly*yy2)
						if typ == "bulk":
							dzOSi2 = dz2 - (lz*zz2)
						else:
							dzOSi2 = dz2
						
						dOSi2 = math.sqrt(dxOSi2**2 + dyOSi2**2 + dzOSi2**2)
						dot_product = dxOSi1*dxOSi2 + dyOSi1*dyOSi2 + dzOSi1*dzOSi2
						mag_product = dOSi1*dOSi2
						#print(mag_product)

						div = np.round(dot_product/mag_product, decimals = 7)
						#print(div, O1,Si,O2, sep = '\t')
						#if div == 'nan':
						#	print(dOSi1, dxOSi1, dyOSi1,dzOSi1, O1, Si, osio3[i][j][k])
						#	print(dOSi2, dxOSi2, dyOSi2, dzOSi2, O2)
						#print(div)
						angle = math.degrees(math.acos(div))	
						#print(angle, O1,Si,O2, sep = '\t')
						f333.write(str(angle)+'\n')

				#for i in range(len(osio4)):
				for j in range(len(osio4[i])):
					for k in range(len(osio4[i][j])):
						O1 = osio4[i][j][k][0]
						Si = osio4[i][j][k][1]
						O2 = osio4[i][j][k][2]
						iO1 = ID.index(O1)
						iSi = ID.index(Si)
						iO2 = ID.index(O2)
						
						dx1 = xyz[iO1][1] - xyz[iSi][1]
						dy1 = xyz[iO1][2] - xyz[iSi][2]
						dz1 = xyz[iO1][3] - xyz[iSi][3]
						xx1 = np.round(dx1/lx, decimals = 0)
						yy1 = np.round(dy1/ly, decimals = 0)
						zz1 = np.round(dz1/lz, decimals = 0)
						dxOSi1 = dx1 - (lx*xx1)
						dyOSi1 = dy1 - (ly*yy1)
						if typ == "bulk":
							dzOSi1 = dz1 - (lz*zz1)
						else:
							dzOSi1 = dz1
							
						dOSi1 = math.sqrt(dxOSi1**2 + dyOSi1**2 + dzOSi1**2)

	
						dx2 = xyz[iO2][1] - xyz[iSi][1]
						dy2 = xyz[iO2][2] - xyz[iSi][2]
						dz2 = xyz[iO2][3] - xyz[iSi][3]
						xx2 = np.round(dx2/lx, decimals = 0)
						yy2 = np.round(dy2/ly, decimals = 0)
						zz2 = np.round(dz2/lz, decimals = 0)
						dxOSi2 = dx2 - (lx*xx2)
						dyOSi2 = dy2 - (ly*yy2)
						if typ == "bulk":
							dzOSi2 = dz2 - (lz*zz2)
						else:
							dzOSi2 = dz2
						
						dOSi2 = math.sqrt(dxOSi2**2 + dyOSi2**2 + dzOSi2**2)
						dot_product = dxOSi1*dxOSi2 + dyOSi1*dyOSi2 + dzOSi1*dzOSi2
						mag_product = dOSi1*dOSi2
						angle = math.degrees(math.acos(dot_product/mag_product))
						f444.write(str(angle)+'\n')

				#for i in range(len(osio5)):
				for j in range(len(osio5[i])):
					for k in range(len(osio5[i][j])):
						O1 = osio5[i][j][k][0]
						Si = osio5[i][j][k][1]
						O2 = osio5[i][j][k][2]
						iO1 = ID.index(O1)
						iSi = ID.index(Si)
						iO2 = ID.index(O2)
						
						dx1 = xyz[iO1][1] - xyz[iSi][1]
						dy1 = xyz[iO1][2] - xyz[iSi][2]
						dz1 = xyz[iO1][3] - xyz[iSi][3]
						xx1 = np.round(dx1/lx, decimals = 0)
						yy1 = np.round(dy1/ly, decimals = 0)
						zz1 = np.round(dz1/lz, decimals = 0)
						dxOSi1 = dx1 - (lx*xx1)
						dyOSi1 = dy1 - (ly*yy1)
						if typ == "bulk":
							dzOSi1 = dz1 - (lz*zz1)
						else:
							dzOSi1 = dz1
							
						dOSi1 = math.sqrt(dxOSi1**2 + dyOSi1**2 + dzOSi1**2)
	
						dx2 = xyz[iO2][1] - xyz[iSi][1]
						dy2 = xyz[iO2][2] - xyz[iSi][2]
						dz2 = xyz[iO2][3] - xyz[iSi][3]
						xx2 = np.round(dx2/lx, decimals = 0)
						yy2 = np.round(dy2/ly, decimals = 0)
						zz2 = np.round(dz2/lz, decimals = 0)
						dxOSi2 = dx2 - (lx*xx2)
						dyOSi2 = dy2 - (ly*yy2)
						if typ == "bulk":
							dzOSi2 = dz2 - (lz*zz2)
						else:
							dzOSi2 = dz2
						
						dOSi2 = math.sqrt(dxOSi2**2 + dyOSi2**2 + dzOSi2**2)
						dot_product = dxOSi1*dxOSi2 + dyOSi1*dyOSi2 + dzOSi1*dzOSi2
						mag_product = dOSi1*dOSi2
						angle = math.degrees(math.acos(dot_product/mag_product))
						f555.write(str(angle)+'\n')

				#for i in range(len(osio6)):
				for j in range(len(osio6[i])):
					for k in range(len(osio6[i][j])):
						O1 = osio6[i][j][k][0]
						Si = osio6[i][j][k][1]
						O2 = osio6[i][j][k][2]
						iO1 = ID.index(O1)
						iSi = ID.index(Si)
						iO2 = ID.index(O2)
						
						dx1 = xyz[iO1][1] - xyz[iSi][1]
						dy1 = xyz[iO1][2] - xyz[iSi][2]
						dz1 = xyz[iO1][3] - xyz[iSi][3]
						xx1 = np.round(dx1/lx, decimals = 0)
						yy1 = np.round(dy1/ly, decimals = 0)
						zz1 = np.round(dz1/lz, decimals = 0)
						dxOSi1 = dx1 - (lx*xx1)
						dyOSi1 = dy1 - (ly*yy1)
						if typ == "bulk":
							dzOSi1 = dz1 - (lz*zz1)
						else:
							dzOSi1 = dz1
							
						dOSi1 = math.sqrt(dxOSi1**2 + dyOSi1**2 + dzOSi1**2)

	
						dx2 = xyz[iO2][1] - xyz[iSi][1]
						dy2 = xyz[iO2][2] - xyz[iSi][2]
						dz2 = xyz[iO2][3] - xyz[iSi][3]
						xx2 = np.round(dx2/lx, decimals = 0)
						yy2 = np.round(dy2/ly, decimals = 0)
						zz2 = np.round(dz2/lz, decimals = 0)
						dxOSi2 = dx2 - (lx*xx2)
						dyOSi2 = dy2 - (ly*yy2)
						if typ == "bulk":
							dzOSi2 = dz2 - (lz*zz2)
						else:
							dzOSi2 = dz2
						
						dOSi2 = math.sqrt(dxOSi2**2 + dyOSi2**2 + dzOSi2**2)
						dot_product = dxOSi1*dxOSi2 + dyOSi1*dyOSi2 + dzOSi1*dzOSi2
						mag_product = dOSi1*dOSi2
						angle = math.degrees(math.acos(dot_product/mag_product))
						f666.write(str(angle)+'\n')

#				for i in range(len(osio7)):
				for j in range(len(osio7[i])):
					for k in range(len(osio7[i][j])):
						O1 = osio7[i][j][k][0]
						Si = osio7[i][j][k][1]
						O2 = osio7[i][j][k][2]
						iO1 = ID.index(O1)
						iSi = ID.index(Si)
						iO2 = ID.index(O2)
							
						dx1 = xyz[iO1][1] - xyz[iSi][1]
						dy1 = xyz[iO1][2] - xyz[iSi][2]
						dz1 = xyz[iO1][3] - xyz[iSi][3]
						xx1 = np.round(dx1/lx, decimals = 0)
						yy1 = np.round(dy1/ly, decimals = 0)
						zz1 = np.round(dz1/lz, decimals = 0)
						dxOSi1 = dx1 - (lx*xx1)
						dyOSi1 = dy1 - (ly*yy1)
						if typ == "bulk":
							dzOSi1 = dz1 - (lz*zz1)
						else:
							dzOSi1 = dz1
							
						dOSi1 = math.sqrt(dxOSi1**2 + dyOSi1**2 + dzOSi1**2)
	
						dx2 = xyz[iO2][1] - xyz[iSi][1]
						dy2 = xyz[iO2][2] - xyz[iSi][2]
						dz2 = xyz[iO2][3] - xyz[iSi][3]
						xx2 = np.round(dx2/lx, decimals = 0)
						yy2 = np.round(dy2/ly, decimals = 0)
						zz2 = np.round(dz2/lz, decimals = 0)
						dxOSi2 = dx2 - (lx*xx2)
						dyOSi2 = dy2 - (ly*yy2)
						if typ == "bulk":
							dzOSi2 = dz2 - (lz*zz2)
						else:
							dzOSi2 = dz2
						
						dOSi2 = math.sqrt(dxOSi2**2 + dyOSi2**2 + dzOSi2**2)
						dot_product = dxOSi1*dxOSi2 + dyOSi1*dyOSi2 + dzOSi1*dzOSi2
						mag_product = dOSi1*dOSi2
						div = np.round(dot_product/mag_product, decimals = 7)
						#print(dot_product, mag_product,div)
						#if mag_product == 0:
							#print(dot_product, mag_product,O1,O2,Si)
						angle = math.degrees(math.acos(dot_product/mag_product))
						f777.write(str(angle)+'\n')
	return

ringAngle()

#print(siosi5)
#print(osio5)
#print(np.shape(siosi5),np.shape(osio5))
#data = ring("bond_tail0",38)
