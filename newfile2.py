g_lboardLetters = ["A",
	"B",
	"C",
	"D",
	"E",
	"F",
	"G",
	"H"]
	
########################

class ChessPiece:
	def __init__(self, type, posX, posY):
		self.type = type
		self.posX = posX
		self.posY = posY
	
	#get board letter pos
	def GetBoardLetter(self, count=2):
		global g_lboardLetters
		
		letters = ""
		
		for i in range(count):
			letters += g_lboardLetters[self.posX]
		
		return letters
		
	#get board num pos
	def GetBoardNum(self):
		return self.posY + 1
		
	def GetBoardPos(self, count=2):
		return self.GetBoardLetter(count) + str(self.GetBoardNum())
		
	def IsBoardPosEqualsTo(self, otherBoardPos):
		#otherLetter = otherBoardPos[:2]
		#otherNumber = str(otherBoardPos[2:])
		if(self.GetBoardPos() == otherBoardPos):
			return true
		else:
			return false

########################

def sum(a, b):
	return a + b

def printPawn(posX, posY):
	for i in range(8):
		for j in range(8):
			if(i == posX and j == posY):
				print("p", end='')
			else:
				print("=", end='')
		print()
		

def printPiece(chessPiece):
	for i in range(8):
		for j in range(8):
			if(i == chessPiece.posX and j == chessPiece.posY):
				print(chessPiece.type, end='')
			else:
				print("=", end='')
		print()
		
		
def printPieces(lchessPieces):
	global g_lboardLetters
	
	#print the first row
	print("0", end='')
	#print letters row
	for i in range(8):
		print("|" + g_lboardLetters[i] + g_lboardLetters[i], end='')
	print("|0")
	
	#print the rest of the board
	for i in range(8):
		print(str(i + 1), end='')
		for j in range(8):
			m = -1
			print("|", end='')
			for k in range(len(lchessPieces)):
				if(i == lchessPieces[k].posX and j == lchessPieces[k].posY):
					m = k
					break
			if(m != -1):
				print(lchessPieces[m].type, end='')
			else:
				print("==", end='')
		print("|" + str(i + 1))
	
	#print letters row
	print("0", end='')
	for i in range(8):
		print("|" + g_lboardLetters[i] + g_lboardLetters[i], end='')
	print("|0")



pawnPiece = ChessPiece("wk", 0, 0)
myPieces = [ChessPiece("wq", 0, 0), ChessPiece("wk", 3, 3), 
ChessPiece("wb", 1, 1)]

#debug info
print("sum = " + str(sum(1, 2)) + "\nlen = " + str(len(myPieces)))
#printPawn(2, 0)

#print all pieces
printPieces(myPieces)

print("Pos " + myPieces[1].GetBoardPos())

otherPos = "DD4"

print(otherPos + " is equals to " + myPieces[1].GetBoardPos() + "? " + str(myPieces[1].IsBoardPosEqualsTo(otherPos)))

#get user input
inp_from = input("From:")
inp_to = input("(" + inp_from + ") To:")

print(inp_from + ">" + inp_to)