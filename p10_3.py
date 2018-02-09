snum = ['201701', '201702', '201703', '201704', '201705']
name = ['kang', 'chio', 'seo', 'choi2', 'Lee']
kscore = [90, 90, 80, 90, 85]
escore = [80, 85, 80, 92, 85]
mscore = [85, 90, 80, 83, 90]
total = []
avg = []

for ii in range(len(snum)):
	temp_sum = kscore[ii] + escore[ii] + mscore[ii]
	total.append(temp_sum)
	avg.append(temp_sum/3)

for ii in range(len(snum)):
	print("num:{},name:{}, kor:{}, eng:{}, math:{}, total:{},avg:{:.2f} ".format(snum[ii],name[ii],kscore[ii], escore[ii], mscore[ii],total[ii], avg[ii]))

data = []
for ii in range(len(snum)):
	temp = []
	temp.append(snum[ii])
	temp.append(name[ii])
	temp.append(kscore[ii])
	temp.append(escore[ii])
	temp.append(mscore[ii])
	temp.append(total[ii])
	temp.append(avg[ii])
	data.append(temp)

data.sort(key=lambda e: e[6])
for ii in data:
	print(ii)
