import math 
import numpy as np

file = "cn_all"

block = 1
t = 2.262

si3 = []
si4 = []
si5 = []
o1 = []
o2 = []
o3 = []

si3,si4,si5,o1,o2,o3 = np.genfromtxt(file, usecols = (0,1,2,3,4,5), unpack = True)

si32 = []
si42 = []
si52 = []
o12 = []
o22 = []
o32 = []

chunksize = len(o1)//block
total = chunksize * block
rem = len(o1) - total

for i in range(rem, len(o1)):
	si32.append(si3[i])
	si42.append(si4[i])
	si52.append(si5[i])
	o12.append(o1[i])
	o22.append(o2[i])
	o32.append(o3[i])

chunk_si3 = [si32[i:i+chunksize] for i in range(0,len(o1), chunksize)]
chunk_si4 = [si42[i:i+chunksize] for i in range(0,len(o1), chunksize)]
chunk_si5 = [si52[i:i+chunksize] for i in range(0,len(o1), chunksize)]
chunk_o1 = [o12[i:i+chunksize] for i in range(0,len(o1), chunksize)]
chunk_o2 = [o22[i:i+chunksize] for i in range(0,len(o1), chunksize)]
chunk_o3 = [o32[i:i+chunksize] for i in range(0,len(o1), chunksize)]


bA_si3 = []
bA_si4 = []
bA_si5 = []
bA_o1 = []
bA_o2 = []
bA_o3 = []

for i in range(len(chunk_si3)):
	bA_si3.append(np.mean(chunk_si3[i]))
	bA_si4.append(np.mean(chunk_si4[i]))
	bA_si5.append(np.mean(chunk_si5[i]))
	bA_o1.append(np.mean(chunk_o1[i]))
	bA_o2.append(np.mean(chunk_o2[i]))
	bA_o3.append(np.mean(chunk_o3[i]))

s_si3 = np.std(bA_si3)
s_si4 = np.std(bA_si4)
s_si5 = np.std(bA_si5)
s_o1 = np.std(bA_o1)
s_o2 = np.std(bA_o2)
s_o3 = np.std(bA_o3)

print("Si3", np.mean(bA_si3), t*s_si3/math.sqrt(block))
print("Si4", np.mean(bA_si4), t*s_si4/math.sqrt(block))
print("Si5", np.mean(bA_si5), t*s_si5/math.sqrt(block))
print("O1", np.mean(bA_o1), t*s_o1/math.sqrt(block))
print("O2", np.mean(bA_o2), t*s_o2/math.sqrt(block))
print("O3", np.mean(bA_o3), t*s_o3/math.sqrt(block))
