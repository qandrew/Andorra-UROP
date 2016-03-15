# a = [1,2,3]
# b = a[:]
# b[2] = 5
# print a,b

rocks = [[3,0],[3,2],[0,4]]
print [0,5] in rocks




# def pack(tentSize, missingSquares):
# 	# Take care to return a list of dictionaries with keys:
# 	#  "anchor": [x,y]
# 	#  "orientation": 0/1

# 	#preprocessing
# 	tent = [[None for x in xrange(tentSize[1])] for y in xrange(tentSize[0])]
# 	anchor = []
# 	#print tent
# 	for i in xrange(len(missingSquares)):
# 		tent[missingSquares[i][0]][missingSquares[i][1]] = 'ROCK!' #fill in rocks
# 	max_arrangement = 0

# 	tent, maximal = recurse_check(tent,max_arrangement,0,0)
# 	return tent, maximal

# def recurse_check(tent, maximal,x,y):
# 	#check if free
# 	if x >= len(tent[0]): #go down to new line
# 		x -= len(tent[0]) #width
# 		y += 1
# 	if y >= len(tent): #we have checked whole matrix, height
# 		print "looked thru"
# 		return tent, maximal

# 	print '______________'
# 	print "now at: ", y,x, maximal 
# 	print tent
# 	#print tent[y][x], tent[y+1][x], tent[y+2][y]

# 	#preprocess
# 	maximal_a, maximal_b, maximal_c = 0,0,0
# 	tent_a = list(tent)
# 	tent_b = list(tent)
# 	tent_c = list(tent)

# 	if x +2 < len(tent[0]): #check horizontally
# 		if (tent[y][x] == None) and (tent[y][x+1] == None) and (tent[y][x+2] == None):
# 			print 'horiz'
# 			tent_b[y][x] = [x,y]
# 			tent_b[y][x+1] = [x,y]
# 			tent_b[y][x+2] = [x,y]
# 			tent_b, maximal_b = recurse_check(tent_b,maximal+1,x+3,y)
# 	if y +2 < len(tent): #check vertically
# 		if (tent[y][x] == None) and (tent[y+1][x] == None) and (tent[y+2][x] == None):
# 			print 'vert'
# 			tent_c[y][x] = [x,y]
# 			tent_c[y+1][x] = [x,y]
# 			tent_c[y+2][x] = [x,y]
# 			tent_c, maximal_c = recurse_check(tent_c,maximal+1,x+1,y)
# 	#else: #we cannot make a bed starting from this location
# 	tent_a, maximal_a = recurse_check(tent_a,maximal,x+1,y)

# 	#return maximal solution
# 	if maximal_a == max(maximal_a,maximal_b,maximal_c):
# 		print 'going up to ', x, y
# 		return tent_a, maximal_a
# 	elif maximal_b == max(maximal_a,maximal_b,maximal_c):
# 		print 'going up to ', x, y
# 		return tent_b, maximal_b
# 	elif maximal_c == max(maximal_a,maximal_b,maximal_c):
# 		print 'going up to', x, y
# 		return tent_c, maximal_c

# 	#return tent, maximal


# if __name__ == '__main__':
# 	tent_s = [3,4]
# 	#rocks = [[3,0],[3,2],[0,4]]
# 	rocks = []
# 	print pack(tent_s,rocks)