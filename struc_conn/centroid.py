import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

f2 = "Ring2"
f3 = "Ring3"
f4 = "Ring4"
f5 = "Ring5"
f6 = "Ring6"
f7 = "Ring7"
#count = 0
ID = []
xyz = []
count = 0
ID2 = []
xyz2 = []
with open("/home/n686n273/work/Silica_ReaxFF/BulkCool/AM_4000K_1000Kps/1/bond_tail") as f:
	for line in f:
		part = line.split()
		if len(part) == 5:
			ID2.append(part[1])
			xyz2.append([float(part[1]), float(part[2]), float(part[3]), float(part[4])])
#print(np.shape(ID2))
#print(np.shape(xyz2))
ID = [ID2[i:i+576] for i in range(0, len(ID2), 576)]
xyz = [xyz2[i:i+576] for i in range(0, len(xyz2), 576)]




output = []



x2 = []
y2 = []
z2 = []
x22 = []
y22 = []
z22 = []
#iD = []
iD2 = []
def centroid2():
	iD = []
	with open("Ring2") as f:
		iD = []
		count = 0
		for line in f:
			#iD = []
			part = line.split()
			if len(part) == 2:
				#iD = []
				index = [ID[count].index(node) for node in part]
				xx = [xyz[count][i][1] for i in index]
				yy = [xyz[count][i][2] for i in index]
				zz = [xyz[count][i][3] for i in index]
				iD.append(part)
				#print(part)
				x2.append(np.mean(xx))
				y2.append(np.mean(yy))
				z2.append(np.mean(zz))
#			iD2.append(iD)
			if line == '\n':
				#print('blank')	
				#iD2.append(iD)
				#iD.clear()
				x22.append(x2)
				y22.append(y2)
				z22.append(z2)
				count += 1
				#iD.clear()
	return

centroid2()
#print(np.shape(x2))
#print(np.shape(x22))
#print(iD2)	
new_file = open("centroid2_z","w")
for i in z2:	
	new_file.write(str(i)+'\n')


