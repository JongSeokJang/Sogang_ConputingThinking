
def isUniversityStudent(age):
	return "University"



def isHighSchoolStudent(age):
	return "HighSchool"


def isMiddleSchoolStudent(age):
	return "MiddleSchool"


def isElementarySchoolStudent(age):
	return "Elementary"

def printStatus(status):
	print("hi {}.student".format(status))

def main():

	born_year = int(input("intert birth_year: "))
	age = 2017-born_year + 1
	flag = 0
	if 20 <= age <= 26:
		status = isUniversityStudent(age)
	elif 17 <= age < 20:
		status = isHighSchoolStudent(age)
	elif 14 <= age < 17:
		status = isMiddleSchoolStudent(age)
	elif 8 <= age < 14:
		status = isElementarySchoolStudent(age)
	elif age <= 8:
		after = 8 - age;		
		flag = 1
	else:
		exit()	

	if flag == 0:
		printStatus(status)
	else:
		print(" after {}".format(after))
		status = isElementarySchoolStudent(8)
		printStatus(status)
			
		
		

if __name__=="__main__":
	main()

