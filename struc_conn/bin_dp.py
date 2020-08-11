file = "final_dp"
parsing = False
with open(file) as f:
	count = 0
	start = 0
	end = 0
	#parsing = False
	for line in f:
		count += 1
		parts = line.split()
		if float(parts[1]) == -39.5:
			start = count
			end = count + 80
			#print(start, end)
		if count == start:
			#print(count)
			parsing = True
		if count == end:
			parsing = False	
		if parsing:
			print(parts[1], parts[3])
