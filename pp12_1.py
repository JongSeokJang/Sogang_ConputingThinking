fp_r = open("DataIn_01.txt")
fp_w = open("Out_01.txt", "w")


print("The square results are" , file = fp_w)
temp_sum  = 0;
count = 0 ;
for s in fp_r:
	data = list ( int(x) for x in s.split() )

	for ind in range( len(data) ):
		print("{}". format(data[ind]*data[ind]), end=" ", file =fp_w)	
		temp_sum = temp_sum + data[ind]
		count = count + 1 
	print("", file=fp_w)

print("------------------------", file = fp_w)
print("The sum of input data is : {} ". format(temp_sum), file =fp_w)
print("------------------------", file = fp_w)
print("The average of in put data :{:.3f}". format(temp_sum/count), file = fp_w)
