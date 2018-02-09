year = int(input("insert airbitrary year : "))

if ((year % 400 == 0) or (year % 4 == 0)) and (not year % 100 == 0):
	print("yoon!")
else:
	print("not yoon!")
