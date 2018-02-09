fp = open("in_data.txt", "r")

for s in fp:
	print( s, end="")

fp.close()



fp = open("in_data.txt", "r")
s = fp.readlines()
print(s)
fp.close()

fR = open("in_data.txt", "r")
fW = open("out_data.txt", "w")

s = fR.read()
fW.write(s)

fR.close();
fW.close();



fR = open("in_data.txt", "r")
fW = open("out_data.txt", "w")

for s in fR:
	print(s)
	fW.write(s)	# print(s, end="", file = fW)

fR.close()
fW.close()

