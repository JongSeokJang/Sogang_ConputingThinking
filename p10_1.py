def f(x):
	return 2*x +7
def g(x):
	return x*x*x;


for ii in range(-9,10):

	print("x={:2d}: {:>10.2f}".format(ii, f(ii)+g(ii)+f(g(ii)) +g(f(ii)) ) )
print("Done")
