s = (
{'num':'1', 'name':'kang', 'korean':90, 'english':80, 'math':85, 'total':0, 'avg':0.0},
{'num':'2', 'name':'choi', 'korean':90, 'english':80, 'math':85, 'total':0, 'avg':0.0},
{'num':'3', 'name':'seo', 'korean':90, 'english':80, 'math':85, 'total':0, 'avg':0.0},
{'num':'4', 'name':'choi2', 'korean':90, 'english':80, 'math':85, 'total':0, 'avg':0.0},
{'num':'5', 'name':'lee', 'korean':90, 'english':80, 'math':85, 'total':0, 'avg':0.0}
)
for i in students:
	for ele in i:
		print("{}:{}". format(ele, i[ele]) , end='')	
	print()

