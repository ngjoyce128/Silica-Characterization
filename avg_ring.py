import math
import numpy as np

file = "ring_stats_all"

block = 1
t = 2.262

r2 = []
r3 = []
r4 = []
r5 = []
r6 = []
r7 = []

r2,r3,r4,r5,r6,r7 = np.genfromtxt(file, usecols = (6,7,8,9,10,11), unpack = True)
r22 = []
r32 = []
r42 = []
r52 = []
r62 = []
r72 = []

chunksize = len(r2)//block
total = chunksize * block
rem = len(r2) - total

for i in range(rem, len(r2)):
	r22.append(r2[i])
	r32.append(r3[i])
	r42.append(r4[i])
	r52.append(r5[i])
	r62.append(r6[i])
	r72.append(r7[i])
chunk_2 = [r22[i:i+chunksize] for i in range(0,len(r22), chunksize)]
chunk_3 = [r32[i:i+chunksize] for i in range(0,len(r22), chunksize)]
chunk_4 = [r42[i:i+chunksize] for i in range(0,len(r22), chunksize)]
chunk_5 = [r52[i:i+chunksize] for i in range(0,len(r22), chunksize)]
chunk_6 = [r62[i:i+chunksize] for i in range(0,len(r22), chunksize)]
chunk_7 = [r72[i:i+chunksize] for i in range(0,len(r22), chunksize)]

bA2 = [] #block Average
bA3 = []
bA4 = []
bA5 = []
bA6 = []
bA7 = []

for i in range(len(chunk_2)):	
	bA2.append(np.mean(chunk_2[i]))
	bA3.append(np.mean(chunk_3[i]))
	bA4.append(np.mean(chunk_4[i]))
	bA5.append(np.mean(chunk_5[i]))
	bA6.append(np.mean(chunk_6[i]))
	bA7.append(np.mean(chunk_7[i]))

s_2 = np.std(bA2)
s_3 = np.std(bA3)
s_4 = np.std(bA4)
s_5 = np.std(bA5)
s_6 = np.std(bA6)
s_7 = np.std(bA7)

print(2,np.mean(bA2), t*s_2/math.sqrt(block))
print(3,np.mean(bA3), t*s_3/math.sqrt(block))
print(4,np.mean(bA4), t*s_4/math.sqrt(block))
print(5,np.mean(bA5), t*s_5/math.sqrt(block))
print(6,np.mean(bA6), t*s_6/math.sqrt(block))
print(7,np.mean(bA7), t*s_7/math.sqrt(block))
