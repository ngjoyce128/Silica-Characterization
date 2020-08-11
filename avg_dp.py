import numpy as np

chunk =  80
f = "z_dp_all"
chunk = 80

dp1 = np.genfromtxt(f, usecols = 1, unpack = True)
z = np.genfromtxt(f, usecols = 0, max_rows = 80, unpack = True)

dp = [dp1[i:i+chunk] for i in range(0,len(dp1),chunk)]
avg_dp = []
avg_dp = np.mean(dp, axis = 0)

for i in range(chunk):
	print(z[i], avg_dp[i], sep='\t')
