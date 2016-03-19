import time
a = {}

for i in xrange(100000):
	if i%3 == 0:
		a[i] = 3*i

print len(a.keys())

start = time.time()

huding = 0
for i in xrange(500):
	if i in a.keys():
		huding += 1

elapsed = time.time() - start
print elapsed

print ''

start = time.time()

huding = 0
for i in xrange(500):
	if i in a:
		huding += 1

elapsed = time.time() - start
print elapsed