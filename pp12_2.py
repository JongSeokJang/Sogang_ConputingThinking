fpIn = open("DataIn_01.txt", "r")
fpOut = open("Out_02.txt", "w")

fpOut.write("The square results are\n")

total = 0
length = 0
for s in fpIn:
	num = list( int(x) for x in s.split() )
	total += sum(num)
	length += len(num)
	for i in range(len(num)):
		sq = num[i] * num[i]
		fpOut.write("%3d" %sq)
	fpOut.write("\n")

avg = total/length
fpOut.write("-----------------\n The sum of input data is")
fpOut.write(str(total))
fpOut.write("-----------------\n The average of input data is")
fpOut.write(str(round(avg,3)))
fpOut.write("\n")

fpIn.close()
fpOut.close()
