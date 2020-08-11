import numpy as np
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=True, type=str, help="REAX connectivity file")
parser.add_argument('-m1', '--min', required=True, type=float, help="REAX connectivity file")
parser.add_argument('-m2', '--max', required=True, type=float, help="REAX connectivity file")

args = parser.parse_args()
datafile = args.input
m1 = args.min
m2 = args.max

l = []
l = np.genfromtxt(datafile, usecols = 0, unpack = True)
y,x = np.histogram(l, range = (m1,m2),bins=200, density = True)
x = x[:-1]
for i in range(len(x)):
	print(x[i], y[i])

