def searchList(L, x):
	for index in range(len(L)):
		if L[index] == x:
			return index
	else:
		return -1 

fp_r = open("DataIn_02.txt")
fp_w = open("DataOut_02.txt", "w")

flag = 0
count = 0;
for s in fp_r:
	print(count, s)
	if flag == 0:	# odd

		k = int(s)
		flag = 1
	else:			# even
		L = list( int(x) for x in s.split()	)
		idx = searchList(L, k)
		if idx == -1:
			print("Key {} is not in {}".format(k,L), file=fp_w)
		else:
			print("Key {} is at {} in {}".format(k,idx,L), file=fp_w)
		flag = 0

	count = count+1
	

fp_r.close()
fp_w.close()	
