snum = [201701, 201702, 201703, 201704, 201705]
ksco = [49, 79, 60, 100, 80]
msco = [43, 59, 85, 30, 90]
esco = [49, 79, 48, 68, 100]

mid_score = [snum, ksco, msco, esco]
print(mid_score)
ii  = 0
for i in range(5): 
	temp_list = [ksco[i], msco[i], esco[i]]
	mid_sum = sum(temp_list)
	print("{} average : {:.2f}".format(snum[i], mid_sum/3))
	


print( len(mid_score) )
for i in range( len(mid_score)-1 ):
	for j in range (len(snum)):

		if mid_score[i+1][j] >= 90:
			grade = 'A'
		elif mid_score[i+1][j] >=80:
			grade = 'B'
		elif mid_score[i+1][j] >=70:
			grade = 'C'
		elif mid_score[i+1][j] >=60:
			grade = 'D'
		else:
			grade = 'F'

		print(grade, end=" ")
		
	print()

