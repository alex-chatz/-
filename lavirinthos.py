import random
#ftiaxnw ton pinaka
Labyrinth = [[0 for x in range (10)] for x in range(10)]
for x in range(0,10):
	for y in range(0,10):
		Labyrinth[x][y] = " "
#tixaies sintetagmenes
a = random.randrange(0,10)
b = random.randrange(0,10)
Labyrinth[a][b] = "Me"
print Labyrinth[a][b]
print a,b
c = random.randrange(0,10)
d = random.randrange(0,10)
Labyrinth[c][d] = "End"
print Labyrinth[c][d]
print c,d
sum = 0
for x in range(0,10):
	for y in range(0,10):
		if Labyrinth[x][y] == " ":
			print "|  ",Labyrinth[x][y],"  ",
			if y == 9 :
				print "|" 

		elif Labyrinth[x][y] == "Me":
			print "|    ",Labyrinth[x][y],
			if y == 9:
				print "|"
		elif Labyrinth[x][y] == "End":
			print "| ",Labyrinth[x][y]," ",
			if y == 9:
				print "|"
		sum = sum + 1
#an o xristis patisei s
while Labyrinth[a][b] != Labyrinth[c][d]:
	inp = raw_input("Use wasd keys to move and then press enter")
	if inp == "s":
		a = a + 1
		print a
		if a == 10:
			a = 0
		for x in range(0,10):
			for y in range(0,10):
				Labyrinth[x][y] = " "
		Labyrinth[a][b] = "Me"
		Labyrinth[c][d] = "End"

		for x in range(0,10):
			for y in range(0,10):
				if Labyrinth[x][y] == " ":
					print "|  ",Labyrinth[x][y],"  ",
					if y == 9 :
						print "|" 

				elif Labyrinth[x][y] == "Me":
					print "|    ",Labyrinth[x][y],
					if y == 9:
						print "|"
				elif Labyrinth[x][y] == "End":
					print "| ",Labyrinth[x][y]," ",
					if y == 9:
						print "|"
#an o xristis patisei w
	elif inp == "w":
		a = a - 1
		print a
		if a == -1:
			a = 9
		for x in range(0,10):
			for y in range(0,10):
				Labyrinth[x][y] = " "
		Labyrinth[a][b] = "Me"
		Labyrinth[c][d] = "End"

		for x in range(0,10):
			for y in range(0,10):
				if Labyrinth[x][y] == " ":
					print "|  ",Labyrinth[x][y],"  ",
					if y == 9 :
						print "|" 

				elif Labyrinth[x][y] == "Me":
					print "|    ",Labyrinth[x][y],
					if y == 9:
						print "|"
				elif Labyrinth[x][y] == "End":
					print "| ",Labyrinth[x][y]," ",
					if y == 9:
						print "|"
#an o xristis patisei d
	elif inp == "d":
		b = b + 1
		print b
		if b == 10:
			b = 0
		for x in range(0,10):
			for y in range(0,10):
				Labyrinth[x][y] = " "
		Labyrinth[a][b] = "Me"
		Labyrinth[c][d] = "End"

		for x in range(0,10):
			for y in range(0,10):
				if Labyrinth[x][y] == " ":
					print "|  ",Labyrinth[x][y],"  ",
					if y == 9 :
						print "|" 

				elif Labyrinth[x][y] == "Me":
					print "|    ",Labyrinth[x][y],
					if y == 9:
						print "|"
				elif Labyrinth[x][y] == "End":
					print "| ",Labyrinth[x][y]," ",
					if y == 9:
						print "|"
#an o xristis patisei a
	elif inp == "a":
		b = b - 1
		print b
		if b == -1:
			b = 9
		for x in range(0,10):
			for y in range(0,10):
				Labyrinth[x][y] = " "
		Labyrinth[a][b] = "Me"
		Labyrinth[c][d] = "End"

		for x in range(0,10):
			for y in range(0,10):
				if Labyrinth[x][y] == " ":
					print "|  ",Labyrinth[x][y],"  ",
					if y == 9 :
						print "|" 

				elif Labyrinth[x][y] == "Me":
					print "|    ",Labyrinth[x][y],
					if y == 9:
						print "|"
				elif Labyrinth[x][y] == "End":
					print "| ",Labyrinth[x][y]," ",
					if y == 9:
						print "|"
print "CONGRATULATIONS!!!!"


