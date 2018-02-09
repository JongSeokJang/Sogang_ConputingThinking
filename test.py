# 1. setJmpHM()

def setJmpHM(curM, jmpM) :
	
	M = curM + jmpM
	jmpH = M // 60
	futureM = M - jmpH*60
	return jmpH, futureM

# 2. setHour()
def setHour(curH,jmpH) :
	
	tmp = curH + jmpH
	if tmp > 23 :
		futureH = tmp - 24
	else:
		futureH= tmp

	return futureH

#---------------------------------------
fr = open("HW07_time_In.txt", "r")
fw = open("HW07_time_Out.txt", "w")

T = 0
for aLine in fr:
	curH, curM, jmpM = aLine.split()
	curH = int(curH); curM = int(curM); jmpM = int(jmpM)
	jmpH, futureM = setJmpHM(curM, jmpM)
	jmpH = int(jmpH); futureM= int(futureM)

	futureH = setHour(curH,jmpH) #함수 안의 값 호출은 반드시 함수명 동반
	futureH = int(futureH)

	
	T=T+1
	print("Test  %2d: Future time = %2d:%2d" %(T, futureH, futureM),file = fw)
