stu1 = ['kang',80,90,95]
stu2 = ['choi',90,80,88]

D = {201701:stu1, 201702:stu2}

for key in D:
	print(key, D[key])
	


for key in D:
	print(key, end=' ')
	for element in D[key]:
		print(element, end=' ')
	print()
		



for ii in range(-9, 10):
	print(ii)
