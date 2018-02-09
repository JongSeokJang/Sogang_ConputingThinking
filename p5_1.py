L = [5,6, "Hello", 7, "Python"];
print(len(L))
L[len(L)-1] = "World"

print(L)

print(L[-4])
for i in L:
	if type(i) == str:
		print(i)


L = [];

for i in range(1, 101):
	if i%2 == 0:
		L.append(i);


print(L)
for i in L:
	if i% 8 == 0 and i < 60:
		print (i)


score = [82, 98, 100, 40, 75, 55, 73];
for i in score:
	if i > 90:
		print ("{} is A". format(score.index(i)+1) );
	elif i > 70:
		print ("{} is B". format(score.index(i)+1) );
	elif i > 50:
		print ("{} is C". format(score.index(i)+1) );
	else:	
		print ("{} is F". format(score.index(i)+1) );

L = [];
a = input("Insert score");
L = list(int(x) for x in a.split())
for i in L:
	if i > 90:
		print ("{} is A". format(L.index(i)+1) );
	elif i > 70:
		print ("{} is B". format(L.index(i)+1) );
	elif i > 50:
		print ("{} is C". format(L.index(i)+1) );
	else:	
		print ("{} is F". format(L.index(i)+1) );

a = input("Please, enter any word : ")
L = list(a);
print(L)
count = 0;
for a in L:
	if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a =='u' :
		count += 1;
	
	if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a =='U' :
		count += 1;

print(count)
