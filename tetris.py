import random
def makeL(a,b,Tetris):
	#ftiaxno to L
	Tetris[a-2][b] = 1
	Tetris[a-1][b] = 1
	Tetris[a][b] = 1
	Tetris[a][b+1] = 1

	return Tetris

def main():

	sum = 0
	#dimiourgo ton pinaka
	Tetris = [[0 for x in xrange (10)] for x in xrange(23)]
	for x in xrange(23):
		for y in xrange(10):
			Tetris[x][y] = 0
	flag = 0
	while flag == 0:
		#tyxaies sintetagmenes
		a = random.randrange(0,20)
		b = random.randrange(0,9)
		#proipotheseis
		if Tetris[a][b] == 0:	
			if ((a == 19) and (Tetris[a][b+1] == 0)):
				makeL(a,b,Tetris)
				sum = sum + 1
			if ((Tetris[a+1][b] == 1 or Tetris[a+1][b+1]  == 1) and (Tetris[a][b+1] == 0)):
				makeL(a,b,Tetris)
				sum = sum + 1
		#an simplirothei o pinakas to flag ginetai 1 gia na stamatisei i epanalipsi
		if 1 in Tetris[0]: flag = 1

	# for x in xrange(23):
	# 	print x,Tetris[x]
	#an ksexilisei na afairesei to teleftaio block
	if 1 in Tetris[22]: sum = sum - 1

	print "Were included ",sum," L blocks in the game"

main()