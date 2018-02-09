bornYear = int(input("insert your born year :"))

age = 2017 - bornYear + 1
status = "student"

if (age > 26):
	s_type = "not"	
if (age >= 20):
	s_type = "univ"	
elif (age >= 17):
	s_type = "high"	
elif (age >= 14):
	s_type = "middle"	
elif (age >= 8 ):
	s_type = "element"	
else:
	s_type = "not"

print("{} {}".format(s_type, status) )

