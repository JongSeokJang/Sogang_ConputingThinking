
while(1):
	instr = input("input:")
	if( instr == "STOP"):
		print("Bye")
		break
		
	
	outstr = ""
	for c in instr:
		if c.islower():
			outstr = outstr + c.upper()
		elif c.isupper():
			outstr = outstr + c.lower()
		else:
			outstr = outstr + c
	
	print(outstr)


