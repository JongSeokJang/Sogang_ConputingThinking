a = 123.456789
print( "%d, %f " %(a, a) )

a = 3.14
a = str(a)
print( a, type(a) )

a = float(a)
a = int(a)
print( a, type(a) )

a = float(a)
print( a, type(a) )

a = input("이름: ")
b = input("학번: ")
c = input("나이: ")

string = "당신의 이름은 " + a +"이며, 학번은 " + b + "입니다."
print( string )
print( "a" * int(c) )

