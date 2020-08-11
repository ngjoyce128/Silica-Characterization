import math
import numpy as np
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i1', '--input1' , required=True, type=str, help="angle/distance file")

args = parser.parse_args()
f1 = args.input1

block = 10
t = 2.262

l = np.genfromtxt(f1, usecols = 0, unpack = True)
l.tolist()

chunksize = len(l)//block
total = chunksize * block
rem = len(l) - total
l2 = []

for i in range(rem, len(l)):
	l2.append(l[i])

chunk = [l2[i:i+chunksize] for i in range(0,len(l2), chunksize)]

bA = []
for i in range(len(chunk)):
        bA.append(np.mean(chunk[i]))

s = np.std(bA)

print(np.mean(bA), t*s/math.sqrt(block), sep='\t')


