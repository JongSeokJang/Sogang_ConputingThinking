students = [
{"num":"1", "name":"kang", "kor":90, "eng":80, "math":85, "total":0,"avg":0.0, "order":0},
{"num":"2", "name":"choi", "kor":90, "eng":85, "math":90, "total":0,"avg":0.0, "order":0},
{"num":"3", "name":"seo",  "kor":80, "eng":80, "math":80, "total":0,"avg":0.0, "order":0},
{"num":"4", "name":"choi2","kor":90, "eng":92, "math":83, "total":0,"avg":0.0, "order":0},
{"num":"5", "name":"lee",  "kor":85, "eng":85, "math":90, "total":0,"avg":0.0, "order":0}
]

for student in students:
	student["total"] = student["kor"] + student["eng"] + student["math"]
	student["avg"] = student["total"]/3

students.sort(reverse=True, key=lambda student: student["avg"])

order = 1
for student in students:
	student["order"] = order
	order = order+1
	print(student)