"""
x3 = []
y3 = []
z3 = []
x33 = []
y33 = []
z33 = []
def centroid3():
	with open("Ring3") as f:
		count = 0
		for line in f:
			part = line.split()
			if len(part) == 3:
				index = [ID[count].index(node) for node in part]
				xx = [xyz[count][i][1] for i in index]
				yy = [xyz[count][i][2] for i in index]
				zz = [xyz[count][i][3] for i in index]

				x3.append(np.mean(xx))
				y3.append(np.mean(yy))
				z3.append(np.mean(zz))
			elif line == '\n':	
				
				x33.append(x3)
				y33.append(y3)
				z33.append(z3)
				count += 1
	return

centroid3()


x4 = []
y4 = []
z4 = []
x44 = []
y44 = []
z44 = []
def centroid4():
	with open("Ring4") as f:
		count = 0
		for line in f:
			part = line.split()
			if len(part) == 4:
				index = [ID[count].index(node) for node in part]
				xx = [xyz[count][i][1] for i in index]
				yy = [xyz[count][i][2] for i in index]
				zz = [xyz[count][i][3] for i in index]

				x4.append(np.mean(xx))
				y4.append(np.mean(yy))
				z4.append(np.mean(zz))
			elif line == '\n':	
				
				x44.append(x4)
				y44.append(y4)
				z44.append(z4)
				count += 1
	return

centroid4()


x5 = []
y5 = []
z5 = []
x55 = []
y55 = []
z55 = []
def centroid5():
	with open("Ring5") as f:
		count = 0
		for line in f:
			part = line.split()
			if len(part) == 5:
				index = [ID[count].index(node) for node in part]
				xx = [xyz[count][i][1] for i in index]
				yy = [xyz[count][i][2] for i in index]
				zz = [xyz[count][i][3] for i in index]

				x5.append(np.mean(xx))
				y5.append(np.mean(yy))
				z5.append(np.mean(zz))
			elif line == '\n':	
				
				x55.append(x5)
				y55.append(y5)
				z55.append(z5)
				count += 1
	return

centroid5()


x6 = []
y6 = []
z6 = []
x66 = []
y66 = []
z66 = []
def centroid6():
	with open("Ring6") as f:
		count = 0
		for line in f:
			part = line.split()
			if len(part) == 6:
				#print(part)
				index = [ID[count].index(node) for node in part]
				#print(index)
				xx = [xyz[count][i][1] for i in index]
				yy = [xyz[count][i][2] for i in index]
				zz = [xyz[count][i][3] for i in index]

				x6.append(np.mean(xx))
				y6.append(np.mean(yy))
				z6.append(np.mean(zz))
			elif line == '\n':	
				
				x66.append(x6)
				y66.append(y6)
				z66.append(z6)
				count += 1
	return

centroid6()

x7 = []
y7 = []
z7 = []
x77 = []
y77 = []
z77 = []
def centroid7():
	with open("Ring7") as f:
		count = 0
		for line in f:
			part = line.split()
			if len(part) == 7:
				index = [ID[count].index(node) for node in part]
				xx = [xyz[count][i][1] for i in index]
				yy = [xyz[count][i][2] for i in index]
				zz = [xyz[count][i][3] for i in index]

				x7.append(np.mean(xx))
				y7.append(np.mean(yy))
				z7.append(np.mean(zz))
			elif line == '\n':	
				
				x77.append(x7)
				y77.append(y7)
				z77.append(z7)
				count += 1
	return

centroid7()
#print(np.shape(x2))
#print(np.shape(x3))
#print(np.shape(x4))
#print(np.shape(x5))
#print(np.shape(x6))
#print(np.shape(x7))
#print(x22)
with open("ringcen.dat","w") as f:
	for i in range(len(x22)):
		for j in range(len(x22[i])):
			line = [2, str(x22[i][j]), str(y22[i][j]), str(z22[i][j])]
			f.write('\t'.join(map(str,line)) + '\n')
		f.write('\n')

	for i in range(len(x33)):
		for j in range(len(x33[i])):
		line = [3, str(x33[i]), str(y33[i]), str(z33[i])]
		f.write('\t'.join(map(str,line)) + '\n')
		f.write('\n')

	for i in range(len(x44)):
		for j in range(len(x44[i])):
		line = [4, str(x44[i][j]), str(y44[i]), str(z4[i])]
		f.write('\t'.join(map(str,line)) + '\n')
		f.write('\n')

	for i in range(len(x5)):
		line = [5, str(x5[i]), str(y5[i]), str(z5[i])]
		f.write('\t'.join(map(str,line)) + '\n')
		f.write('\n')

	for i in range(len(x6)):
		line = [6, str(x6[i]), str(y6[i]), str(z6[i])]
		f.write('\t'.join(map(str,line)) + '\n')
		f.write('\n')

	for i in range(len(x7)):
		line = [7, str(x7[i]), str(y7[i]), str(z7[i])]
		f.write('\t'.join(map(str,line)) + '\n')
		f.write('\n')




#___________________________________________________________________________________________________________________________
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax4 = fig.add_subplot(111, projection='3d')
norm = matplotlib.colors.Normalize(vmin = 2, vmax = 7)
ax.scatter(x2,y2,z2, color = 'r', s = 30)
#ax.scatter(x2,y2,z2, c = 2*np.ones_like(x2), norm = norm, cmap = 'Blues', s = 20)
ax.scatter(x3,y3,z3, c = 3*np.ones_like(x3), norm = norm, cmap = 'Blues', s = 30)
ax.scatter(x4,y4,z4, c = 4*np.ones_like(x4), norm = norm, cmap = 'Blues', s = 40)
ax.scatter(x5,y5,z5, c = 5*np.ones_like(x5), norm = norm, cmap = 'Blues', s = 50)
ax.scatter(x6,y6,z6, c = 6*np.ones_like(x6), norm = norm, cmap = 'Blues', s = 60)
ax.scatter(x7,y7,z7, c = 7*np.ones_like(x7), norm = norm, cmap = 'Blues', s = 70)
plt.xlabel("x")
plt.ylabel("y")
ax.set_zlabel("z")
plt.show()

"""
