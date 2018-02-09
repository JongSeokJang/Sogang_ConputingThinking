
def char_freq(s):
    
    D={}
    for i in s:
        if i.isspace():
            continue
        i=i.lower()
        D[i]=D.get(i,0)+1
    return D

def caseChange(sf):
    st=''
    for c in sf:
        if c.islower():
            st=st+c.upper()
        elif c.isupper():
            st=st+c.lower()
        else:
            st=st+c
    return st

while True:
    s=input("Input:")
    chrCntD=char_freq(s)
    for k,v in chrCntD.items():
        if s == "STOP" or s == "stop":
            break
        print("(%s : %d)"%(k,v),end='')
    print()
    a=caseChange(s)
    if a == "STOP" or a == "stop":
        break
    print(a)
print("Bye")

        
