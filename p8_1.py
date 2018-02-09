## p1
L = [3,7,6,11,5];

L2 = L[1 :] + L[0:1];
print (L2)

## p2
L = [ [1,2,3], [1,4], [7], [1,3,5,7] ]
L2 = [];
for i in L:
	sum = 0;
	for j in i:
		sum = sum + j*j;	
	L2.append(sum);	

print(L2)


##p3
data = input("Enter string:")
data_list = data.split(" ");
print("number of words in s : {}".format(len(data_list) ) ) 

sum = 0
for i in data_list:
	sum = sum + len(i);	

print("average length : {}". format(sum/len(data_list) ) )

