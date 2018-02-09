def cal_kor_avg(students):
    kor_total=0
    for i in students:
        kor_total+=students['kor']
    return kor_total/len(students)
def cal_eng_avg(students):
    kor_total=0
    for i in students:
        eng_total+=students['eng']
    return eng_total/len(students)
def cal_mat_avg(students):
    mat_total=0
    for i in students:
        mat_total+=students['mat']
    return mat_total/len(students)
def cal_total_avg(students):
    total=0
    for i in students:
        total+=students['total']
    return total/len(students)
def print_students(students):
    for i in range(len(students)):
        kor=students[i].get('kor')
        eng=students[i].get('eng')
        mat=students[i].get('mat')
        students[i]['total']=(kor+eng+mat)
        students[i]['avg']=((kor+eng+mat)/3)
        print('num: %s, name: %s, kor: %d, eng: %d, mat: %d, total: %d, avg: %.2f'
              %(students[i]['num'],students[i]['name'],students[i]['kor'],students[i]['eng'],students[i]['mat'],students[i]['total'],students[i]['avg']))
def print_avg(t,k,e,m):
    print('\n: %.2f'%(t/5))
    print(': %.2f'%(k/5))
    print(': %.2f'%(e/5))
    print(': %.2f'%(m/5))
#main
def main():
    students=[{"num":"1", "name":"a", "kor":90, "eng":80, "mat":85,"total":0,"avg":0.0},
            {"num":"2", "name":"b", "kor":90,"eng":85, "mat":90,"total":0,"avg":0.0},
            {"num":"3", "name":"c","kor":80, "eng":80, "mat":80,"total":0,"avg":0.0},
            {"num":"4", "name":"d", "kor":90, "eng":92, "mat":83,"total":0,"avg":0.0},
            {"num":"5", "name":"e", "kor":85, "eng":85, "mat":90,"total":0,"avg":0.0}]
    print_students(students)
    t=cal_total_avg(students)
    k=cal_kor_avg(students)
    e=cal_eng_avg(students)
    m=cal_mat_avg(students)
    print_avg(t,k,e,m)
if __name__=='__main__':
    main()
