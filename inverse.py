import math

a = raw_input("Enter a: ")
a = int(a)

b = raw_input("Enter b: ")
b = int(b)

print "Finding the inverse of %d(mod %d)" % (b, a)

a0 = a
b0 = b
t0 = 0
t = 1
q = math.floor(float(a0)/b0)
r = a0 - (q*b0)

while r > 0:
	temp = (t0 - (q*t)) % a 
	t0 = t
	t = temp
	a0 = b0
	b0 = r
	q = math.floor(float(a0)/b0)
	r = a0 - (q*b0)

if(b0 != 1):
	print "%d(mod %d) has no inverse" % (b, a)
else:
	print "The inverse of %d(mod %d) is %d(mod %d)" % (b, a, t, a)
