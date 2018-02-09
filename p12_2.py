fpIn	= open("DataIn.txt", "r")
fpOut	= open("Out.txt","w")


fpOut.write("The square results are\n")

for s in fpIn:
	num = list( int(x) for x in s.split() )

	for i in range(len(num)):
		sq = num[i] * num[i]
		fpOut.write("%5d" %sq)
		
	fpOut.write("\n")

fpIn.close()
fpOut.close()
